from selenium.webdriver.common.by import By


class YoutubePageLocators:
    DOWNLOAD_AS_BUTTON = (By.ID, 'eytd_btn')


class YoutubeDownloaderLocators:
    DOWNLOAD_QUALITY_OPTIONS = (By.CSS_SELECTOR, "div[id*='download-youtube-video-fmt-eytd']")
    DOWNLOAD_QUALITy_HIGHER_OPTIONS = (By.CSS_SELECTOR, "div[id*='download-youtube-video-fmt-eytd'][loop='1']")











