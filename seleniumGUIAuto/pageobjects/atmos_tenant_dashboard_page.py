
from lib.basepage import BasePage


class AtmosTntDashBoard(BasePage):
    tnt_dashboard_txt = "xpath=>//span[contains(text(),'Tenant Dashboard')]"
    tnt_click_tntname_txt = "xpath=>//a[contains(@href, 'maui_admin/tenant_info')]"
    tnt_list_txt = "xpath=>//a[contains(text(), 'Tenant List')]"
    tnt_click_ssl_for_web_txt = "xpath=>//a[contains(text(), 'Require SSL for Web Service connections')]"
    # tnt_click_btn_Enable_ssl = "xpath=>//input[contains(@value, 'Enable')]"
    tnt_click_btn_Enable_ssl = "xpath=>//input[contains(@onclick, '/maui_admin/submit_configure_ws_ssl')]"
    tnt_click_add_tntadmin = "xpath=>//input[contains(@onclick, 'operation=add&tenant_name')]"
    tnt_type_tntadmin = "xpath=>//input[contains(@id, 'username')]"
    tnt_click_save_tntadmin = "xpath=>//input[contains(@id, 'save_button')]"
    tnt_clickaddnewtntadmin_confirm = "xpath=>//span[@class='confirmation_text_button' and text()='Add']"
    add_sub_tnt_btn = "xpath=>//input[contains(@onclick, 'prepare_adding_subtenant')]"
    sub_tenant_name_input = "xpath=>//input[@id='sub_tenant_name']"
    create_sub_tnt_btn = "xpath=>//input[@id='add_tenant']"
    fail_create_sub_tnt = "xpath=>//p[contains(text(), 'Error: Failed to initialize subtenant.')]"
    value_getfromBox = "xpath=>//input[contains(@id, 'username')]"
    tnt_type_addNewAdmin_username = "xpath=>//input[@id='username']"
    tnt_type_addNewAdmin_passwd = "xpath=>//input[@id='passwd']"
    tnt_type_addNewAdmin_passwd_cnfm = "xpath=>//input[@id='passwd_cnfm']"
    tnt_type_addNewAdmin_email = "xpath=>//input[@id='email']"
    tnt_type_addNewAdmin_mobile = "xpath=>//input[@id='mobile']"
    tnt_type_addNewAdmin_phone = "xpath=>//input[@id='phone']"

    def is_tnt_dashboard_display(self):
        is_display = self.is_element_visible(self.tnt_dashboard_txt)
        return is_display

    def click_add_sub_tnt_btn(self):
        self.wait_unit_el_present(self.add_sub_tnt_btn)
        self.click(self.add_sub_tnt_btn)

    def click_tnt_click_ssl_for_web_txt(self):
        self.click(self.tnt_click_ssl_for_web_txt)

    def click_tnt_click_btn_Enable_ssl(self):
        self.click(self.tnt_click_btn_Enable_ssl)

    def type_sub_tenant_name_input(self, text):
        self.type(self.sub_tenant_name_input, text)

    def type_tnt_type_tntadmin(self, text):
        self.type(self.tnt_type_tntadmin, text)

    def type_tnt_type_addNewAdmin_passwd(self, text):
        self.type(self.tnt_type_addNewAdmin_passwd, text)

    def type_tnt_type_addNewAdmin_passwd_cnfm(self, text):
        self.type(self.tnt_type_addNewAdmin_passwd_cnfm, text)

    def type_tnt_type_addNewAdmin_email(self, text):
        self.type(self.tnt_type_addNewAdmin_email, text)

    def type_tnt_type_addNewAdmin_mobile(self, text):
        self.type(self.tnt_type_addNewAdmin_mobile, text)

    def type_tnt_type_addNewAdmin_phone(self, text):
        self.type(self.tnt_type_addNewAdmin_phone, text)

    def click_create_sub_tnt_btn(self):
        self.click(self.create_sub_tnt_btn)

    def click_tnt_list_txt(self):
        self.click(self.tnt_list_txt)

    def click_tnt_click_tntname_txt(self):
        self.click(self.tnt_click_tntname_txt)

    def click_tnt_click_add_tntadmin(self):
        self.click(self.tnt_click_add_tntadmin)

    def click_tnt_click_save_tntadmin(self):
        self.click(self.tnt_click_save_tntadmin)

    def click_tnt_clickaddnewtntadmin_confirm(self):
        self.click(self.tnt_clickaddnewtntadmin_confirm)

    def is_fail_create_sub_tnt_display(self):
        is_display = self.is_element_visible(self.fail_create_sub_tnt)
        return is_display