import os
import configparser


class AzureConfig:
    def __init__(self, conf_file_path: str) -> None:
        self.__parse_conf_file(conf_file_path)

    def __parse_conf_file(self, conf_file_path: str) -> None:
        '''Parse configuration file 
        
        :param conf_file_path: path to configuration file
        :return: AzureConfig instance or Exception
        '''
        try:
            config = configparser.ConfigParser()
            config.read(conf_file_path)

            self.installer_pipeline_id: str = config['Installer']['definition']
            self.installer_organization: str = config['Installer']['organization']
            self.installer_project: str = config['Installer']['project']

            self.diag_tools_pipeline_id: str = config['diagnostics']['definition']
            self.diag_tools_organization: str = config['diagnostics']['organization']
            self.diag_tools_project: str = config['diagnostics']['project']

            self.pat: str = config['Auth']['pat']
                
        except Exception as ex:
            raise Exception(f'fail to parse conf file {conf_file_path}: {ex}')    
        

class DiagToolWeeklyTestconfig:
    def __init__(self, conf_file_path: str) -> None:
        self.__parse_conf_file(conf_file_path)

    def __parse_conf_file(self, conf_file_path: str) -> None:
        '''Parse configuration file 
        
        :param conf_file_path: path to configuration file
        :return: DiagToolWeeklyTestconfig instance or Exception
        '''
        try:
            config = configparser.ConfigParser()
            config.read(conf_file_path)

            self.output_folder = config['Output']['projectRoot']

            self.SDK_major_version_list = config['Branch']['major'].split('\n')
            self.SDK_major_version_list.remove('')

            self.last_week_required_os_list = config['DiagToolsTestLastWeekConfig']['requiredOS'].split('\n')
            self.last_week_required_os_list.remove('')

            self.last_week_required_os_sdk_branch_list = config['DiagToolsTestLastWeekConfig']['requiredOSSDKBranch'].split('\n')
            self.last_week_required_os_sdk_branch_list.remove('')

            self.last_week_alternate_os_list = config['DiagToolsTestLastWeekConfig']['alternateOS'].split('\n')
            self.last_week_alternate_os_list.remove('')

            self.last_week_alternate_os_sdk_branch_list = config['DiagToolsTestLastWeekConfig']['alternateOSSDKBranch'].split('\n')
            self.last_week_alternate_os_sdk_branch_list.remove('')

            self.alternate_os_list = config['DiagToolsTest']['alternateOSTable'].split('\n')
            self.alternate_os_list.remove('')

        except Exception as ex:
            raise Exception(f'fail to parse conf file {conf_file_path}: {ex}')    


class LTTngWeeklyTestconfig:
    def __init__(self, conf_file_path: str) -> None:
        self.__parse_conf_file(conf_file_path)

    def __parse_conf_file(self, conf_file_path: str) -> None:
        '''Parse configuration file 
        
        :param conf_file_path: path to configuration file
        :return: DiagToolWeeklyTestconfig instance or Exception
        '''
        try:
            config = configparser.ConfigParser()
            config.read(conf_file_path)
            
            self.output_folder = config['Output']['projectRoot']
            
            self.SDK_major_version_list = config['Branch']['major'].split('\n')
            self.SDK_major_version_list.remove('')
            
            self.lttng_os_list = config['LTTngTest']['os'].split('\n')
            self.lttng_os_list.remove('')
        
        except Exception as ex:
            raise Exception(f'fail to parse conf file {conf_file_path}: {ex}')    