import os
import configparser


class AzureConfig:
    def __init__(self, conf_file_path: str) -> None:
        self.__parse_conf_file(conf_file_path)

    def __parse_conf_file(self, conf_file_path: str) -> None:
        '''Parse configuration file 
        
        :param conf_file_path: path to configuration file
        :return: DiagToolsTestConfiguration instance or Exception
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
        

class DiagnosticToolsInfo:
    SDK_major_version_list: list[str] = []
    diag_tools_last_week_test_config: dict = dict()

    diag_tools_alternate_os_list: list[str] = []

    LTTng_OS_list: list[str] = []
