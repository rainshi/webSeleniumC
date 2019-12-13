# -*- coding:utf-8 -*-
"""
@author:     Rain Shi
@date:       3/25/2018
"""
import os.path
import sys
import re
from selenium import webdriver
from lib.logger import Logger
from config import config

logger = Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):

    dir = config.PROJECT_PATH
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'
    ff_driver_path = dir + '/tools/geckodriver.exe'
    browser = config.BROWSER

    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.py file, return the driver
    def open_browser(self, driver):
        browser = config.BROWSER
        logger.info("You had select %s browser." % browser)
        url = config.LOGIN_URL
        logger.info("The test server url is: %s" % url)
        if re.match(r'(i|I)(e|E)', browser):
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")
        elif re.match(r'(c|C)(h|H)(r|R)(o|O)(m|M)(e|E)', browser):
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            # driver = webdriver.Chrome(self.chrome_driver_path)
            driver = webdriver.Chrome(self.chrome_driver_path, chrome_options=options)
            logger.info("Starting Chrome browser.")
        elif re.match(r'(f|F)(i|I)(r|R)(e|E)(f|F)(o|O)(x|X)', browser):
            driver = webdriver.Firefox(self.ff_driver_path)
            logger.info("Starting firefox browser.")
        else:
            print "Currently not support this browser {}".format(browser)
            sys.exit(-1)

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(20)
        logger.info("Set implicitly wait 20 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()
