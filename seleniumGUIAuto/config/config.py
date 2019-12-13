# BROWSER define the browser type (chrome, ie, firefox) for testing
import os
BROWSER = 'chrome'

LOGIN_URL = 'https://10.32.183.17'
LOGIN_URL_slave1 = 'https://10.32.183.18'
LOGIN_URL_slave2 = 'https://10.32.183.21'
LOGIN_URL_slave3 = 'https://10.32.183.22'
MAUI_ADMIN = 'mauiadmin_pit'
MAUI_ADMIN_PASSWORD = 'password'
TENANT_NAME = 'cdp'
TENANT_ADMIN = 'cdp'
TENANT_PASSWORD = 'password'

PROJECT_PATH=os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))