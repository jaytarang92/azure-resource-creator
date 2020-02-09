from azure.mgmt.resource import ResourceManagementClient


class ResourceManager(ResourceManagementClient):

    def __init__(self, sp_credentials=None, subscription_id=None):
        self.service_principal_credentials = sp_credentials
        self.subscription_id = subscription_id
        self.client = ResourceManagementClient(self.service_principal_credentials, self.subscription_id)

    def list(self):
        return self.client.resource_groups.list()

    def exists(self, resource_group_name=None):
        if resource_group_name is not None:
            for rg in self.list():
                if rg.name.lower() == resource_group_name.lower():
                    return True
        return False

    def create(self, resource_group_name=None, location=None):
        _location = location or 'eastus'
        if resource_group_name is not None and not self.exists(resource_group_name):
            print(f'Creating new resource group: {resource_group_name}')
            return self.client.resource_groups.create_or_update(resource_group_name, {'location': _location})
        raise ValueError('Resource group name cannot be None')

    def delete(self, resource_group_name=None):
        if resource_group_name is not None and self.exists(resource_group_name):
            print(f'Deleting resource group: {resource_group_name}')
            return self.client.resource_groups.delete(resource_group_name)
        raise ValueError(f'Resource group {resource_group_name} does not exist')

