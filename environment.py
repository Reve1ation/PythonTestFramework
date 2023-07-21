import ssl
import yaml

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):
    ssl._create_default_https_context = ssl._create_unverified_context
    options = Options()
    options.add_argument("window-size=1920,1080")
    ChromeDriverManager().install()
    context.driver = webdriver.Chrome(options=options)
    with open('config/ebay_prod.yaml', 'r') as f:
        context.user_data = yaml.safe_load(f)


def after_scenario(context, scenario):
    context.driver.close()
    context.driver.quit()
