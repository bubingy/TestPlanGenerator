import os

import app
from GenerationAwareAnalyze.configuration import GithubConfig
from tools import github_service


class GenerationAwareTestInfo:
    def __init__(self, runtime_commit_info: dict, blog_samples_commit_info: dict) -> None:
        self.runtime_commit_info = runtime_commit_info
        self.blog_samples_commit_info = blog_samples_commit_info


@app.function_monitor(
    pre_run_msg='start to latest commit for runtime and blog-samples'
)
def get_generation_aware_test_info(github_config: GithubConfig) -> GenerationAwareTestInfo | Exception:
    latest_runtime_commit = github_service.get_latest_commit(
        github_config.token,
        github_config.runtime_owner,
        github_config.runtime_repo
    )

    if isinstance(latest_runtime_commit, Exception):
        return latest_runtime_commit
    
    latest_blog_samples_commit = github_service.get_latest_commit(
        github_config.token,
        github_config.blog_samples_owner,
        github_config.blog_samples_repo
    )

    if isinstance(latest_blog_samples_commit, Exception):
        return latest_blog_samples_commit
    
    return GenerationAwareTestInfo(latest_runtime_commit, latest_blog_samples_commit)