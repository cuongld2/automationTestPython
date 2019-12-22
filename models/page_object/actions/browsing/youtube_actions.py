from models.page_object.actions.base_page_actions import BasePageActions
from models.page_object.elements.browsing.youtube_elements import YoutubePageElements, YoutubeDownloaderElements


class YoutubePageActions(BasePageActions):
    youtube_page_elements = YoutubePageElements()

    def click_download_as_btn(self, driver):
        self.youtube_page_elements.find_download_as_btn(driver).click()


class YoutubeDownloaderActions(BasePageActions):
    youtube_downloader_elements = YoutubeDownloaderElements()

    def click_download_low_quality_option(self, driver):
        self.youtube_downloader_elements.find_download_low_quality_option(driver).click()

    def get_text_low_quality_option(self, driver):
        return self.youtube_downloader_elements.find_download_low_quality_option(driver).text

    def get_text_higher_quality_option(self, driver):
        return self.youtube_downloader_elements.find_download_higher_quality_option(driver).text










