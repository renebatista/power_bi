# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'MasterUser'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '1e429e3e-98f4-4459-841e-6578855e5020'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = 'e8c6f8d4-bd2e-4b46-862a-feb39921be14'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = 'da02d7a6-5248-43a2-812e-dc9bffc4bda5'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = 'f4978d71-3dc9-4400-8741-2d8669babc86'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 's2p8Q~DnPhodHwAFLsFGgTRP9psP6aI.BwaJqbje'
    
    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = 'admin@robbysonsystems.onmicrosoft.com'
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = 'Home2020*'