import json
from urllib import request


def get_latest_commit(token: str, owner: str, repo: str, branch: str='main') -> dict|Exception:
    '''get latest commit of given repo(main branch by default).

    :param token: github token.
    :param owner: name of the Azure DevOps organization.
    :param repo: project name.
    :return: latest commit of main.
    '''
    url = f'https://api.github.com/repos/{owner}/{repo}/commits?sha={branch}&per_page=1'
    try:
        response = request.urlopen(
            request.Request(
                url,
                headers={
                    'Authorization': f'Bearer {token}'
                }
            )
        )
        response_content = response.read().decode('utf-8')
        commit = json.loads(response_content)[0]
        return commit
    
    except Exception as ex:
        return Exception(f'Fail to get latest commit from {owner}/{repo}: {ex}')