import ssl

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller


def before_scenario(context, scenario):
    ssl._create_default_https_context = ssl._create_unverified_context
    chromedriver_autoinstaller.install()
    version = chromedriver_autoinstaller.get_chrome_version()
    print(f"Chrome version: {version}")
    options = Options()
    options.add_argument("window-size=1920,1080")
    context.driver = webdriver.Chrome(options=options)


def after_scenario(context, scenario):
    context.driver.quit()
