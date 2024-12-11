from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_chrome_driver():
    """
    Setup and return Chrome WebDriver with standard options
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.add_argument("--headless=new")  # New headless mode
    #chrome_options.add_argument("--window-size=1920,1080")
    #chrome_options.add_argument("--disable-gpu")
    # if you use windows
    #chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")


    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver
