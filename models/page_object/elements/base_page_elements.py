from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class BasePageElements(object):
    @staticmethod
    def select_shadow_element_by_css_selector(browser, selector):
        element = browser.execute_script('return arguments[0].shadowRoot', selector)
        return element

    def find_shadow_element(self, driver, *string_text):
        wait = WebDriverWait(driver, 20)
        i = 0
        root = wait.until(ec.presence_of_element_located((By.TAG_NAME, string_text[i])))
        # root = driver.find_element_by_tag_name(string_text[i])
        while len(string_text) > (i + 1):
            i = i + 1
            shadow_root = self.select_shadow_element_by_css_selector(driver, root)
            root = shadow_root.find_element_by_css_selector(string_text[i])
        return root

    @staticmethod
    def wait_for_element(driver, timeout=10):
        return WebDriverWait(driver, timeout)

    def find_element_if_exist(self, driver, locator):
        element = None
        try:
            element = self.wait_for_element(driver).until(ec.presence_of_element_located(locator))
        except TimeoutException as e:
            print(e.stacktrace)
        return element


