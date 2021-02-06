# test_automation
Test automation with Python and selenium 

**Description:**
Test automation is built using Python programming language and selenium with webdriver. 
Selenium is library compatible with different programming languages, in this case with Python. 
That library interfaces with webdriver and webdriver manipulates with web browser (Chrome). 
Pytest is python library used in test scripts to facilitate test execution.
Basically it requires some prerequisites to be fulfilled.

**Prerequisites:**
1. Setting up Python environment
   Download Python (version used in this case Python 3.9.0) and install:
   https://www.python.org/downloads/release/python-390/
   To check presence of python library use command: pip list (in command line) 
   If not present install selenium: pip install selenium (in command line)
   If not present install pytest: pip install -U pytest (in command line)
2. Setting up webdriver for Chrome
  In Google Chrome browser go to settings and in About Chrome check chrome version (e.g. Version 88.0.4324.146)
  Download webdriver for particular version
  https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/
  Downloaded exe file (Windows) put in folder created for webdrivers and add path to environment variable PATH 
  
**How to use**
  In order to run tests use command line:
  1. Navigate to src directory
  2. Type pytest to run all tests (all files that contain test in name will be executed)
     To run particular test type pytest test_name (>pytest TC01_Log_in_test)
