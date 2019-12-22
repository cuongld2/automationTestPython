from datetime import datetime

import pytest
from selenium.webdriver import Firefox, FirefoxProfile

firefox_system_profile = r'/home/cuongld/.mozilla/firefox/jxhdfsma.donald'
browser = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report right before close webdriver.
        :param request:
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        hasattr(report, 'wasxfail')
        timestamp = datetime.now().strftime('%H-%M-%S.%f')[:-3]
        filename = timestamp + ".png"
        if browser is not None and ('winapp' not in item.name):
            try:
                _capture_screenshot(filename)
            except:
                print("Cannot capture screenshot!!!")

        # if file_name:
        html = '<div><img src="screenshots/%s" style="width:600px;height:228px;" ' \
               'onclick="window.open(this.src)" align="right"/></div>' % filename
        extra.append(pytest_html.extras.html(html))
    report.extra = extra


def _capture_screenshot(filename):
    current_dir = get_current_dir()[0]
    browser.save_screenshot(current_dir + "/resources/screenshots/" + filename)


def get_current_dir():
    import os
    before_split = os.getcwd()
    return before_split.split('\\testscripts\\')


@pytest.fixture(scope='session')
def firefox_browse_youtube():
    global browser
    browser_profile = FirefoxProfile(firefox_system_profile)
    browser = Firefox(executable_path=r'/home/cuongld/webdriver/geckodriver', firefox_profile=browser_profile)
    browser.install_addon(firefox_system_profile+'/extensions/{b9acf540-acba-11e1-8ccb-001fd0e08bd4}.xpi')
    browser.maximize_window()
    list_window_handles = browser.window_handles
    browser.switch_to.window(list_window_handles[0])
    yield browser
    browser.quit()








