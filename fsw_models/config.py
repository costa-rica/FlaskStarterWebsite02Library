print("- in fsw_models/config.py")
import os
from fsw_config import ConfigDev, ConfigProd, ConfigWorkstation

if os.environ.get('FSW_CONFIG_TYPE')=='workstation':
    config = ConfigWorkstation()
    print('- fsw_models/config: Local')
elif os.environ.get('FSW_CONFIG_TYPE')=='dev':
    config = ConfigDev()
    print('- fsw_models/config: Development')
elif os.environ.get('FSW_CONFIG_TYPE')=='prod':
    config = ConfigProd()
    print('- fsw_models/config: Production')