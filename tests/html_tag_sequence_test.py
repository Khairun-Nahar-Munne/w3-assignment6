from selenium.webdriver.common.by import By
from config.config import Config
from utils.excel_reporter import ExcelReporter
from utils.web_utils import wait_for_element
from drivers.chrome_driver import get_chrome_driver

def check_html_tag_sequence(tags):
    """
    Check if the HTML tag sequence from H1 to H6 is in the correct order and identify missing or broken tags.
    
    :param tags: List of HTML tag elements (e.g., H1, H2, etc.)
    :return: Tuple (True if sequence is correct, False otherwise, missing_tags, broken_sequence, detected_sequence)
    """
    expected_sequence = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    tag_sequence = [tag.lower() for tag in tags]  # Get the lowercase representation of tag names
    last_tag_index = -1  # To track the order
    broken_sequence = []
    missing_tags = []

    # Iterate through expected tags and check the sequence
    for i, tag in enumerate(expected_sequence):
        if tag in tag_sequence:
            current_index = tag_sequence.index(tag)
            if current_index < last_tag_index:
                broken_sequence.append(tag)  # Tag is out of order
            last_tag_index = current_index
        else:
            missing_tags.append(tag)  # Tag is missing

    # Return result: is sequence correct, missing tags, broken sequence, and the detected sequence
    is_correct = len(broken_sequence) == 0 and len(missing_tags) == 0
    return is_correct, missing_tags, broken_sequence, tag_sequence


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
        print("Starting HTML tag sequence test...")
        driver.get(base_url)
        wait_for_element(driver, By.TAG_NAME, 'h1')

        # Get all heading tags from H1 to H6
        heading_tags = driver.find_elements(By.XPATH, '//h1 | //h2 | //h3 | //h4 | //h5 | //h6')

        # Extract the tag names
        tag_names = [tag.tag_name for tag in heading_tags]

        # Check the sequence of the heading tags
        is_sequence_correct, missing_tags, broken_sequence, detected_sequence = check_html_tag_sequence(tag_names)

        # Determine comments based on the results
        if is_sequence_correct:
            comments = 'Tag sequence is correct.'
        else:
            comments = []
            if missing_tags:
                comments.append(f'Missing tags: {", ".join(missing_tags)}')
            if broken_sequence:
                 comments.append(f'Broken sequence: {", ".join(detected_sequence)}')  # Add detected sequence
           
            comments = ' '.join(comments)

        # Add results to the test report
        test_results.append({
            'page_url': base_url,
            'testcase': 'HTML Tag Sequence Test (H1-H6)',
            'passed': is_sequence_correct,
            'comments': comments
        })

        # Generate a consolidated report
        ExcelReporter.generate_report(test_results, 'html_tag_sequence_homepage_test')
        print("HTML tag sequence test completed. Results saved.")

    except Exception as e:
        print(f"Error occurred during the test: {str(e)}")
        test_results.append({
            'page_url': base_url,
            'testcase': 'HTML Tag Sequence Test (H1-H6)',
            'passed': False,
            'comments': f"Test failed with error: {str(e)}"
        })

    return test_results


if __name__ == "__main__":
    driver = get_chrome_driver()
    
    try:
        run_html_tag_sequence_test(driver)
    finally:
        driver.quit()
