import configparser


class GithubConfig:
    def __init__(self, conf_file_path: str) -> None:
        self.__parse_conf_file(conf_file_path)

    def __parse_conf_file(self, conf_file_path: str) -> None:
        '''Parse configuration file 
        
        :param conf_file_path: path to configuration file
        :return: GithubConfig instance or Exception
        '''
        try:
            config = configparser.ConfigParser()
            config.read(conf_file_path)

            self.output_folder = config['Output']['projectRoot']

            self.runtime_owner: str = config['runtime']['owner']
            self.runtime_repo: str = config['runtime']['repo']

            self.blog_samples_owner: str = config['blog-samples']['owner']
            self.blog_samples_repo: str = config['blog-samples']['repo']

            self.token: str = config['Auth']['token']
                
        except Exception as ex:
            raise Exception(f'fail to parse conf file {conf_file_path}: {ex}')  