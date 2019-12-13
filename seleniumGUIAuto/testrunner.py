# coding=utf-8
"""
@author:     Amy Jiang
@date:       3/25/2018
"""

import unittest
import time
from lib import HTMLTestRunner
from config import config

# config report output path
report_path = config.PROJECT_PATH + '/reports/'

# get sys time
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# set report name
HtmlFile = report_path + now + "HTMLAtmosGUITestReport.html"

# create suite，add all cases of folder testcases to testsuit
testDir = config.PROJECT_PATH + "/testcases"
suite = unittest.TestLoader().discover(testDir,"*.py")

if __name__ =='__main__':
    # # run test by HTMLTestRunner and generate HTML report
    with open(HtmlFile, 'w') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title=u'Atmos GUI Testing Result：')
        runner.run(suite)