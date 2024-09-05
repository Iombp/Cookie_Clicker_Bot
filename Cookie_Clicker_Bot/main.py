# Script created using version 2.052; newer features may not be compatible

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import sys
import keyboard
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import re
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException

stop_threads = False

# Function responsible for collecting golden cookies and clicking the big cookie
def big_cookie_click():
    global stop_threads
    try:
        while not stop_threads:
            try:
                # Checking and clicking the Golden Cookie (shimmer)
                golden_cookies = driver.find_elements(By.CLASS_NAME, "shimmer")
                if golden_cookies:
                    for golden_cookie in golden_cookies:
                        if golden_cookie.is_displayed() and golden_cookie.is_enabled():
                            try:
                                golden_cookie.click()
                                time.sleep(0.1)
                            except (ElementClickInterceptedException, StaleElementReferenceException):
                                pass 

                # Checking and clicking the Big Cookie
                big_cookie = driver.find_element(By.ID, "bigCookie")
                if big_cookie.is_displayed() and big_cookie.is_enabled():
                    try:
                        big_cookie.click()
                    except ElementClickInterceptedException:
                        pass 
                time.sleep(0.01)
                
            except NoSuchElementException:
                pass 
            except StaleElementReferenceException:
                pass 

    except Exception as e:
        print("ENDING big_cookie_click FUNCTION:", e)

# Function responsible for handling upgrades
# A very simple function. I initially intended to create a function that performs calculations based on the cost of an upgrade,
# its efficiency, and the time required to gather enough resources for that upgrade. However, the function always ended up
# upgrading the last upgrade regardless of other factors, which was not the desired behavior.
# I’m very curious about the best way to implement this. If you have ideas for a better function, that's me https://github.com/Iombp
def auto_upgrades():
    while not stop_threads:
        try:
            time.sleep(0.1)
            crate_products = driver.find_elements(By.XPATH, "//div[@class='crate upgrade enabled']")
            if crate_products:
                crate_products[0].click()
            products = driver.find_elements(By.XPATH, "//div[@class='product unlocked enabled']")
            if products:
                products[-1].click()
        except (ElementClickInterceptedException, StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException):
            pass 

# Function responsible for closing pop-ups
def close_popups():
    global stop_threads
    while not stop_threads:
        # Chose EN lang
        try:
            language_button = driver.find_element(By.ID, "langSelect-EN")
            language_button.click()
        except Exception:
            pass

        # Close "Got it"
        try:
            got_it_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/a[1]")
            got_it_btn.click()
        except Exception:
            pass
        
        # Close achievements
        try:
            close_ach = driver.find_element(By.CLASS_NAME, "close")
            close_ach.click()
        except:
            pass
        
        time.sleep(1)

# Function that notifies everyone that the bot is running (completely useless)
def change_bakery_name():
    try:
        bakery_name = driver.find_element(By.ID,'bakeryName')
        bakery_name.click()
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "bakeryNameInput"))
        )
        newname = "Iombp" # You can change this string to set your own name. 
        # You can also remove this function if it is not needed (Remember to also remove line 354).
        
        driver.execute_script(f"document.getElementById('bakeryNameInput').value = '{newname}';")
        driver.execute_script("document.getElementById('bakeryNameInput').dispatchEvent(new Event('change'));")

        confirm = driver.find_element(By.ID,'promptOption0')
        confirm.click()
    except Exception as e:
        print(f"Exception occurred while changing bakery name: {e}")
        
        
# Function responsible for using sugar lumps. It upgrades each upgrade evenly 
# (To activate, uncomment lines 385 and 386).
def use_lumps():
    while not stop_threads:
        try:   
            time.sleep(5)
            for i in range(0, 19):
                upgrade_lumps_script = f"Game.ObjectsById[{i}].levelUp()"
                driver.execute_script(upgrade_lumps_script) 
        except:
            pass
        
# Function responsible for adding a sugar lump. It works very well but may disrupt the fun.
# You can add lumps using the command Game.gainLumps(amount) in the console (press F12).
# (To activate, uncomment lines 388 and 389).
def gain_lumps():
    while not stop_threads:
        driver.execute_script("Game.gainLumps(1)")
        time.sleep(10) # Time interval in seconds for receiving 1 sugar lump

# Function ascend: It is advised not to use it may halt the program. 
# Upgrades everything in a specified order (order is random; no calculations were made when creating this bot).
# Function may cause issues with other functions and can disrupt the program.
# I plan to fix this function soon.
# def ascend():
#     global ascend_count
#     while not stop_threads:
#         try:
#             time.sleep(43200)
            
#             ascend_btn = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.ID, "legacyButton"))
#             )
#             ascend_btn.click()
#             print('1')
#             time.sleep(0.5)
            
#             ascend_btn_ascend = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.ID, "promptOption0"))
#             )
#             ascend_btn_ascend.click()
#             print('2')
#             time.sleep(10)

#             heven_chips = driver.find_elements(By.ID, "ascendHCs")
#             chips_amount = heven_chips[0].text

#             chips_amount = chips_amount.replace(",", "")

#             match = re.search(r"\d+", chips_amount)

#             if match:
#                 chips_amount = int(match.group())
#                 print('3')
#             else:
#                 print("Num not found.")
#                 chips_amount = 0

#             orders = [363, 323, 264, 265, 266, 267, 268, 395, 520, 282, 328, 326, 253, 255, 254, 288, 290, 719, 720, 
#                       411, 283, 412, 284, 286, 285, 287, 181, 289, 281, 353, 274, 354, 275, 355, 276, 368, 356, 277, 
#                       393, 357, 278, 291, 358, 279, 646, 717, 718, 394, 359, 280, 325, 141, 269, 273, 271, 272, 270, 
#                       819, 537, 327, 365, 647, 397, 360, 643, 562, 591, 592, 801, 802, 803, 329, 326, 804, 805, 292, 
#                       364, 293, 396, 495, 408, 449, 450, 409, 539, 451, 410, 542, 540, 541, 496, 561, 505, 787, 768, 
#                       788, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779]

#             # 264 Game.PutUpgradeInPermanentSlot(6,0)   100 
#             # 265 Game.PutUpgradeInPermanentSlot(43,1)  20 000
#             # 266 Game.PutUpgradeInPermanentSlot(82,2)  3 000 000
#             # 267 Game.PutUpgradeInPermanentSlot(109,3) 400 000 000
#             # 268 Game.PutUpgradeInPermanentSlot(188,4) 50 000 000 000
#             for order in orders:
#                 if order == 264 and chips_amount > 111:
#                     try:
#                         driver.execute_script(f"Game.PurchaseHeavenlyUpgrade({order})")
#                         time.sleep(0.2)
#                         driver.execute_script(f"Game.PutUpgradeInPermanentSlot(6,0)")
#                         time.sleep(0.2)

#                         prompt_option0 = WebDriverWait(driver, 10).until(
#                             EC.element_to_be_clickable((By.ID, "promptOption0"))
#                         )
#                         driver.execute_script("arguments[0].scrollIntoView(true);", prompt_option0)
#                         prompt_option0.click()
#                         print('4')

#                     except (ElementClickInterceptedException, StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException):
#                         print('ERROR:1')
#                         prompt_option0 = driver.find_element(By.ID, "promptOption0")
#                         prompt_option0.click()
#                 elif order == 264 and chips_amount > 20000:
#                     try:
#                         driver.execute_script(f"Game.PurchaseHeavenlyUpgrade({order})")
#                         time.sleep(0.2)
#                         driver.execute_script(f"Game.PutUpgradeInPermanentSlot(43,1)")
#                         time.sleep(0.2)

#                         prompt_option0 = WebDriverWait(driver, 10).until(
#                             EC.element_to_be_clickable((By.ID, "promptOption0"))
#                         )
#                         driver.execute_script("arguments[0].scrollIntoView(true);", prompt_option0)
#                         prompt_option0.click()
#                         print('4')

#                     except (ElementClickInterceptedException, StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException):
#                         print('ERROR:2')
#                         prompt_option0 = driver.find_element(By.ID, "promptOption0")
#                         prompt_option0.click()
#                 elif order == 264 and chips_amount > 3000000:
#                     try:
#                         driver.execute_script(f"Game.PurchaseHeavenlyUpgrade({order})")
#                         time.sleep(0.2)
#                         driver.execute_script(f"Game.PutUpgradeInPermanentSlot(82,2)")
#                         time.sleep(0.2)

#                         prompt_option0 = WebDriverWait(driver, 10).until(
#                             EC.element_to_be_clickable((By.ID, "promptOption0"))
#                         )
#                         driver.execute_script("arguments[0].scrollIntoView(true);", prompt_option0)
#                         prompt_option0.click()
#                         print('4')

#                     except (ElementClickInterceptedException, StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException):
#                         print('ERROR:2')
#     
#                         prompt_option0 = driver.find_element(By.ID, "promptOption0")
#                         prompt_option0.click()
#                 elif order == 264 and chips_amount > 400000000:
#                     try:
#                         driver.execute_script(f"Game.PurchaseHeavenlyUpgrade({order})")
#                         time.sleep(0.2)
#                         driver.execute_script(f"Game.PutUpgradeInPermanentSlot(109,3)")
#                         time.sleep(0.2)

#                     
#                         prompt_option0 = WebDriverWait(driver, 10).until(
#                             EC.element_to_be_clickable((By.ID, "promptOption0"))
#                         )
#                         driver.execute_script("arguments[0].scrollIntoView(true);", prompt_option0)
#                         prompt_option0.click()
#                         print('4')

#                     except (ElementClickInterceptedException, StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException):
#                   
#                   
#                         prompt_option0 = driver.find_element(By.ID, "promptOption0")
#                         prompt_option0.click()
#                 elif order == 264 and chips_amount > 51000000000:
#                     try:
#                         driver.execute_script(f"Game.PurchaseHeavenlyUpgrade({order})")
#                         time.sleep(0.2)
#                         driver.execute_script(f"Game.PutUpgradeInPermanentSlot(188,4)")
#                         time.sleep(0.2)

#                       
#                         prompt_option0 = WebDriverWait(driver, 10).until(
#                             EC.element_to_be_clickable((By.ID, "promptOption0"))
#                         )
#                         driver.execute_script("arguments[0].scrollIntoView(true);", prompt_option0)
#                         prompt_option0.click()
#                         print('4')

#                     except (ElementClickInterceptedException, StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException):
#            
#                       
#                         prompt_option0 = driver.find_element(By.ID, "promptOption0")
#                         prompt_option0.click()
#                 else:
#                     driver.execute_script(f"Game.PurchaseHeavenlyUpgrade({order})")
#                     time.sleep(0.2)
#         except (ElementClickInterceptedException, StaleElementReferenceException):
#             time.sleep(0.5)
#             ascend_after = driver.find_element(By.ID, "ascendButton")
#             ascend_after.click()

#             time.sleep(0.5)
#             ok_btn = driver.find_element(By.ID, "promptOption0")
#             ok_btn.click()

#             time.sleep(3)
#             ascend_count += 1
            

#         time.sleep(0.5)
#         ascend_after = driver.find_element(By.ID, "ascendButton")
#         ascend_after.click()

#         time.sleep(0.5)
#         ok_btn = driver.find_element(By.ID, "promptOption0")
#         ok_btn.click()
#         ascend_count += 1
    
# Simple function that tracks the runtime duration of the program.
def measure_working_time():
    start_time = time.time()
    i = 0
    t = 1
    while not stop_threads:
        time.sleep(1)
        i += 1
        elapsed_time = time.time() - start_time 
        if elapsed_time >= 60:
            print(f"{t * 1}")
            t += 1
            start_time = time.time()

# Function that upgrades the dragon.
def upgrade_dragon():
    while not stop_threads:
        driver.execute_script(f"Game.UpgradeDragon()")
        time.sleep(1)
        
    

# Chrome settings configuration.
chrome_options = Options()
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("user-data-dir=C:\\chrome_profile")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--force-renderer-accessibility")

# Path to chromedriver.exe
service = Service("chromedriver.exe")

# Run chrome with choosen profile
driver = webdriver.Chrome(service=service, options=chrome_options)

# Run CookieClicker site
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Maximize the browser window.
driver.maximize_window()

change_bakery_name()

# This is not needed and does not cause any bugs.
print("Click the 'X' in the Privacy and cookie settings located in the lower-left corner.")
# Time delay before starting the program.
time.sleep(10)




# All threading in 1 place
big_cookie_click_t = threading.Thread(target=big_cookie_click)
big_cookie_click_t.start()

auto_upgrades_t = threading.Thread(target=auto_upgrades)
auto_upgrades_t.start()

close_popups_t = threading.Thread(target=close_popups)
close_popups_t.start()

measure_working_time_t = threading.Thread(target=measure_working_time)
measure_working_time_t.start()

upgrade_dragon_t = threading.Thread(target=upgrade_dragon)
upgrade_dragon_t.start()



# use_lumps_t = threading.Thread(target=use_lumps)
# use_lumps_t.start()

# gain_lumps_t = threading.Thread(target=gain_lumps)
# gain_lumps_t.start()

# ascend_t = threading.Thread(target=ascend)
# ascend_t.start()



save = ActionChains(driver)
try:
    while True:
        # Check if the 'ESC' key is pressed
        if keyboard.is_pressed('esc'):
            print("ESC pressed. Exiting program...")
            # Save current state using Ctrl+S
            save.key_down(Keys.CONTROL).send_keys('s').key_up(Keys.CONTROL).perform()
            time.sleep(2)  # Wait for the save action to complete
            stop_threads = True  # Signal to stop other threads
            driver.quit()  # Close the browser
            break  # Exit the loop

        time.sleep(0.1)  # Short delay to prevent high CPU usage

except KeyboardInterrupt:
    # Handle interruption from keyboard (e.g., Ctrl+C)
    print("Program interrupted.")
    stop_threads = True  # Signal to stop other threads
    driver.quit()  # Close the browser
    sys.exit()  # Exit the program