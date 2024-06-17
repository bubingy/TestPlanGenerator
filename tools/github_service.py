# coding=utf-8

import json
from urllib import request


def get_latest_commit_of_main(token: str, owner: str, repo: str) -> list:
    '''get latest commit of given repo(main branch).

    :param token: github token.
    :param owner: name of the Azure DevOps organization.
    :param repo: project name.
    :return: latest commit of main.
    '''
    url = f'https://api.github.com/repos/{owner}/{repo}/commits?per_page=1'
    try:
        response = request.urlopen(
            request.Request(
                url,
                headers={
                    'Authorization': f'Bearer {token}'
                }
            )
        )
        commit = json.loads(response.read().decode())
        return commit
    
    except Exception as ex:
        return Exception(f'Fail to get latest commit from {owner}/{repo}: {ex}')