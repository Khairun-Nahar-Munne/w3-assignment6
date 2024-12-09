# main.py
from drivers.chrome_driver import get_chrome_driver
from config.config import Config
from tests.h1_tag_test import run_h1_tag_test
from tests.url_status_test import run_url_status_test
from tests.html_tag_sequence_test import run_html_tag_sequence_test
from tests.currency_filter_test import run_currency_filter_test
from tests.image_alt_test import run_image_alt_test
from tests.script_data_test import run_scraping_and_save_report
# Import other test modules as needed

def main():
    # Initialize Chrome WebDriver
    driver = get_chrome_driver()
    
    try:
        # Run tests based on configuration
        for test in Config.TESTS_TO_RUN:
            if test == 'h1_tag_test':
                run_h1_tag_test(driver)
            elif test == 'url_status_test':
                run_url_status_test(driver)
            elif test == 'html_tag_sequence_test':
                run_html_tag_sequence_test(driver)
            elif test == 'currency_filter_test':
                run_currency_filter_test(driver)
            elif test == 'image_alt_test':
                run_image_alt_test(driver)
            else:
                run_scraping_and_save_report(driver)

            # Add other test conditions as needed
    
    except Exception as e:
        print(f"An error occurred during testing: {e}")
    
    finally:
        # Close browser
        driver.quit()

if __name__ == "__main__":
    main()