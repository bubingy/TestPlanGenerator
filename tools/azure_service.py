import os
import json
import base64
from urllib import request


def convert_pat(pat: str):
    authorization_string = str(
        base64.b64encode(bytes(f':{pat}', 'ascii')),
        'ascii'
    )
    return authorization_string


def get_latest_acceptable_build(pat: str,
                                organization: str,
                                project: str,
                                definition_id: int,
                                branch_name: str='main') -> dict|Exception:
    '''Get latest successful or partially successful build of specified pipeline.

    :param pat: personal access token.
    :param organization: name of the Azure DevOps organization.
    :param project: project name.
    :param definition_id: definition id.
    :param branch_name: branch name.
    :return: the latest successful or partially successful build.
    '''
    authorization = convert_pat(pat)
    url = (
        f'https://dev.azure.com/{organization}/{project}/_apis/build/builds?'
        f'definitions={definition_id}'
        f'&branchName=refs/heads/{branch_name}'
        f'&reasonFilter=schedule,batchedCI'
        f'&resultFilter=succeeded,partiallySucceeded'
        '&queryOrder=startTimeDescending'
        '&$top=1'
        '&api-version=7.2-preview.7'
    )
    try:
        response = request.urlopen(
            request.Request(
                url,
                headers={
                    'Authorization': f'Basic {authorization}'
                }   
            )
        )
        response_content = response.read().decode('utf-8')
        build = json.loads(response_content)['value'][0]
        return build
    except Exception as ex:
        return Exception(f'fail to get latest acceptable build in {organization}/{project}: {ex}')


def get_artifact(pat: str,
                 organization: str,
                 project: str,
                 build_id: str,
                 artifact_name: str) -> dict|Exception:
    '''Get artifact according to the given `build_id` and `artifact_name`.

    :param pat: personal access token.
    :param organization: name of the Azure DevOps organization.
    :param project: project name.
    :param build_id: build id.
    :param artifact_name: name of artifact.
    :return: artifact information of build.
    '''
    authorization = convert_pat(pat)
    url = (
        f'https://dev.azure.com/{organization}/{project}/_apis/'
        f'build/builds/{build_id}/artifacts?'
        f'artifactName={artifact_name}&api-version=7.2-preview.5'
    )
    try:
        response = request.urlopen(
            request.Request(
                url,
                headers={
                    'Authorization': f'Basic {authorization}'
                }
            )
        )
        artifact = json.loads(response.read().decode())
        return artifact
    except Exception as ex:
        return Exception(f'fail to get artifact {artifact_name} of build {build_id}: {ex}')


def download_artifact(pat: str, download_url: str, output_dir: str, buffer_size: int=2097152) -> str|Exception:
    authorization = convert_pat(pat)
    try:
        response = request.urlopen(
            request.Request(
                download_url,
                headers={
                    'Authorization': f'Basic {authorization}'
                }
            )
        )

        file_name = os.path.basename(download_url)
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, 'wb+') as out:
            while True:
                buffer = response.read(buffer_size)
                if not buffer: break
                out.write(buffer)
        return file_path
    
    except Exception as ex:
        return Exception(f'fail to download {download_url} to {output_dir}: {ex}')