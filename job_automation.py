import json
from selenium.webdriver.common.by import By
from driver import get_driver

def apply_to_job(linkedin_cookies):
    driver = get_driver()
    # Load LinkedIn or any other job site
    driver.get("https://www.linkedin.com/")

    # Set cookies
    for cookie in linkedin_cookies:
        driver.add_cookie(cookie)

    # Navigate to job page and apply
    # Add your application logic here
    # Example:
    driver.get("URL_OF_JOB")
    # Your logic to apply for the job...

    driver.quit()
