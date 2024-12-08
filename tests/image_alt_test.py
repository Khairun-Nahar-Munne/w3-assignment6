from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config
from utils.excel_reporter import ExcelReporter
from utils.web_utils import wait_for_element
from drivers.chrome_driver import get_chrome_driver

def run_image_alt_test(driver):
    """
    Test to ensure that all images on the page have an alt attribute.
    
    :param driver: Selenium WebDriver
    :return: List of test results
    """
    test_results = []
    base_url = Config.TEST_SITE_URL

    try:
        # Navigate to the test URL
        driver.get(base_url)
        print(f"Navigating to {base_url}")

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "img")))

        # Find all images on the page
        images = driver.find_elements(By.TAG_NAME, "img")
        print(f"Found {len(images)} images on the page.")

        # Iterate through all images and check the alt attribute
        for image in images:
            alt_text = image.get_attribute("alt")

            # Check if alt attribute is missing
            if not alt_text:
                print(f"Image missing alt attribute: {image.get_attribute('src')}")
                test_results.append({
                    'image_src': image.get_attribute('src'),
                    'alt_text': "N/A",
                    'testcase': "Image Alt Attribute",
                    'passed': False,
                    'comments': "Alt attribute is missing."
                })
            else:
                test_results.append({
                    'image_src': image.get_attribute('src'),
                    'alt_text': alt_text,
                    'testcase': "Image Alt Attribute",
                    'passed': True,
                    'comments': "Alt attribute is present."
                })

        # Generate an Excel report
        print("Generating Excel report...")
        ExcelReporter.generate_report(test_results, 'image_alt_attribute_test')
        print("Image alt attribute test completed. Results saved.")

    except Exception as e:
        print(f"Error occurred during the test: {str(e)}")
        test_results.append({
            'image_src': "N/A",
            'alt_text': "N/A",
            'testcase': "Image Alt Attribute Test",
            'passed': False,
            'comments': f"Test failed with error: {str(e)}"
        })

    return test_results


if __name__ == "__main__":
    # Setup WebDriver
    driver = get_chrome_driver()
    try:
        run_image_alt_test(driver)
    finally:
        driver.quit()
