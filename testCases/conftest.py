# repeatedly used codes to be placed here

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        print("Launching Chrome browser..........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        print("Launching firefox browser...........")
    else:
        driver = webdriver.Edge()
        driver.maximize_window()
        print("Launching default driver ..MS Edge.....")

    return driver


def pytest_addoption(parser):   # This method will get value from command line Interface (CLI)/hook/terminal
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):   # This will return browser value to set up method
    return request.config.getoption("--browser")

# To generate pytest html report
# Hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'E-commerce'
    config._metadata['Tested by'] = 'Vishwa'

# Hook for delete/modify environment info to HTML file
@pytest.mark.optioalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


