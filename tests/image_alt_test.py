from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config
from utils.excel_reporter import ExcelReporter
from drivers.chrome_driver import get_chrome_driver
from utils.web_utils import wait_for_element

def run_image_alt_test(driver):
    """
    Test to ensure that all images on the page have an alt attribute.
    If all images have alt text, report Pass. Otherwise, report Fail with details of missing alt attributes.
    
    :param driver: Selenium WebDriver
    :return: List of test results
    """
    test_results = []
    base_url = Config.TEST_SITE_URL
    all_images_have_alt = True  # Flag to check if all images pass

    try:
        # Navigate to the test URL
        driver.get(base_url)
        print(f"Navigating to {base_url}")

        # Wait for the page to load
        wait_for_element(driver, By.TAG_NAME, "img")

        # Find all images on the page
        images = driver.find_elements(By.TAG_NAME, "img")
        print(f"Found {len(images)} images on the page.")

        # List to store the missing alt text image sources
        missing_alt_images = []

        # Iterate through all images and check the alt attribute
        for image in images:
            alt_text = image.get_attribute("alt")

            # If alt attribute is missing, log the failure
            if not alt_text:
                all_images_have_alt = False
                missing_alt_images.append(image.get_attribute('src'))

        # Prepare the test result
        if all_images_have_alt:
            test_results.append({
                'page_url': base_url,
                'testcase': "Image Alt Attribute Test",
                'passed': True,
                'comments': "All images have alt attributes."
            })
        else:
            test_results.append({
                'page_url': base_url,
                'testcase': "Image Alt Attribute Test",
                'passed': False,
                'comments': f"Missing alt attributes for images: {', '.join(missing_alt_images)}"
            })

        # Generate an Excel report
        print("Generating Excel report...")
        ExcelReporter.generate_report(test_results, 'image_alt_attribute_test')
        print("Image alt attribute test completed. Results saved.")

    except Exception as e:
        print(f"Error occurred during the test: {str(e)}")
        test_results.append({
            'page_url': base_url,
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
