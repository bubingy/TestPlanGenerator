import os
import json

import app
from DiagToolWeekly.dotnet_sdk import DotnetSDKInfo
from DiagToolWeekly.diag_tools import DiagnosticToolsInfo
from DiagToolWeekly.configuration import LTTngWeeklyTestconfig


@app.function_monitor(
    pre_run_msg='write week info to json'
)
def write_week_info_to_json(output_folder: str, week_info: dict) -> None | Exception:
    output_path = os.path.join(output_folder, 'week.json')

    try:
        if os.path.exists(output_path):
            os.remove(output_path)

        with open(output_path, 'w+') as fp:
            json.dump(week_info, fp)
    except Exception as ex:
        return Exception(f'fail to write week info: {ex}')


@app.function_monitor(
    pre_run_msg='load week info from json'
)
def load_week_info_from_json(json_path: str) -> dict | Exception:
    try:
        with open(json_path, 'r') as fp:
            week_info = json.load(fp)
            return week_info
    except Exception as ex:
        return Exception(f'fail to load week info from {json_path}: {ex}')
    

@app.function_monitor(
    pre_run_msg='write sdk info to json'
)
def write_SDKInfo_to_json(output_folder: str, sdk_info_list: list[DotnetSDKInfo]) -> None | Exception:
    output_path = os.path.join(output_folder, 'SDKInfo.json')

    _sdk_info_list = map(
        lambda sdk_info: {
            'branch': sdk_info.branch_name,
            'version': sdk_info.dotnet_sdk_version,
            'buildId': sdk_info.build_id
        },
        sdk_info_list
    )
    
    try:
        if os.path.exists(output_path):
            os.remove(output_path)

        with open(output_path, 'w+') as fp:
            json.dump(list(_sdk_info_list), fp)
    except Exception as ex:
        return Exception(f'fail to write sdk info: {ex}')


@app.function_monitor(
    pre_run_msg='load SDK info list from json'
)
def load_SDK_info_from_json(json_path: str) -> list[DotnetSDKInfo] | Exception:
    SDK_info_list = []
    try:
        with open(json_path, 'r') as fp:
            for SDK_info in json.load(fp):
                SDK_info_list.append(
                    DotnetSDKInfo(
                        SDK_info['branch'],
                        SDK_info['version'],
                        SDK_info['buildId'],
                    )
                )
        return SDK_info_list
    except Exception as ex:
        return Exception(f'fail to load SDK info from {json_path}: {ex}')
    

@app.function_monitor(
    pre_run_msg='write diag tool info to json'
)
def write_diag_tool_info_to_json(output_folder: str, diag_tool_info: DiagnosticToolsInfo) -> None | Exception:
    output_path = os.path.join(output_folder, 'DiagToolInfo.json')

    _diag_tool_info = {
        'version': diag_tool_info.diag_tool_version,
        'buildId': diag_tool_info.build_id
    }
    
    try:
        if os.path.exists(output_path):
            os.remove(output_path)

        with open(output_path, 'w+') as fp:
            json.dump(_diag_tool_info, fp)
    except Exception as ex:
        return Exception(f'fail to write diag tool info: {ex}')


@app.function_monitor(
    pre_run_msg='load diag tool info from json'
)
def load_diag_tool_info_from_json(json_path: str) -> DiagnosticToolsInfo | Exception:
    try:
        with open(json_path, 'r') as fp:
            _diag_tool_info = json.load(fp)
        return DiagnosticToolsInfo(
            _diag_tool_info['buildId'],
            _diag_tool_info['version']
        )
    except Exception as ex:
        return Exception(f'fail to load diag tool info from {json_path}: {ex}')


@app.function_monitor(
    pre_run_msg='write diag tool test matrix to json'
)
def write_diag_tool_test_matrix_to_json(output_folder: str, os_sdk_map: dict) -> None | Exception:
    output_path = os.path.join(output_folder, 'DiagToolTestMatrix.json')

    try:
        if os.path.exists(output_path):
            os.remove(output_path)

        with open(output_path, 'w+') as fp:
            json.dump(os_sdk_map, fp)
    except Exception as ex:
        return Exception(f'fail to write diag tool test matrix: {ex}')
    

@app.function_monitor(
    pre_run_msg='load diag tool test matrix from json'
)
def load_diag_tool_test_matrix_from_json(json_path: str) -> dict | Exception:
    try:
        with open(json_path, 'r') as fp:
            os_sdk_map = json.load(fp)
            return os_sdk_map
    except Exception as ex:
        return Exception(f'fail to load diag tool test matrix from {json_path}: {ex}')
    

@app.function_monitor(
    pre_run_msg='write LTTng test info to json'
)
def write_LTTngInfo_to_json(output_folder: str, lttng_info: LTTngWeeklyTestconfig) -> None | Exception:
    output_path = os.path.join(output_folder, 'LTTngTestInfo.json')

    _lttng_info = {
        'branch': lttng_info.SDK_major_version_list,
        'os': lttng_info.lttng_os_list
    }
    
    try:
        if os.path.exists(output_path):
            os.remove(output_path)

        with open(output_path, 'w+') as fp:
            json.dump(_lttng_info, fp)
    except Exception as ex:
        return Exception(f'fail to write LTTng test info: {ex}')
    

@app.function_monitor(
    pre_run_msg='load LTTng test info from json'
)
def load_LTTngInfo_from_json(json_path: str) -> dict | Exception:
    try:
        with open(json_path, 'r') as fp:
            lttng_info = json.load(fp)
            return lttng_info
    except Exception as ex:
        return Exception(f'fail to load LTTng test info from {json_path}: {ex}')