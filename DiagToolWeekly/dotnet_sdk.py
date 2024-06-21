import os
import glob
import zipfile
import tempfile
from urllib import request
from xml.etree import ElementTree as ET

import app
from DiagToolWeekly.configuration import AzureConfig
from tools import azure_service


class DotnetSDKInfo:
    def __init__(self, branch_name: str, dotnet_sdk_version: str) -> None:
        self.branch_name = branch_name
        self.dotnet_sdk_version = dotnet_sdk_version


@app.function_monitor(
    pre_run_msg='start to query latest .NET SDK'
)
def get_latest_sdk_info_by_branch_name(azure_config: AzureConfig, branch_name: str) -> DotnetSDKInfo | Exception:
    build_info = azure_service.get_latest_acceptable_build(
        azure_config.pat,
        azure_config.installer_organization,
        azure_config.installer_project,
        azure_config.installer_pipeline_id
    )

    if isinstance(build_info, Exception):
        return build_info
    build_id = build_info['id']
    
    artifact_info = azure_service.get_artifact(
        azure_config.pat,
        azure_config.installer_organization,
        azure_config.installer_project,
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
            artifact_download_url,
            tempdir
        )

        if isinstance(file_path, Exception):
            return file_path
        
        try:
            # extract zip
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(tempdir)

            xml_path_pattern = os.path.join(tempdir, 'AssetManifests', '*x64-installers.xml')
            xml_path = glob.glob(xml_path_pattern)[0]

            tree = ET.parse(xml_path)
            root = tree.getroot()
            
            version = root.findall('Blob')[0].attrib['Id'].split('/')[1]
            return DotnetSDKInfo(branch_name, version)
        except Exception as ex:
            return Exception(f'fail to get sdk version from build-{build_id}: {ex}')


