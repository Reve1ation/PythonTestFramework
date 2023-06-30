from features.pages.page import Page


class GoogleSearchPage(Page):
    URL = 'https://www.google.com'

    def __init__(self, context):
        super().__init__(context)

    @property
    def search_input(self):
        return self.find_element(name='q')

    @property
    def search_results(self):
        return self.find_elements(css='.g')

    def load(self):
        self.logger.info(self.URL)
        self.driver.get(self.URL)
