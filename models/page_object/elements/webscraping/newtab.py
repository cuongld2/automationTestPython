
from selenium.webdriver.support import expected_conditions as ec

from models.page_object.elements.base_page_elements import BasePageElements
from models.page_object.locators.webscraping.newtab import NewTabSearchLocators, NewTabIconSitesLocators, \
    NewTabZenLocators


class NewTabSearchElement(BasePageElements):

    def find_search_string_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabSearchLocators.SEARCH_STRING))

    def find_search_button_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabSearchLocators.SEARCH_BUTTON))


class NewTabIconSitesElement(BasePageElements):
    def find_all_most_visited_sites(self, driver):
        self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabIconSitesLocators.MOST_VISITED_TITLES))
        return driver.find_elements_by_css_selector(NewTabIconSitesLocators.MOST_VISITED_TITLES_CSS_SELECTOR)

    def find_all_most_paid_sites(self, driver):
        self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabIconSitesLocators.MOST_VISITED_ICONS))
        return driver.find_elements_by_css_selector(NewTabIconSitesLocators.MOST_VISITED_ICONS_CSS_SELECTOR)


class NewTabZenElements(BasePageElements):
    def find_any_zen_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabZenLocators.ZEN_NEWS_ITEM))

    def find_all_current_zen_elements(self, driver):
        self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabZenLocators.ZEN_NEWS_ITEM))
        return driver.find_elements_by_css_selector(NewTabZenLocators.ZEN_NEWS_ITEM_CSS_SELECTOR)

    def find_all_current_zen_except_ads_elements(self, driver):
        self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabZenLocators
                                                                           .ZEN_NEWS_NOT_CONTAINS_ADS_ITEM))
        return driver.find_elements_by_css_selector(NewTabZenLocators.ZEN_NEWS_NOT_CONTAINS_ADS_ITEM_CSS_SELECTOR)
















