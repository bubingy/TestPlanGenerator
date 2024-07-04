import os
import json

from DiagToolWeekly import record


def summarize_diag_tool_test_plan(project_root: str):

    for project_name in os.listdir(project_root):
        project_path = os.path.join(project_root, project_name)

        # if it's not a folder, just ignore
        if not os.path.isdir(project_path):
            continue

        # collect week info
        week_info_json_path = os.path.join()
        week_info = record.load_week_info_from_json(week_info_json_path)
