# from pathlib import Path

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from time import sleep  # Fixed import

# ROOT_FOLDER = Path(__file__).parent
# CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver'

# def make_chrome_browser(*options: str) -> webdriver.Chrome:
#     chrome_options = webdriver.ChromeOptions()
    
#     # Add default options for stability
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')
    
#     if options is not None:
#         for option in options:
#             chrome_options.add_argument(option)
            
#     chrome_service = Service(
#         executable_path=str(CHROME_DRIVER_PATH),
#     )
    
#     chrome_browser = webdriver.Chrome(
#         service=chrome_service,
#         options=chrome_options,
#     )
    
#     return chrome_browser

# if __name__ == '__main__':
#     # Initialize browser with headless mode
#     options = ()
#     browser = make_chrome_browser(*options)

#     browser.get('https://www.google.com.br')

#     sleep(10)
#     # # Initialize browser without headless mod
#     # try:
#     #     # Navigate to Google
#     #     chrome_browser.get('https://www.google.com')
#     #     time.sleep(10)  # Small delay to ensure page loads
        
#     #     print("Browser session created successfully!")
        
#     # except Exception as e:
#     #     print(f"An error occurred: {e}")
        
#     # finally:
#     #     # Always close the browser
#     #     chrome_browser.quit()


# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # Add default options for stability
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-infobars')
    
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser

if __name__ == '__main__':
    TIME_TO_WAIT = 20
    MAX_RETRIES = 3

    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    
    for attempt in range(MAX_RETRIES):
        try:
            browser = make_chrome_browser(*options)
            
            # Como antes
            browser.get('https://www.google.com')

            # Espere para encontrar o input
            search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
                EC.presence_of_element_located(
                    (By.NAME, 'q')
                )
            )
            search_input.send_keys('noticias de hoje')
            search_input.send_keys(Keys.ENTER)

            # Wait for search results using a more reliable selector
            results = WebDriverWait(browser, TIME_TO_WAIT).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'div.g')  # More specific selector
                )
            )
            
            # Find all result links within the first result
            links = results.find_elements(By.TAG_NAME, 'a')
            
            # Click the first valid link
            for link in links:
                href = link.get_attribute('href')
                if href and 'google' not in href.lower():
                    # Use JavaScript click to avoid potential intercepted click
                    browser.execute_script("arguments[0].click();", link)
                    break

            # Dorme por 20 segundos
            sleep(TIME_TO_WAIT)
            break  # Success, exit the retry loop
            
        except Exception as e:
            print(f"Attempt {attempt + 1} failed with error: {e}")
            if attempt < MAX_RETRIES - 1:
                print("Retrying...")
                sleep(2)  # Wait before retry
            else:
                print("Max retries reached. Giving up.")
                
        finally:
            try:
                browser.quit()
            except:
                pass  # Ignore errors during browser cleanup