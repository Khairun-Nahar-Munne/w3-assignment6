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

def check_html_tag_sequence(tags):
    """
    Check if the HTML tag sequence from H1 to H6 is in the correct order.
    
    :param tags: List of HTML tag elements (e.g., H1, H2, etc.)
    :return: True if sequence is correct, False if any tag is missing or out of order.
    """
    expected_sequence = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    tag_sequence = [tag.lower() for tag in tags]  # Get the lowercase representation of tag names
    last_tag = 0  # To ensure that the sequence is not broken
    
    for tag in tag_sequence:
        if expected_sequence.index(tag) < last_tag:
            return False  # The sequence is broken
        last_tag = expected_sequence.index(tag)
    
    return True

def run_html_tag_sequence_test(driver):
    """
    Test for HTML tag sequence (H1-H6) existence and order on all internal links of the page.
    
    :param driver: Selenium WebDriver
    :return: List of test results
    """
    test_results = []
    base_url = Config.TEST_SITE_URL

    try:
        # First, check the homepage for H1-H6 tag sequence
        driver.get(base_url)
        wait_for_element(driver, By.TAG_NAME, 'h1')

        # Get all heading tags from H1 to H6
        heading_tags = driver.find_elements(By.XPATH, '//h1 | //h2 | //h3 | //h4 | //h5 | //h6')
        
        # Check the sequence of the heading tags
        is_sequence_correct = check_html_tag_sequence([tag.tag_name for tag in heading_tags])

        test_results.append({
            'page_url': base_url,
            'testcase': 'HTML Tag Sequence Test (H1-H6)',
            'passed': is_sequence_correct,
            'comments': 'Tag sequence is correct' if is_sequence_correct else 'Tag sequence is broken or missing'
        })
        
        # Get all links on the homepage
        links = driver.find_elements(By.TAG_NAME, 'a')
        all_links = set(link.get_attribute('href') for link in links if link.get_attribute('href'))
        unique_internal_links = {urljoin(base_url, link) for link in all_links if is_internal_link(link, base_url)}

        print(f"Found {len(unique_internal_links)} unique internal links to check.")

        for link in unique_internal_links:
            try:
                driver.get(link)
                wait_for_element(driver, By.TAG_NAME, 'h1')

                # Get all heading tags from H1 to H6 for the page
                heading_tags = driver.find_elements(By.XPATH, '//h1 | //h2 | //h3 | //h4 | //h5 | //h6')
                
                # Check the sequence of the heading tags
                is_sequence_correct = check_html_tag_sequence([tag.tag_name for tag in heading_tags])
                
                result = {
                    'page_url': link,
                    'testcase': 'HTML Tag Sequence Test (H1-H6)',
                    'passed': is_sequence_correct,
                    'comments': 'Tag sequence is correct' if is_sequence_correct else 'Tag sequence is broken or missing'
                }

                test_results.append(result)

            except Exception as e:
                test_results.append({
                    'page_url': link,
                    'testcase': 'HTML Tag Sequence Test (H1-H6)',
                    'passed': False,
                    'comments': f'Error while accessing link: {str(e)}'
                })

        # Generate a consolidated report
        ExcelReporter.generate_report(test_results, 'html_tag_sequence_test')
        print("Test completed. Results saved.")
        
    except Exception as e:
        print(f"Error occurred during the test: {str(e)}")

    return test_results


if __name__ == "__main__":
    driver = get_chrome_driver()
    
    try:
        run_html_tag_sequence_test(driver)
    finally:
        driver.quit()
