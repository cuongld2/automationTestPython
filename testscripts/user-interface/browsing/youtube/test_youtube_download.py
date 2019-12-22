import time
from pytest_testrail.plugin import pytestrail

from models.page_object.actions.browsing.youtube_actions import YoutubePageActions, YoutubeDownloaderActions
from utilities.constants import Links

youtube_page_actions = YoutubePageActions()
youtube_downloader_actions = YoutubeDownloaderActions()


@pytestrail.case('C1')
def test_youtube_download_regular_file(firefox_browse_youtube):
    firefox_browse_youtube.get(Links.YOUTUBE_VIDEO_LINK)
    youtube_page_actions.click_download_as_btn(firefox_browse_youtube)
    assert '360p' in youtube_downloader_actions.get_text_low_quality_option(firefox_browse_youtube)


@pytestrail.case('C2')
def test_youtube_download_high_quality_file(firefox_browse_youtube):
    firefox_browse_youtube.get(Links.YOUTUBE_VIDEO_LINK)
    youtube_page_actions.click_download_as_btn(firefox_browse_youtube)
    assert '720p' in youtube_downloader_actions.get_text_higher_quality_option(firefox_browse_youtube)



