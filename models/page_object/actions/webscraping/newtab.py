from selenium.webdriver import ActionChains

from models.page_object.actions.base_page_actions import BasePageActions
from models.page_object.elements.webscraping.newtab import NewTabSearchElement, NewTabIconSitesElement, \
    NewTabZenElements


class NewTabSearchPageObject(BasePageActions):

    new_tab_search_element = NewTabSearchElement()

    def get_css_value_search_string_element(self, driver, css_property):
        return self.new_tab_search_element.find_search_string_element(driver).value_of_css_property(css_property)

    def send_key_string_to_search_string_element(self, driver, *text):
        return self.new_tab_search_element.find_search_string_element(driver).send_keys(text)

    def get_css_value_search_button_element(self, driver, css_property):
        return self.new_tab_search_element.find_search_button_element(driver).value_of_css_property(css_property)

    def click_search_button_element(self, driver):
        return self.new_tab_search_element.find_search_button_element(driver).click()


class NewTabIconSitesPageObject(BasePageActions):

    new_tab_icon_site_elem = NewTabIconSitesElement()

    def get_total_number_most_visited_sites(self, driver):
        return len(self.new_tab_icon_site_elem.find_all_most_visited_sites(driver))

    def get_total_number_most_paid_sites(self, driver):
        return len(self.new_tab_icon_site_elem.find_all_most_paid_sites(driver))

    def get_attribute_any_most_visited_site_element(self, driver, nth_element, attribute_name):
        return self.new_tab_icon_site_elem.find_all_most_visited_sites(driver)[nth_element].get_attribute(attribute_name)

    def get_attribute_any_most_visited_paid_element(self, driver, nth_element, attribute_name):
        return self.new_tab_icon_site_elem.find_all_most_paid_sites(driver)[nth_element].get_attribute(attribute_name)

    def click_any_most_visited_site_element(self, driver, nth_element):
        self.new_tab_icon_site_elem.find_all_most_visited_sites(driver)[nth_element].click()

    def click_any_most_visited_paid_element(self, driver, nth_element):
        self.new_tab_icon_site_elem.find_all_most_paid_sites(driver)[nth_element].click()


class NewTabZenPageObject(BasePageActions):
    new_tab_zen_elem = NewTabZenElements()

    def click_on_any_zen_element(self, driver):
        driver.execute_script('arguments[0].click();', self.new_tab_zen_elem.find_any_zen_element(driver))

    def move_to_any_zen_element(self, driver):
        actions = ActionChains(driver)
        actions.move_to_element(self.new_tab_zen_elem.find_any_zen_element(driver)).perform()

    def get_attribute_any_zen_element(self, driver, attribute_name):
        return self.new_tab_zen_elem.find_any_zen_element(driver).get_attribute(attribute_name)

    def get_number_of_all_current_zen_elements(self, driver):
        return len(self.new_tab_zen_elem.find_all_current_zen_elements(driver))

    def get_attribute_all_zen_elements(self, driver, attribute_name):
        attribute_value = []
        for element in self.new_tab_zen_elem.find_all_current_zen_elements(driver):
            attribute_value.append(element.get_attribute(attribute_name))
        return attribute_value

    def get_attribute_all_zen_except_ads_elements(self, driver, attribute_name):
        attribute_value = []
        for element in self.new_tab_zen_elem.find_all_current_zen_except_ads_elements(driver):
            attribute_value.append(element.get_attribute(attribute_name))
        return attribute_value




