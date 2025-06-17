from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

URL = "http://13.60.232.156:3000"

def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = "/usr/bin/google-chrome"
    return webdriver.Chrome(options=options)


def test_hero_title():
    driver = setup_browser()
    driver.get(URL)
    assert "Banking made simple, secure, and fast" in driver.page_source
    driver.quit()

def test_hero_description():
    driver = setup_browser()
    driver.get(URL)
    assert "Access your accounts, send money instantly, and manage your finances" in driver.page_source
    driver.quit()

def test_get_started_button():
    driver = setup_browser()
    driver.get(URL)
    get_started_button = driver.find_element(By.LINK_TEXT, 'Get Started')
    assert get_started_button is not None
    driver.quit()

def test_sign_in_button():
    driver = setup_browser()
    driver.get(URL)
    sign_in_button = driver.find_element(By.LINK_TEXT, 'Sign In')
    assert sign_in_button is not None
    driver.quit()

def test_zelle_instant_transfers():
    driver = setup_browser()
    driver.get(URL)
    assert "Zelle" in driver.page_source and "Instant Transfers" in driver.page_source
    driver.quit()

def test_secure_banking_feature():
    driver = setup_browser()
    driver.get(URL)
    assert "Secure Banking" in driver.page_source
    driver.quit()

def test_instant_transfers_feature():
    driver = setup_browser()
    driver.get(URL)
    assert "Instant Transfers" in driver.page_source
    driver.quit()

def test_user_friendly_feature():
    driver = setup_browser()
    driver.get(URL)
    assert "User-Friendly" in driver.page_source
    driver.quit()

def test_bank_level_security():
    driver = setup_browser()
    driver.get(URL)
    assert "Bank-Level Security" in driver.page_source
    driver.quit()

def test_faq_section():
    driver = setup_browser()
    driver.get(URL)
    assert "Frequently Asked Questions" in driver.page_source
    driver.quit()