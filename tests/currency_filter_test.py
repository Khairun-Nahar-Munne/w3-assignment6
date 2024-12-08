from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config.config import Config
from utils.excel_reporter import ExcelReporter
from utils.web_utils import wait_for_element
from drivers.chrome_driver import get_chrome_driver


def run_currency_filter_test(driver):
    """
    Test to ensure that property tile currency changes when selecting a different currency.
    
    :param driver: Selenium WebDriver
    :return: List of test results
    """
    test_results = []
    base_url = Config.TEST_SITE_URL

    try:
        # Navigate to the test URL
        driver.get(base_url)

        # Wait for the currency dropdown/footer to load
        currency_dropdown = wait_for_element(driver, By.ID, "js-currency-sort-footer")

        # Get the list of currencies available
        currency_options = currency_dropdown.find_elements(By.CSS_SELECTOR, ".select-ul li")
        original_currency = driver.find_element(By.CLASS_NAME, "js-price-value").text

        for currency_option in currency_options:
            # Extract the currency country code and symbol
            currency_code = currency_option.get_attribute("data-currency-country")
            currency_symbol = currency_option.find_element(By.TAG_NAME, "p").text.strip()

            # Click the currency option
            ActionChains(driver).move_to_element(currency_option).click().perform()

            # Wait for the price to update
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element(
                    (By.CLASS_NAME, "js-price-value"), currency_symbol
                )
            )

            # Verify the currency symbol in the property price
            updated_price_text = driver.find_element(By.CLASS_NAME, "js-price-value").text
            test_results.append({
                'currency': currency_code,
                'symbol': currency_symbol,
                'original_currency': original_currency,
                'updated_price': updated_price_text,
                'testcase': f"Currency Change to {currency_code}",
                'passed': currency_symbol in updated_price_text,
                'comments': f"Expected {currency_symbol} in price, found {updated_price_text}"
            })

        # Generate an Excel report
        ExcelReporter.generate_report(test_results, 'currency_filtering_test')
        print("Currency filtering test completed. Results saved.")

    except Exception as e:
        print(f"Error occurred during the test: {str(e)}")
        test_results.append({
            'currency': "N/A",
            'symbol': "N/A",
            'original_currency': "N/A",
            'updated_price': "N/A",
            'testcase': "Currency Change Test",
            'passed': False,
            'comments': f"Test failed with error: {str(e)}"
        })

    return test_results


if __name__ == "__main__":
    

    driver = get_chrome_driver()
    try:
        run_currency_filter_test(driver)
    finally:
        driver.quit()
