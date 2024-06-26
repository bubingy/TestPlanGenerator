import os
from datetime import datetime

from openpyxl import Workbook

from tools import date_tools
from DiagToolWeekly.configuration import AzureConfig
from DiagToolWeekly.configuration import DiagToolWeeklyTestconfig
from DiagToolWeekly.configuration import LTTngWeeklyTestconfig
from DiagToolWeekly import dotnet_sdk
from DiagToolWeekly import diag_tools
from DiagToolWeekly import os_sdk_table
from DiagToolWeekly import presentation
from DiagToolWeekly import record


def generate_diag_tool_weekly_test_plan(azure_conf: AzureConfig,
                                        diag_conf: DiagToolWeeklyTestconfig,
                                        lttng_conf: LTTngWeeklyTestconfig):
    # create excel
    workbook = Workbook()

    # week info
    today = datetime.today()
    formatted_date_str = today.strftime('%Y-%m-%d')
    week_info = date_tools.get_week_info(formatted_date_str)
    if not isinstance(week_info, Exception):
        presentation.write_week_info_to_sheet(workbook, week_info)
        record.write_week_info_to_json(diag_conf.output_folder, week_info)

    # sdk info
    sdk_info_list = []
    for branch in diag_conf.SDK_major_version_list:
        sdk_info = dotnet_sdk.get_latest_sdk_info_by_branch_name(azure_conf, branch)

        if isinstance(sdk_info, Exception):
            continue

        sdk_info_list.append(sdk_info)

    presentation.write_sdk_info_list_to_sheet(workbook, sdk_info_list)
    record.write_SDKInfo_to_json(diag_conf.output_folder, sdk_info_list)

    # diag tool info
    diag_tool_info = diag_tools.get_latest_diagnostic_tool_info(azure_conf)
    if not isinstance(diag_tool_info, Exception):
        presentation.write_diag_tools_info_to_sheet(workbook, diag_tool_info)
        record.write_diag_tool_info_to_json(diag_conf.output_folder, diag_tool_info)

    # test matrix
    os_sdk_map = os_sdk_table.get_os_rotation(diag_conf)
    presentation.write_weekly_diag_tools_test_matrix_to_sheet(workbook, os_sdk_map)
    record.write_diag_tool_test_matrix_to_json(diag_conf.output_folder, os_sdk_map)

    # lttng info
    presentation.write_weekly_lttng_test_matrix_on_sheet(workbook, lttng_conf)
    record.write_LTTngInfo_to_json(diag_conf.output_folder, lttng_conf)

    # write excel
    excel_path = os.path.join(diag_conf.output_folder, 'testplan.xlsx')
    if os.path.exists(excel_path):
        os.remove(excel_path)
    workbook.save(excel_path)