# coding=utf-8
"""
@author:     Rain Shi
@date:       3/25/2018
"""
import time
import os.path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from lib.logger import Logger
from config import config
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# create a logger instance
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    define a base page class, store common element/page action, all page should inherit from this class
    """

    def __init__(self, driver):
        self.driver = driver

    # quit browser and end testing
    def quit_browser(self):
        self.driver.quit()

    # browser forward
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # browser back
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # implicitly wait
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # display wait,wait until element display, time out 15 sec
    def wait_unit_el_present(self, xpath):
        wait = WebDriverWait(self.driver, 15)
        element = ''
        if 'xpath=>' in xpath:
            xpath = xpath.split('=>')[1]
        locator = (By.XPATH, xpath)
        try:
            element = wait.until(EC.presence_of_element_located(locator))
        except Exception:
            logger.error("Failed to wait element!")
            self.get_windows_img()
        return element

    # close page
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    # save screenshot
    def get_windows_img(self):
        # type: () -> object
        """
        save the screenshot to project_path+'/screenshots/'
        """
        file_path = config.PROJECT_PATH + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    # element locator
    def find_element(self, selector):
        """
         selector split by '=>'
         example: submit_btn = "id=>su"
                  login_lnk = "xpath => //*[@id='u1']/a[7]"
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()   # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful "
                                "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    # input inputbox
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    def getText(self, selector):
        # type: (object) -> object
        element = self.find_element(selector)
        v1 = element.text
        return v1

    def getattribute(self, selector, attribute):
        el = self.find_element(selector)
        try:
            at = el.get_attribute(attribute)
        except NameError as e:
            logger.error("Failed to get attribute: %s for the element with %s" % (attribute, e))
        return at

    # clear inputbox
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # click el
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # get page title
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    # switch frame
    def select_frame(self, frame):
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(frame)
        logger.info("Switch to frame: %s" % frame)

    # swich to window
    def switch_towindow(self, window_name):
        # self.driver.switch_to_window(window_name)
        self.driver.switch_to.window(window_name)

    # switch to frame
    def switch_toframe(self, frame_name):
        # self.driver.switch_to_frame(frame_name)
        self.driver.switch_to.frame(frame_name)
        logger.info("Switch to frame: %s" % frame_name)
    #switch to default page
    def switch_todefault(self):
        # self.driver.switch_to_default_content()
        self.driver.switch_to.default_content()

    # switch to alert window
    def switch_toalert(self):
        # self.driver.switch_to_alert()
        self.driver.switch_to.alert()

    def is_element_visible(self, xpath):
        driver = self.driver
        if 'xpath=>' in xpath:
            xpath = xpath.split('=>')[1]
        locator = (By.XPATH, xpath)
        try:
            the_element = EC.visibility_of_element_located(locator)
            assert the_element(driver)
            flag = True
        except:
            flag = False
        return flag

    def accept_alert(self):
        # alert = self.driver.switch_to_alert()
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert().dismiss()

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)