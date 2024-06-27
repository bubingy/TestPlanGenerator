import app
from DiagToolWeekly.configuration import DiagToolWeeklyTestconfig

@app.function_monitor(
    pre_run_msg='get required operating systems and their sdk branch for this week'
)
def get_required_os_sdk_map(diag_conf: DiagToolWeeklyTestconfig) -> dict:
    required_os_sdk_map = dict()
    for idx, os_name in enumerate(diag_conf.last_week_required_os_list):
        last_week_sdk_branch = diag_conf.last_week_required_os_sdk_branch_list[idx]
        if last_week_sdk_branch in diag_conf.SDK_major_version_list:
            last_week_sdk_branch_idx = diag_conf.SDK_major_version_list.index(last_week_sdk_branch)
            required_os_this_week_test_branch_idx = \
                (last_week_sdk_branch_idx + 1) % len(diag_conf.SDK_major_version_list)
            required_os_sdk_map[os_name] = diag_conf.SDK_major_version_list[required_os_this_week_test_branch_idx]
        else:
            required_os_sdk_map[os_name] = diag_conf.SDK_major_version_list[idx % len(diag_conf.SDK_major_version_list)]
    return required_os_sdk_map


@app.function_monitor(
    pre_run_msg='get alternate operating systems and their sdk branch for this week'
)
def get_alternate_os_sdk_map(diag_conf: DiagToolWeeklyTestconfig) -> dict:
    alternate_os_sdk_map = dict()
    first_alternate_os_index = \
        diag_conf.alternate_os_list.index(diag_conf.last_week_alternate_os_list[0]) + len(diag_conf.last_week_alternate_os_list)
    
    for idx, sdk_major_version in enumerate(diag_conf.SDK_major_version_list):
        alternate_os_sdk_map[sdk_major_version] = \
            diag_conf.alternate_os_list[(first_alternate_os_index+idx) % len(diag_conf.alternate_os_list)]

    return alternate_os_sdk_map


def get_os_rotation(diag_conf: DiagToolWeeklyTestconfig):
    required_os_status = get_required_os_sdk_map(diag_conf)
    alternate_os_status = get_alternate_os_sdk_map(diag_conf)

    os_rotation = dict()
    os_rotation['requiredOS'] = required_os_status
    os_rotation['alternateOS'] = alternate_os_status

    return os_rotation