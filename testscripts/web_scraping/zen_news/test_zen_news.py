import time

from delayed_assert import assert_expectations, expect
from pytest_testrail.plugin import pytestrail
from models.page_object.actions.webscraping.newtab import NewTabZenPageObject
from utilities.constants import Links
from utilities.data_structures import check_if_duplicates_list
from utilities.date_time_utils import how_many_days_til_now
from utilities.web_scraping_utils import WebScrapingTime

new_tab_zen_page_object = NewTabZenPageObject()


@pytestrail.case('C5')
def test_check_no_duplicate_news_on_zen(chrome_browser):
    chrome_browser.get(Links.NEW_TAB_LINK)
    for x in range(0, 20):
        new_tab_zen_page_object.scroll_to_with_scroll_height(chrome_browser)
        time.sleep(2)
    url_list = new_tab_zen_page_object.get_attribute_all_zen_elements(chrome_browser, 'href')
    assert check_if_duplicates_list(url_list)


@pytestrail.case('C6')
def test_no_old_news_on_zen(chrome_browser):
    import requests
    web_scraping_time = WebScrapingTime()
    chrome_browser.get(Links.NEW_TAB_LINK)
    for x in range(0, 10):
        new_tab_zen_page_object.scroll_to_with_scroll_height(chrome_browser)
        time.sleep(2)
    url_list = new_tab_zen_page_object.get_attribute_all_zen_except_ads_elements(chrome_browser, 'href')
    print(f'Total of the sites collected is : {len(url_list)}')
    for url in url_list:
        response = None
        try:
            response = requests.get(url)
        except ConnectionError as e:
            print(e)
        expect(response is not None, f'Assert response not None for site {url}')
        expect(response.status_code == 200, f'Assert response status code for site {url}')
        published_time = web_scraping_time.get_published_time_of_web_page(response.text)
        if published_time is not None:
            expect(how_many_days_til_now(published_time) <= 30, f'Verify date of page {url}')
        # else:
            # print(f'Url of the site which cannot get published date is : {url}')
    assert_expectations()




