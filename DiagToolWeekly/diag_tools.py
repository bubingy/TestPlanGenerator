import os
import zipfile
import tempfile
from xml.etree import ElementTree as ET

import app
from DiagToolWeekly.configuration import AzureConfig
from tools import azure_service


class DiagnosticToolsInfo:
    def __init__(self, build_id: str, diag_tool_version: str) -> None:
        self.build_id: str = build_id
        self.diag_tool_version: str = diag_tool_version


@app.function_monitor(
    pre_run_msg='start to query latest diagnostic tool'
)
def get_latest_diagnostic_tool_info(azure_config: AzureConfig) -> DiagnosticToolsInfo | Exception:
    build_info = azure_service.get_latest_acceptable_build(
        azure_config.pat,
        azure_config.diag_tools_organization,
        azure_config.diag_tools_project,
        azure_config.diag_tools_pipeline_id
    )

    if isinstance(build_info, Exception):
        return build_info
    build_id = build_info['id']

    artifact_info = azure_service.get_artifact(
        azure_config.pat,
        azure_config.diag_tools_organization,
        azure_config.diag_tools_project,
        build_id,
        'AssetManifests'
    )
    
    if isinstance(artifact_info, Exception):
        return artifact_info
    artifact_download_url = artifact_info['resource']['downloadUrl']

    with tempfile.TemporaryDirectory() as tempdir:
        # download AssetManifests.zip
        file_path = azure_service.download_artifact(
            azure_config.pat,
            'AssetManifests',
            artifact_download_url,
            tempdir
        )

        if isinstance(file_path, Exception):
            return file_path
        
        try:
            # extract zip
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(tempdir)

            xml_path = os.path.join(tempdir, 'AssetManifests', 'Windows_NT-AnyCPU.xml')
            tree = ET.parse(xml_path)
            root = tree.getroot()
            version = root.findall(
                '''.//Package[@Id='dotnet-counters']'''
            )[0].attrib['Version']
            return DiagnosticToolsInfo(build_id, version)
        except Exception as ex:
            return Exception(f'fail to get diagnostic tools version from build-{build_id}: {ex}')

