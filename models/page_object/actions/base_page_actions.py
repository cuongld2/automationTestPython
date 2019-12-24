

class BasePageActions:
    def scroll_to_with_scroll_height(self, driver):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')








