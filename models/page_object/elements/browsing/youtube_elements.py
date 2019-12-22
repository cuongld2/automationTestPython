from models.page_object.elements.base_page_elements import BasePageElements
from models.page_object.locators.browsing.youtube_locators import YoutubePageLocators, YoutubeDownloaderLocators
from selenium.webdriver.support import expected_conditions as ec


class YoutubePageElements(BasePageElements):
    def find_download_as_btn(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(YoutubePageLocators.DOWNLOAD_AS_BUTTON))


class YoutubeDownloaderElements(BasePageElements):
    def find_download_low_quality_option(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(YoutubeDownloaderLocators.DOWNLOAD_QUALITY_OPTIONS))

    def find_download_higher_quality_option(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(YoutubeDownloaderLocators.DOWNLOAD_QUALITy_HIGHER_OPTIONS))
