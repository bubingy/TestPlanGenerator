from DiagToolWeekly.configuration import AzureConfig, DiagToolWeeklyTestconfig
from DiagToolWeekly import os_sdk_table

azure_conf_path = 'E:\\Workspace\\TestPlanGenerator\\Config\\azure.conf'
diag_weekly_conf_path = 'E:\\Workspace\\TestPlanGenerator\\Config\\weekly_test.conf'

azure_conf = AzureConfig(azure_conf_path)
diag_weekly_conf = DiagToolWeeklyTestconfig(diag_weekly_conf_path)

required_os_sdk_map = os_sdk_table.get_required_os_sdk_map(diag_weekly_conf)
print(required_os_sdk_map)

alternate_os_sdk_map = os_sdk_table.get_alternate_os_sdk_map(diag_weekly_conf)
print(alternate_os_sdk_map)