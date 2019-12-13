# coding=utf-8

import unittest
from lib.browser_engine import BrowserEngine
from pageobjects.atmos_login_page import AtmosLogin
from pageobjects.atmos_system_dasboard_page import AtmosSysDashBoard
from pageobjects.atmos_tenant_dashboard_page import AtmosTntDashBoard
from config import config
from lib.logger import Logger

# create a logger instance
logger = Logger(logger="AtmosGUILogin").getlog()

class AtmosGUILogion(unittest.TestCase):
    mauiadmin_user_name = config.MAUI_ADMIN
    mauiadmin_password = config.MAUI_ADMIN_PASSWORD
    tenant_name = config.TENANT_NAME
    tenant_admin_name = config.TENANT_ADMIN
    tenant_admin_password = config.TENANT_PASSWORD
    browser = BrowserEngine

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_atmos_maui_admin_logion(self):
        logger.info ("********* Start case: test_atmos_maui_admin_logion *********")
        atmoslogin = AtmosLogin(self.driver)
        atmoslogin.click_mauadmin_login_link()
        atmoslogin.type_user_name(self.mauiadmin_user_name)
        atmoslogin.type_password(self.mauiadmin_password)
        atmoslogin.click_login_btn()
        atmoslogin.select_frame('mainFrame')
        #check: mauiadmin success to login
        atmossys = AtmosSysDashBoard(self.driver)
        self.assertTrue(atmossys.is_sys_dashboard_display(),msg = 'System Dashboard displayed')
        atmoslogin.get_windows_img()

    def test_atmos_tenant_login(self):
        logger.info( "********* Start case: test_atmos_tenant_login *********")
        atmoslogin = AtmosLogin(self.driver)
        atmoslogin.select_frame('topFrame')
        atmoslogin.click("xpath=>//img[@id='logout']")
        atmoslogin.accept_alert()
        atmoslogin.switch_todefault()
        atmoslogin.click_tenant_login_link()
        atmoslogin.type_tenant_name(self.tenant_name)
        atmoslogin.type_tnt_user_name(self.tenant_admin_name)
        atmoslogin.type_password(self.tenant_admin_password)
        atmoslogin.click_login_btn()
        atmoslogin.get_windows_img()
        atmoslogin.select_frame('mainFrame')
        #check: tenant success to login
        atmostnt = AtmosTntDashBoard(self.driver)
        self.assertTrue(atmostnt.is_tnt_dashboard_display(),msg = 'Tenant Dashboard displayed')
        atmoslogin.get_windows_img()

if __name__ == '__main__':
    unittest.main()
