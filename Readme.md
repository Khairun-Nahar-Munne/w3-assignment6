# Vacation Rental Home Page Automation Testing Assignment

## Description

This script automates the testing of a vacation rental details page to validate essential elements and functionality, specifically for SEO purposes using Python, Selenium and Pandas. Goals of this assignment:
- Testing SEO-related elements.
- Validating URL.
- Generating Excel files to record test results.


## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Project Structure](#project-structure)
3. [Excel Sheet Model](#excel-sheet-model)
5. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Running the Application](#running-the-application)
6. [Contributing](#contributing)

## Features
- The script checks several test cases such as:

  - **H1 tag existence**: Verifies that an H1 tag is present on the page.
  - **HTML tag sequence**: Ensures that the H1-H6 tags are correctly sequenced.
  - **Image alt attribute**: Checks if images have a valid alt attribute.
  - **URL status code**: Ensures all URLs on the page return valid status codes (no 404 errors).
  - **Currency filter functionality**: Validates that the property tile currency changes when the currency filter is used.
  - **Script data extraction**: Extracts data from the page's scripts and records it in an Excel file.

- The results of the tests will be recorded in an Excel file, capturing any identified issues.

## Prerequisites

Ensure the following requirements are met before running the automation scripts:

1. **Python**  
   - Version: 3.8 or later.  
   - [Download Python](https://www.python.org/downloads/)

2. **Browser**  
   - Google Chrome or Mozilla Firefox must be installed.  
   - [Download Google Chrome](https://www.google.com/chrome/)  
   - [Download Firefox](https://www.mozilla.org/firefox/)

3. **WebDriver Manager**
    - The project uses the `webdriver_manager` library to automatically download and manage the appropriate WebDriver version, so no manual installation is required.  

## Project Structure

```plaintext

  w3-assignment7/
  │
  ├── config/
  │   ├── __init__.py
  │   └── config.py
  │
  ├── drivers/
  │   └── chrome_driver.py
  │
  ├── tests/
  │   ├── __init__.py
  │   ├── h1_tag_test.py
  │   ├── html_tag_sequence_test.py
  │   ├── image_alt_test.py
  │   ├── url_status_test.py
  │   ├── currency_filter_test.py
  │   └── script_data_test.py
  │
  ├── utils/
  │   ├── __init__.py
  │   ├── excel_reporter.py
  │   └── web_utils.py
  │
  ├── requirements.txt
  └── main.py
```

- `config.py`: The config.py file contains configuration settings for running automated tests. It contains the URL of the page on which automated tests are running. Test Site URL: [https://www.alojamiento.io/property/chic-apartament-retiro-park-i-swimming-pool-elevenhost/BC-5455289](https://www.alojamiento.io/property/chic-apartament-retiro-park-i-swimming-pool-elevenhost/BC-5455289)

- `chrome_driver.py`: The chrome_driver.py file provides a utility function to configure and instantiate a Chrome WebDriver for Selenium-based testing. 

- `tests`: The tests folder contains all necessary automated tests files. 

- `excel_reporter.py`: The excel_reporter.py file provides functionality for generating and managing Excel reports for automated test results using Pandas and Openpyxl. It ensures that data is properly organized and stored across multiple sheets within a single Excel file.

- `web_utils.py`: The web_utils.py file provides utility functions to assist with common web automation and validation tasks. These functions streamline operations like checking URL statuses and waiting for web elements during Selenium-based tests.

## Excel Sheet Model:
 - The sheet will have the following columns(Except script_data_test):
     - `page_url`: The URL of the page being tested.
     - `testcase`: The name of the test case.
     - `passed`: Whether the test passed or failed.
     - `comments`: Additional information (such as the status code or missing attributes).

 - The script_data_test excel sheet will have the following columns:
     - `SiteURL`: Scrape SiteURL from Script data.
     - `CampaignID`: Scrape CampaignID from Script data.
     - `SiteName`: Scrape SiteName from Script data.
     - `Browser`: Scrape Browser from Script data.
     - `CountryCode`: Scrape CountryCode from Script data.
     - `IP`: Scrape IP from Script data.
## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Khairun-Nahar-Munne/w3-assignment7.git
   cd w3-assignment7
   ```

2. Set up a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Run All Tests at Once:

   ```bash
   python3 main.py
   ```

2. Run Indivitual Tests (If don't want to run all tests at once):

- **H1 Tag Existence Test**:
  ```bash
  python3 -m tests.h1_tag_test

  ```
- **HTML Tag Sequence Test**:
  ```bash
  python3 -m tests.html_tag_sequence_test
  ```
- **Image Alt Attribute Test**:
  ```bash
  python3 -m tests.image_alt_test
  ```
- **URL Status Code Test**:
  ```bash
  python3 -m tests.url_status_test
  ```
- **Currency Filtering Test**:
  ```bash
  python3 -m tests.currency_filter_test
  ```
- **Script Data Scraping**:
  ```bash
  python3 -m tests.script_data_test
  ```

2. See Execel File:

    ```bash
    Project rooot > test_reports > test_report.xlsx
    ```
  - Test results are saved into test_report folder as test_report.xlsx. Each test file will generate an individual sheet into the excel file after running each test file.
  - Individual excel sheet will also be generated for running same test file. For example, h1_tag_homepage_test, h1_tag_homepage_test1, h1_tag_homepage_test2, etc.

   

## Contributing

Contributions are welcome! Here's how you can contribute:

### Fork the Repository

```bash
- git clone https://github.com/Khairun-Nahar-Munne/hotel-management-system.git
- cd hotel-management-system
```

### Create a New Branch

```bash
- git checkout -b feature/add-new-feature
```

### Make Modifications and Commit Changes

```bash
- git commit -m 'Add new feature: [brief description of the feature]'

```

### Push Changes to the Branch

```bash
- git push origin feature/add-new-feature

```

### Create a New Pull Request

- Navigate to the repository on GitHub.
- Click on the "Compare & pull request" button.
- Fill in the pull request details and submit it for review.
