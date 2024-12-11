from selenium import webdriver
from selenium.webdriver.common.by import By
from config.config import Config
from utils.web_utils import check_url_status
from utils.excel_reporter import ExcelReporter
from drivers.chrome_driver import get_chrome_driver

def run_url_status_test(driver):
    """
    Test URL status codes for unique links on the homepage.
    Save only broken/missing URLs (404) in the report. 
    Show "All Pass" if no 404s are found.
    
    :param driver: Selenium WebDriver
    :return: List of test results
    """
    test_results = []
    unique_urls = set()  # Set to store unique URLs
    broken_urls = []  # List to store only broken URLs
    
    try:
        # Open the base URL (homepage)
        print("Starting url status test...")
        driver.get(Config.TEST_SITE_URL)
        
        # Find all links on the page
        links = driver.find_elements(By.TAG_NAME, 'a')
        
        for link in links:
            href = link.get_attribute('href')
            if href and href.startswith('http'):
                unique_urls.add(href)  # Add URL to the set (ensures uniqueness)
        
        # Test each unique URL
        for url in unique_urls:
            status_code = check_url_status(url)
            
            # Check if the URL is broken (status code is 404)
            if status_code == 404:
                result = {
                    'property_page_url': driver.current_url,
                    'testcase': 'URL Status Check',
                    'passed': False,
                    'comments': f'Broken URL: {url} '
                }
                broken_urls.append(result)  # Collect only broken URLs
            
        # Save only broken URLs to the report
        if broken_urls:
            ExcelReporter.generate_report(broken_urls, 'broken_url_status_test')
            print(f"Broken URLs found: {len(broken_urls)}. Results saved.")
        else:
            # If no broken URLs, create a simple "All Pass" report
            test_results.append({
                'property_page_url': driver.current_url,
                'testcase': 'URL Status Check',
                'passed': True,
                'comments': 'All Pass. No 404 errors found.'
            })
            ExcelReporter.generate_report(test_results, 'broken_url_status_test')
            print("All Pass. No broken URLs found.")
        
    except Exception as e:
        # Handle exceptions and save error details
        result = {
            'page_url': Config.TEST_SITE_URL,
            'testcase': 'URL Status Check',
            'passed': False,
            'comments': f'Error: {str(e)}'
        }
        test_results.append(result)
        ExcelReporter.generate_report(test_results, 'broken_url_status_test')
        print("An error occurred. Results saved.")
    
    return broken_urls

if __name__ == "__main__":
    # Initialize WebDriver (make sure ChromeDriver is installed and in PATH)
    driver = get_chrome_driver()
    
    try:
        run_url_status_test(driver)
    finally:
        driver.quit()
