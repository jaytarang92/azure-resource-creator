from libs.azure_resource_manager import ResourceManager
from libs.service_principal import ServicePrincipalCreator

sp_creator = ServicePrincipalCreator()
sp_object = sp_creator.create_sp_object()
sp_credentials = sp_creator.create_sp_from_credentials(sp_object)

rg = ResourceManager(sp_credentials, sp_object.subscription_id)
print(rg.delete(resource_group_name='test1234'))
print(rg.delete(resource_group_name='test123'))