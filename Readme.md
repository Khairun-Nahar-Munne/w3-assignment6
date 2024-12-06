python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

project_structure/
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


 python3 -m  tests.h1_tag_test
  python3 -m  tests.html_tag_sequence_test

  python3 main.py