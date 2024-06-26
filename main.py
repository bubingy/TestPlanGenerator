import os
import argparse

import app
from DiagToolWeekly.configuration import AzureConfig
from DiagToolWeekly.configuration import DiagToolWeeklyTestconfig
from DiagToolWeekly.configuration import LTTngWeeklyTestconfig
from DiagToolWeekly import test_plan as diag_tool_test_plan


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        '--type',
        dest='project_type',
        choices=['diag-weekly', 'generation-aware']
    )
    args = parser.parse_args()

    project_type = args.project_type

    azure_config_path = os.path.join(app.script_root, 'Config', 'azure.conf')
    diag_tool_weekly_config_path = os.path.join(app.script_root, 'Config', 'weekly_test.conf')

    azure_config = AzureConfig(azure_config_path)
    diag_tool_test_config = DiagToolWeeklyTestconfig(diag_tool_weekly_config_path)
    lttng_config = LTTngWeeklyTestconfig(diag_tool_weekly_config_path)

    if project_type == 'diag-weekly':
        diag_tool_test_plan.generate_diag_tool_weekly_test_plan(azure_config,diag_tool_test_config, lttng_config)