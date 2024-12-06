# config/config.py
class Config:
    TEST_SITE_URL = "https://www.alojamiento.io/property/chic-apartament-retiro-park-i-swimming-pool-elevenhost/BC-5455289"
    CHROME_DRIVER_PATH = None  # Will be set dynamically
    REPORT_DIRECTORY = "test_reports/"
    
    # Test Parameters
    TESTS_TO_RUN = [
        'h1_tag_test',
        'html_tag_sequence_test', 
        'image_alt_test',
        'url_status_test',
        'currency_filter_test',
        'script_data_test'
    ]