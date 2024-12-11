from selenium.webdriver.common.by import By
from config.config import Config
from utils.excel_reporter import ExcelReporter
from utils.web_utils import wait_for_element
from drivers.chrome_driver import get_chrome_driver


def run_h1_tag_test(driver):
    """
    Test for H1 tag existence only on the homepage.
    
    :param driver: Selenium WebDriver
    :return: List of test results
    """
    test_results = []
    base_url = Config.TEST_SITE_URL

    try:
        # First, check the homepage for H1 tag existence
        print("Starting h1 tag test...")
        driver.get(base_url)
        wait_for_element(driver, By.TAG_NAME, 'h1')

        # Find H1 tags on the homepage
        h1_elements = driver.find_elements(By.TAG_NAME, 'h1')
        test_results.append({
            'page_url': base_url,
            'testcase': 'H1 Tag Existence',
            'passed': len(h1_elements) > 0,
            'comments': f'Found {len(h1_elements)} H1 tags' if h1_elements else 'No H1 tag found'
        })

        # Generate a consolidated report
        ExcelReporter.generate_report(test_results, 'h1_tag_homepage_test')
        print("h1 tag test completed. Results saved.")
        
    except Exception as e:
        print(f"Error occurred during the test: {str(e)}")

    return test_results


if __name__ == "__main__":
    driver = get_chrome_driver()
    
    try:
        run_h1_tag_test(driver)
    finally:
        driver.quit()
