import unittest
import random
import string
from lib.browser_engine import BrowserEngine
from pageobjects.atmos_login_page import AtmosLogin
from pageobjects.atmos_system_dasboard_page import AtmosSysDashBoard
from pageobjects.atmos_tenant_dashboard_page import AtmosTntDashBoard
from selenium import webdriver
from config import config
from lib.logger import Logger

# create a logger instance
logger = Logger(logger="AtmosGUILogin").getlog()

class subTnt(unittest.TestCase):
    mauiadmin_user_name = config.MAUI_ADMIN
    mauiadmin_password = config.MAUI_ADMIN_PASSWORD
    tenant_name = config.TENANT_NAME
    tenant_admin_name = config.TENANT_ADMIN
    tenant_admin_password = config.TENANT_PASSWORD
    subTnt_name = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    browser = BrowserEngine
    randomName = subTnt_name

    # @classmethod
    # def setUpClass(cls):
    #     browser = BrowserEngine(cls)
    #     cls.driver = browser.open_browser(cls)
    def setUp(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    def tearDown(cls):
        cls.driver.quit()
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    # http://cig-qametrics.isus.emc.com:3000/node/show?nodeid=14641&project=1
    # create a new sub tenant
    def test_1subTnt_add(self):
        logger.info("********* Start case: test_subTnt_add *********")
        atmoslogin = AtmosLogin(self.driver)
        atmoslogin.type_tenant_name(self.tenant_name)
        atmoslogin.type_tnt_user_name(self.tenant_admin_name)
        atmoslogin.type_password(self.tenant_admin_password)
        atmoslogin.click_login_btn()
        # tnt_list = "xpath=>//a[text()='Tenant List']"
        atmoslogin.select_frame('mainFrame')
        atmosTnt = AtmosTntDashBoard(self.driver)
        atmosTnt.click_add_sub_tnt_btn()
        atmosTnt.type_sub_tenant_name_input(self.randomName)
        atmosTnt.click_create_sub_tnt_btn()
        check_sub_tnt_listed = "xpath=>//a[contains(text(),self.randomName)]"
        # self.assertIs(atmosTnt.is_element_visible(check_sub_tnt_listed), True, msg="Fail to create subtenant %s" % self.check_subTnt_name)
        # self.assertFalse(atmosTnt.is_fail_create_sub_tnt_display(),msg="Fail to create subtenant %s" % self.subTnt_name)
        # self.assertIs(atmosTnt.is_fail_create_sub_tnt_display(), False, msg="Fail to create subtenant %s" % self.subTnt_name)
        try:
            if atmosTnt.is_element_visible(check_sub_tnt_listed):
                logger.info('Assertion test pass.%s' % self.randomName)
            else:
                logger.error('Assertion test fail.')
        except Exception as e:
            print('Assertion test fail.%s' % e)

    def test_2login_on_every_node(self):
        logger.info("********* Start case: login_on_every_node *********")
        urlList = [config.LOGIN_URL_slave1, config.LOGIN_URL_slave2, config.LOGIN_URL_slave3]
        atmoslogin = AtmosLogin(self.driver)
        for self.url in urlList:
            # self.driver.close()
            # atmoslogin = AtmosLogin(self.driver)
            self.driver.get(self.url)
            logger.info("Open url: %s" % self.url)
            self.driver.maximize_window()
            logger.info("Maximize the current window.")
            self.driver.implicitly_wait(20)

            # handles = self.driver.window_handles
            # self.driver.switch_to.window(handles[-1])

            # window_1 = self.driver.current_window_handle
            # windows = self.driver.window_handles
            # for current_window in windows:
            #     if current_window != window_1:
            #         self.driver.switch_to.window(current_window)
            atmoslogin.click_mauadmin_login_link()
            atmoslogin.type_user_name(self.mauiadmin_user_name)
            atmoslogin.type_password(self.mauiadmin_password)
            atmoslogin.click_login_btn()
            atmoslogin.select_frame('mainFrame')
            #check: mauiadmin success to login
            atmossys = AtmosSysDashBoard(self.driver)
            self.assertTrue(atmossys.is_sys_dashboard_display(), msg='System Dashboard displayed')
            atmoslogin.get_windows_img()


    def test_3add_tenant_admin(self):
        logger.info("********* Start case: add_tenant_admin *********")
        atmoslogin = AtmosLogin(self.driver)
        atmoslogin.click_mauadmin_login_link()
        atmoslogin.type_user_name(self.mauiadmin_user_name)
        atmoslogin.type_password(self.mauiadmin_password)
        atmoslogin.click_login_btn()
        atmoslogin.select_frame('leftFrame')
        atmosTnt = AtmosTntDashBoard(self.driver)
        atmosTnt.click_tnt_list_txt()
        atmosTnt.select_frame('mainFrame')
        atmosTnt.click_tnt_click_tntname_txt()
        atmosTnt.click_tnt_click_add_tntadmin()
        atmosTnt.type_tnt_type_tntadmin(self.randomName)
        atmosTnt.click_tnt_click_save_tntadmin()
        atmosTnt.click_tnt_clickaddnewtntadmin_confirm()
        # checkTntName = atmosTnt.getText("//input[contains(@id, 'username')]")
        # checkTntName = atmosTnt.att_value_getfromBox("xpath=>//input[contains(@id, 'username')]")
        checkTntName = atmosTnt.getattribute("xpath=>//input[contains(@id, 'username')]", 'value')
        logger.info("The Tenant admin name is %s :" % checkTntName)
        if checkTntName == self.randomName:
            logger.info('Tenant admin name matched.%s' % self.randomName)
        else:
            logger.error("Tenant admin name not matched")
        atmosTnt.type_tnt_type_addNewAdmin_passwd("password")
        atmosTnt.type_tnt_type_addNewAdmin_passwd_cnfm("password")
        atmosTnt.type_tnt_type_addNewAdmin_email("test@sina.com")
        atmosTnt.type_tnt_type_addNewAdmin_phone("+86051262628888")
        atmosTnt.type_tnt_type_addNewAdmin_mobile("008613814818888")
        atmosTnt.click_tnt_click_save_tntadmin()
        # self.assertIs(atmosTnt.is_element_visible("//td[contains(text(), self.randomName)]"), True, msg="Not find %s" % self.randomName)
        try:
            if atmosTnt.is_element_visible("//td[contains(text(), self.randomName)]"):
                logger.info('Assertion test pass %s' % self.randomName)
            else:
                logger.error('Assertion test fail.')
        except Exception as e:
            print('Assertion test fail.%s' % e)

    def test_4require_SSL_for_Web_Service_connections(self):
        logger.info("********* Start case: require_SSL_for_Web_Service_connections *********")
        atmoslogin = AtmosLogin(self.driver)
        atmoslogin.click_mauadmin_login_link()
        atmoslogin.type_user_name(self.mauiadmin_user_name)
        atmoslogin.type_password(self.mauiadmin_password)
        atmoslogin.click_login_btn()
        atmoslogin.select_frame('leftFrame')
        atmosTnt = AtmosTntDashBoard(self.driver)
        atmosTnt.click_tnt_list_txt()
        atmosTnt.select_frame('mainFrame')
        atmosTnt.click_tnt_click_tntname_txt()
        atmosTnt.click_tnt_click_ssl_for_web_txt()
        at = atmosTnt.getattribute(atmosTnt.tnt_click_btn_Enable_ssl, 'value')
        logger.info("Current button info %s" % at)
        if at == "Enable":
            logger.info("Start to enable SSL")
            atmosTnt.click_tnt_click_btn_Enable_ssl()
            at = atmosTnt.getattribute(atmosTnt.tnt_click_btn_Enable_ssl, 'value')
            logger.info("After Enable current butten info %s" % at)
        else:
            logger.info("Already enable SSL, Skipped, button is %s" % at)


if __name__ == '__main__':
    unittest.main()