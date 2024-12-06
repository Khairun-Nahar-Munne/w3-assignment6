from selenium import webdriver
from selenium.webdriver.common.by import By
from config.config import Config
from utils.web_utils import check_url_status
from utils.excel_reporter import ExcelReporter
from drivers.chrome_driver import get_chrome_driver

def run_url_status_test(driver):
    """
    Test URL status codes for all links on the homepage.
    
    :param driver: Selenium WebDriver
    :return: List of test results
    """
    test_results = []
    
    try:
        # Open the base URL (homepage)
        driver.get(Config.TEST_SITE_URL)
        
        # Find all links on the page
        links = driver.find_elements(By.TAG_NAME, 'a')
        
        for link in links:
            href = link.get_attribute('href')
            if href and href.startswith('http'):
                status_code = check_url_status(href)
                
                # Check for 404 errors
                passed = status_code < 400
                if status_code == 404:
                    passed = False
                
                result = {
                    'property_page_url': driver.current_url,
                    'testcase': 'URL Status Check',
                    'available_url': href,
                    'passed': passed,
                    'comments': f'Status Code: {status_code}'
                }
                
                test_results.append(result)
        
        # Generate report with a different sheet name
        ExcelReporter.generate_report(test_results, 'url_status_test')
        
    except Exception as e:
        result = {
            'page_url': Config.TEST_SITE_URL,
            'testcase': 'URL Status Check',
            'passed': False,
            'comments': f'Error: {str(e)}'
        }
        test_results.append(result)
    
    return test_results

if __name__ == "__main__":
    # Initialize WebDriver (make sure ChromeDriver is installed and in PATH)
    driver = get_chrome_driver()
    
    try:
        run_url_status_test(driver)
    finally:
        driver.quit()
