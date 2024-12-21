from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_headers import Headers
import logging

class Manager:
    def __init__(self):
        self.driver = self._init_driver()
        self.modules = []
    
    def add_modules(self, modules):
        self.modules.extend(modules)
    
    def run(self):
        for module in self.modules:
            res = module.run(self.driver)
            if res != 0:
                logging.error(module.name + " has returned an error: " + module.errorMsg)
    
    def quit(self):
        self.driver.quit()

    def _init_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")

        # Headers tell site that chrome is running in 'headless' mode.. fake_headers library fixes that
        # https://stackoverflow.com/questions/64311719/selenium-unable-to-locate-element-only-when-using-headless-chrome-python
        header = Headers(
            browser="chrome",  # Generate only Chrome UA
            os="win",  # Generate only Windows platform
            headers=False # generate misc headers
        )
        customUserAgent = header.generate()['User-Agent']

        chrome_options.add_argument(f"user-agent={customUserAgent}")

        return webdriver.Chrome(options=chrome_options)