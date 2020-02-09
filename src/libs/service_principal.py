from azure.common.credentials import ServicePrincipalCredentials
from json import loads


class ServicePrincipal(object):

    def __init__(self, sp_config_dict):
        self.client_id = sp_config_dict['appId']
        self.secret = sp_config_dict['password']
        self.subscription_id = sp_config_dict.get('subscription_id')
        self.tenant = sp_config_dict['tenant']


class ServicePrincipalCreator:

    def __init__(self, path_to_sp_config='service-principal.json'):
        self.path_to_sp_config = path_to_sp_config

    def create_sp_object(self):
        try:
            with open(self.path_to_sp_config, 'r') as sp_config_file:
                _service_principal = ServicePrincipal(loads(sp_config_file.read()))
                return _service_principal
        except IOError:
            raise FileExistsError(f'{self.path_to_sp_config}: file does not exist.')

    def create_sp_from_credentials(self, sp_object=None):
        if sp_object is None:
            sp_object = self.create_sp_object()
        return ServicePrincipalCredentials(client_id=sp_object.client_id, secret=sp_object.secret,
                                           tenant=sp_object.tenant)
