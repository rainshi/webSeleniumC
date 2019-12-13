# coding=utf-8
"""
@author:     Rain Shi
@date:       3/25/2018
"""
from lib.basepage import BasePage


class AtmosLogin(BasePage):
    #maui admin login
    maui_admin_link = "xpath=>//span[contains(text(),'Login as Security')]"
    user_name_input = "xpath=>//input[@id='username']"
    password_input = "xpath=>//input[@name='password']"
    login_btn = "xpath=>//span[text()='Login']"
    #tenant admin login
    tenant_admin_link = "xpath=>//span[contains(text(),'Login as TenantAdmin')]"
    tenant_name_input = "xpath=>//input[@id='tenant_name']"
    tnt_user_name_input = "xpath=>//input[@name='username']"

    def click_mauadmin_login_link(self):
        # type: () -> object
        self.click(self.maui_admin_link)

    def click_tenant_login_link(self):
        self.click(self.tenant_admin_link)

    def type_user_name(self, text):
        self.type(self.user_name_input, text)

    def type_tnt_user_name(self, text):
        self.type(self.tnt_user_name_input, text)

    def type_password(self, text):
        self.type(self.password_input, text)

    def type_tenant_name(self, text):
        self.type(self.tenant_name_input, text)

    def click_login_btn(self):
        self.click(self.login_btn)