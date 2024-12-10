from selenium.webdriver.common.by import By
from config.config import Config
from utils.excel_reporter import ExcelReporter
from utils.web_utils import wait_for_element
from drivers.chrome_driver import get_chrome_driver
import re

def scrape_script_data(driver):
    """
    Scrapes necessary data from script tags in the HTML source.
    
    :param driver: Selenium WebDriver
    :return: Dictionary with extracted data
    """
    data = {}
    
    try:
        # Scrape the first script tag for site data (ScriptData.config and userInfo)
        script_data_1 = driver.find_element(By.XPATH, '/html/head/script[4]').get_attribute('innerHTML')
        
        # Extract required fields using regular expressions
        site_data_match = re.search(r'var ScriptData = \{(.*?)\};', script_data_1, re.DOTALL)
        if site_data_match:
            site_data = site_data_match.group(1)
            site_url_match = re.search(r'"SiteUrl":"(.*?)"', site_data)
            site_name_match = re.search(r'"SiteName":"(.*?)"', site_data)
            browser_match = re.search(r'"Browser":"(.*?)"', site_data)
            country_code_match = re.search(r'"CountryCode":"(.*?)"', site_data)
            ip_match = re.search(r'"IP":"(.*?)"', site_data)

            if site_url_match: data['SiteURL'] = site_url_match.group(1)
            if site_name_match: data['SiteName'] = site_name_match.group(1)
            if browser_match: data['Browser'] = browser_match.group(1)
            if country_code_match: data['CountryCode'] = country_code_match.group(1)
            if ip_match: data['IP'] = ip_match.group(1)
        
        # Scrape the second script tag for campaign data (ScriptData.pageData)
        script_data_2 = driver.find_element(By.XPATH, '/html/body/script[5]').get_attribute('innerHTML')
        
        # Extract CampaignId
        campaign_id_match = re.search(r'ScriptData.pageData = \{(.*?)\};', script_data_2, re.DOTALL)
        if campaign_id_match:
            campaign_data = campaign_id_match.group(1)
            campaign_id_match = re.search(r'CampaignId: "(.*?)"', campaign_data)
            if campaign_id_match:
                data['CampaignID'] = campaign_id_match.group(1)
        
        return data
        
    except Exception as e:
        print(f"Error occurred during data scraping: {str(e)}")
        return None

def run_scraping_and_save_report(driver):
    """
    Main function to run the scraping and save the extracted data to an Excel file.
    
    :param driver: Selenium WebDriver
    :return: None
    """
    test_results = []
    base_url = Config.TEST_SITE_URL

    try:
        # First, load the homepage
        driver.get(base_url)
        wait_for_element(driver, By.TAG_NAME, 'h1')

        # Scrape the data from the scripts
        script_data = scrape_script_data(driver)
        
        if script_data:
            # Append the scraped data directly to the test results
            test_results.append({
                'SiteURL': script_data.get('SiteURL', ''),
                'CampaignID': script_data.get('CampaignID', ''),
                'SiteName': script_data.get('SiteName', ''),
                'Browser': script_data.get('Browser', ''),
                'CountryCode': script_data.get('CountryCode', ''),
                'IP': script_data.get('IP', ''),
            })
            
            # Generate a consolidated report with the extracted data
            ExcelReporter.generate_report(test_results, 'script_data_scraping_test')
            print("Data Scrapping completed. Results saved.")
        else:
            print("Failed to scrape data.")
        
    except Exception as e:
        print(f"Error occurred during the test: {str(e)}")

if __name__ == "__main__":
    driver = get_chrome_driver()
    
    try:
        run_scraping_and_save_report(driver)
    finally:
        driver.quit()
