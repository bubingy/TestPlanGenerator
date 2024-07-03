import os
from datetime import datetime

from tools import date_tools
from GenerationAwareAnalyze.configuration import GithubConfig
from GenerationAwareAnalyze import generation_aware_test_info
from GenerationAwareAnalyze import record


def generate_generation_aware_test_plan(github_config: GithubConfig):
    if not os.path.exists(github_config.output_folder):
        os.makedirs(github_config.output_folder)

    # week info
    today = datetime.today()
    formatted_date_str = today.strftime('%Y-%m-%d')
    week_info = date_tools.get_week_info(formatted_date_str)
    if not isinstance(week_info, Exception):
        record.write_week_info_to_json(github_config.output_folder, week_info)

    test_info = generation_aware_test_info.get_generation_aware_test_info(github_config)
    if not isinstance(test_info, Exception):
        record.write_generation_aware_test_info_to_json(github_config.output_folder, test_info)