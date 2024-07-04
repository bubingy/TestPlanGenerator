import os

import app
from DiagToolWeekly.configuration import AzureConfig
from DiagToolWeekly.configuration import DiagToolWeeklyTestconfig
from DiagToolWeekly.configuration import LTTngWeeklyTestconfig
from DiagToolWeekly import test_plan as diag_tool_test_plan
from GenerationAwareAnalyze.configuration import GithubConfig
from GenerationAwareAnalyze import test_plan as generation_aware_test_plan


def generate_test_plan(project_type: str):
    if project_type == 'diag-weekly':
        azure_config_path = os.path.join(app.script_root, 'Config', 'azure.conf')
        diag_tool_weekly_config_path = os.path.join(app.script_root, 'Config', 'weekly_test.conf')

        azure_config = AzureConfig(azure_config_path)
        diag_tool_test_config = DiagToolWeeklyTestconfig(diag_tool_weekly_config_path)
        lttng_config = LTTngWeeklyTestconfig(diag_tool_weekly_config_path)
        diag_tool_test_plan.generate_diag_tool_weekly_test_plan(azure_config, diag_tool_test_config, lttng_config)
    elif project_type == 'generation-aware':
        github_config_path = os.path.join(app.script_root, 'Config', 'github.conf')
        github_config = GithubConfig(github_config_path)
        
        generation_aware_test_plan.generate_generation_aware_test_plan(github_config)

    else:
        print(f'unknown project tpye: {project_type}')