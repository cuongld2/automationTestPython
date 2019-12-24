from selenium.webdriver.common.by import By


class NewTabSearchLocators:
    SEARCH_STRING = (By.ID, 'search-string')
    SEARCH_BUTTON = (By.ID, 'search-button')


class NewTabIconSitesLocators:
    MOST_VISITED_TITLES_CSS_SELECTOR = 'a[data-ga-label*="tile"]'
    MOST_VISITED_ICONS_CSS_SELECTOR = 'a[data-ga-label*="icon"]'
    MOST_VISITED_TITLES = (By.CSS_SELECTOR, MOST_VISITED_TITLES_CSS_SELECTOR)
    MOST_VISITED_ICONS = (By.CSS_SELECTOR, MOST_VISITED_ICONS_CSS_SELECTOR)


class NewTabZenLocators:
    ZEN_NEWS_ITEM_CSS_SELECTOR = 'div[class] > a:not(.qc-link)[href]:not(.context-content)'
    ZEN_NEWS_ITEM = (By.CSS_SELECTOR, ZEN_NEWS_ITEM_CSS_SELECTOR)
    ZEN_NEWS_NOT_CONTAINS_ADS_ITEM_CSS_SELECTOR = 'div[class] > a:not(.qc-link)[href]:not(.context-content)' \
                                                  ':not(.zen-ads__context):not([href*="utm"])' \
                                                  ':not([data-click-url*="click"])'
    ZEN_NEWS_NOT_CONTAINS_ADS_ITEM = (By.CSS_SELECTOR, ZEN_NEWS_NOT_CONTAINS_ADS_ITEM_CSS_SELECTOR)







