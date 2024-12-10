# Vacation Rental Home Page Automation Testing Assignment

## Description

This script automates the testing of a vacation rental details page to validate essential elements and functionality, specifically for SEO purposes. The script checks several test cases such as:

- **H1 tag existence**: Verifies that an H1 tag is present on the page.
- **HTML tag sequence**: Ensures that the H1-H6 tags are correctly sequenced.
- **Image alt attribute**: Checks if images have a valid alt attribute.
- **URL status code**: Ensures all URLs on the page return valid status codes (no 404 errors).
- **Currency filter functionality**: Validates that the property tile currency changes when the currency filter is used.
- **Script data extraction**: Extracts data from the page's scripts and records it in an Excel file.

The results of the tests will be recorded in an Excel file, capturing any identified issues.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Prerequisites](#prerequisites)
4. [Project Structure](#project-structure)
5. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Database Configuration](#database-configuration)
   - [Running the Application](#running-the-application)
6. [Usage](#usage)
7. [Database Schema](#database-schema)

## Requirements

### Tools:

- **Python** (Version: 3.x)
- **Selenium** for web automation.
- **Pandas** for generating Excel reports.
- **Requests** for checking URL status codes.

### Browser:

- **Google Chrome** or **Firefox** (make sure to use the corresponding WebDriver version).
- You can download the Chrome WebDriver from [here](https://sites.google.com/chromium.org/driver/), or the Firefox WebDriver from [here](https://github.com/mozilla/geckodriver/releases).

### Test Site URL:

- [https://www.alojamiento.io/property/chic-apartament-retiro-park-i-swimming-pool-elevenhost/BC-5455289](https://www.alojamiento.io/property/chic-apartament-retiro-park-i-swimming-pool-elevenhost/BC-5455289)

### Tests to Perform:

- **H1 Tag Existence Test**: The script will check if the page contains an H1 tag. If missing, the test will fail.
- **HTML Tag Sequence Test**: The script checks that the H1-H6 tags appear in the correct order (H1 before H2, H2 before H3, etc.). If any sequence is broken or missing, the test will fail.
- **Image Alt Attribute Test**: Verifies if all images on the page have an alt attribute. Missing alt attributes will cause the test to fail.
- **URL Status Code Test**: Checks all URLs on the page to ensure they do not return a 404 (Page Not Found) error.
- **Currency Filtering Test**: Tests the property tiles to confirm that their currency changes when a new currency is selected.
- **Script Data Scraping**: Scrapes specific data from the scripts and records it in an Excel file, including:
  - Site URL
  - Campaign ID
  - Site Name
  - Browser
  - Country Code
  - IP address

## Acceptance Criteria

1. **Reusability**: The code and methods should be reusable for different pages or test cases.
2. **Output Format**: The script will generate an excel report for individual test cases.
3. **Report Model**:
   - The report will have the following columns:
     - `page_url`: The URL of the page being tested.
     - `testcase`: The name of the test case.
     - `passed`: Whether the test passed or failed.
     - `comments`: Additional information (such as the status code or missing attributes).

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
   source env/bin/activate   # On Windows use `source .env/bin/activate
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

2. Run Indivitual Tests:

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

   Test results are saved into test_report folder as test_report.xlsx. Each test file will generate an individual sheet into the excel file after running each test file.

   ```bash
   Project rooot > test_reports > test_report.xlsx
   ```

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
