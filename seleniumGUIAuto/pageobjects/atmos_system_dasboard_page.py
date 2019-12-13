# coding=utf-8

from lib.basepage import BasePage

class AtmosSysDashBoard(BasePage):
    sys_dashboard_txt = "xpath=>//span[contains(text(),'System Dashboard')]"

    def is_sys_dashboard_display(self):
        is_display = self.is_element_visible(self.sys_dashboard_txt)
        return is_display

