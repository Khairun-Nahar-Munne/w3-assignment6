from selenium.webdriver.common.by import By
from config.config import Config
from utils.excel_reporter import ExcelReporter
from utils.web_utils import wait_for_element
from drivers.chrome_driver import get_chrome_driver
from urllib.parse import urljoin, urlparse


def is_internal_link(link, base_url):
    """
    Check if a link is internal.
    
    :param link: URL to check
    :param base_url: Base URL of the website
    :return: True if internal, False otherwise
    """
    if not link or link.startswith(("mailto:", "javascript:")):
        return False
    parsed_link = urlparse(link)
    return not parsed_link.netloc or parsed_link.netloc == urlparse(base_url).netloc


def run_h1_tag_test(driver):
    """
    Test for H1 tag existence on all internal links of the page, starting with the homepage.
    
    :param driver: Selenium WebDriver
    :return: List of test results
    """
    test_results = []
    base_url = Config.TEST_SITE_URL

    try:
        # First, check the homepage for H1 tag existence
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
        
        # Get all links on the page
        links = driver.find_elements(By.TAG_NAME, 'a')
        all_links = set(link.get_attribute('href') for link in links if link.get_attribute('href'))
        unique_internal_links = {urljoin(base_url, link) for link in all_links if is_internal_link(link, base_url)}

        print(f"Found {len(unique_internal_links)} unique internal links to check.")

        for link in unique_internal_links:
            try:
                driver.get(link)
                wait_for_element(driver, By.TAG_NAME, 'h1')

                # Find H1 tags
                h1_elements = driver.find_elements(By.TAG_NAME, 'h1')
                
                result = {
                    'page_url': link,
                    'testcase': 'H1 Tag Existence',
                    'passed': len(h1_elements) > 0,
                    'comments': f'Found {len(h1_elements)} H1 tags' if h1_elements else 'No H1 tag found'
                }

                test_results.append(result)

            except Exception as e:
                test_results.append({
                    'page_url': link,
                    'testcase': 'H1 Tag Existence',
                    'passed': False,
                    'comments': f'Error while accessing link: {str(e)}'
                })

        # Generate a consolidated report
        ExcelReporter.generate_report(test_results, 'h1_tag_all_links_test')
        print("Test completed. Results saved.")
        
    except Exception as e:
        print(f"Error occurred during the test: {str(e)}")

    return test_results


if __name__ == "__main__":
    driver = get_chrome_driver()
    
    try:
        run_h1_tag_test(driver)
    finally:
        driver.quit()
