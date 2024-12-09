from selenium.webdriver.common.by import By
from config.config import Config
from utils.excel_reporter import ExcelReporter
from utils.web_utils import wait_for_element
from drivers.chrome_driver import get_chrome_driver

def check_html_tag_sequence(tags):
    """
    Check if the HTML tag sequence from H1 to H6 is in the correct order.
    
    :param tags: List of HTML tag elements (e.g., H1, H2, etc.)
    :return: Tuple (True if sequence is correct, False if any tag is missing or out of order, broken_sequence)
    """
    expected_sequence = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    tag_sequence = [tag.lower() for tag in tags]  # Get the lowercase representation of tag names
    last_tag = 0  # To ensure that the sequence is not broken
    broken_sequence = []

    for tag in tag_sequence:
        if expected_sequence.index(tag) < last_tag:
            broken_sequence.append(tag)  # Add the broken tag to the list
        last_tag = expected_sequence.index(tag)

    # Return whether the sequence is correct, and any broken sequences
    return len(broken_sequence) == 0, broken_sequence


def run_html_tag_sequence_test(driver):
    """
    Test for HTML tag sequence (H1-H6) existence and order on the homepage only.
    
    :param driver: Selenium WebDriver
    :return: List of test results
    """
    test_results = []
    base_url = Config.TEST_SITE_URL

    try:
        # Check the homepage for H1-H6 tag sequence
        driver.get(base_url)
        wait_for_element(driver, By.TAG_NAME, 'h1')

        # Get all heading tags from H1 to H6
        heading_tags = driver.find_elements(By.XPATH, '//h1 | //h2 | //h3 | //h4 | //h5 | //h6')
        
        # Check the sequence of the heading tags
        is_sequence_correct, broken_sequence = check_html_tag_sequence([tag.tag_name for tag in heading_tags])

        if is_sequence_correct:
            comments = 'Tag sequence is correct'
        else:
            comments = f'Tag sequence is broken or missing. Broken sequence: {", ".join(broken_sequence)}'

        test_results.append({
            'page_url': base_url,
            'testcase': 'HTML Tag Sequence Test (H1-H6)',
            'passed': is_sequence_correct,
            'comments': comments
        })

        # Generate a consolidated report
        ExcelReporter.generate_report(test_results, 'html_tag_sequence_homepage_test')
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
