# utils/web_utils.py
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_url_status(url):
    """
    Check URL status code
    
    :param url: URL to check
    :return: HTTP status code
    """
    try:
        response = requests.head(url, timeout=10)
        return response.status_code
    except requests.RequestException:
        return 404

def wait_for_element(driver, selector, timeout=10):
    """
    Wait for an element to be present
    
    :param driver: Selenium WebDriver
    :param selector: CSS selector
    :param timeout: Maximum wait time
    :return: WebElement if found
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        return element
    except:
        return None