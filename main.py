import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# 1..User SignUp
# Positive scenario:  Signup with valid details
# Negative scenario: Needs to be identified

file_path = r'C:\Users\omii\Desktop\mytest.xlsx'
df = pd.read_excel(file_path)

# Initialize WebDriver (Firefox in this example)
driver = webdriver.Firefox()

try:
    # Navigate to the DemoBlaze website
    driver.get("https://www.demoblaze.com/")
    ########################rmove comment then run the code#####################################################
    # 1. User Sign-Up - Positive Scenario
    # Click on the Sign Up button
#     signup_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, 'signin2'))
#     )
#     signup_button.click()
#
#     # Enter sign up details
#     signup_username = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "sign-username"))
#     )
#     signup_username.send_keys("India@2024")
#
#     signup_password = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "sign-password"))
#     )
#     signup_password.send_keys("Test@123")
#
#     # Submit sign up form
#     signup_submit_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign up')]"))
#     )
#     signup_submit_button.click()
#
#     time.sleep(5)  # Wait to see the result of sign-up
# finally:
#     # Close the browser window
#     driver.quit()

##############################################End code ###################################################


########################rmove comment then run the code#####################################################
    # # 2. User Login - Positive Scenario
#     login_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, 'login2'))
#     )
#     login_button.click()
#
#     login_username = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "loginusername"))
#     )
#     login_username.send_keys("Admin@2025")
#
#     login_password = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "loginpassword"))
#     )
#     login_password.send_keys("Test@123")
#
#     login_submit_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]'))
#     )
#     login_submit_button.click()
#
#     time.sleep(5)  # Wait to see the result of login
#
# finally:
#     #     # Close the browser window
#      driver.quit()
#########################################End code #######################################################



    ########################rmove comment then run the code#####################################################
    # # 3. Product Browsing - Verify products are displayed on the homepage
#     products_displayed = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card.h-100"))
#     )
#
#     if products_displayed:
#         print(f"Products are displayed correctly. Number of products found: {len(products_displayed)}")
#     else:
#         print("No products are displayed on the homepage.")
#
#     # 4. Product Browsing - Navigate to each category
#     categories = ["Phones", "Laptops", "Monitors"]
#
#     for category in categories:
#         category_link = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.LINK_TEXT, category))
#         )
#         category_link.click()
#
#         time.sleep(5)  # Wait for products to load
#
#         category_products_displayed = WebDriverWait(driver, 10).until(
#             EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card.h-100"))
#         )
#
#         if category_products_displayed:
#             print(
#                 f"{category} products are displayed correctly. Number of products found: {len(category_products_displayed)}")
#         else:
#             print(f"No products are displayed for the {category} category.")
#
#         # Return to the homepage after checking each category
#         driver.get("https://www.demoblaze.com/")
#         time.sleep(5)
# finally:
#       driver.quit()

#########################################End code #######################################################


########################Remove comment then run the code#####################################################

     # 5. Adding products to the shopping cart

#     # Navigate to the last page by clicking "Next" until not clickable
#     while True:
#         try:
#             next_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.ID, 'next2'))
#             )
#             driver.execute_script("arguments[0].scrollIntoView();", next_button)
#             next_button.click()
#             time.sleep(3)
#         except:
#             break
#
#     # Click on the last product on the last page
#     last_product_link = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="tbodyid"]/div[last()]/div/div/h4/a'))
#     )
#     last_product_link.click()
#
#     add_to_cart_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a'))
#     )
#     add_to_cart_button.click()
#
#     time.sleep(5)  # Wait to see the result of adding to cart
#
#     # Handle the pop-up alert (confirm product added to cart)
#     WebDriverWait(driver, 10).until(EC.alert_is_present())
#     alert = driver.switch_to.alert
#     alert.accept()
#
#     # 6. Checkout process
#     cart_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "cartur"))
#     )
#     cart_button.click()
#
#     # Check if the product is in the cart
#     time.sleep(5)  # Wait for the cart page to load
#     cart_items = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#tbodyid .success"))
#     )
#
#     if cart_items:
#         print(f"Items are in the cart. Number of items found: {len(cart_items)}")
#     else:
#         print("No items are in the cart.")
#
#     time.sleep(5)
#
# finally:
#     driver.quit()

#########################################End code #######################################################


########################Remove comment then run the code#####################################################

   # 7. Checkout Negative Scenario: Empty the cart and try to checkout

        # Click on the Cart button
# Click on the Cart button
#     cart_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "cartur"))
#     )
#     cart_button.click()
#
#     Delete_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="tbodyid"]/tr/td[4]/a'))
#     )
#     Delete_button.click()
#     # Wait for a while to observe the result
#     time.sleep(10)
#
# finally:
#     # Close the browser window
#     driver.quit()

#########################################End code #######################################################


########################Remove comment then run the code#####################################################

#     # 8. Logout process

# Login process
#     login_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, 'login2'))
#     )
#     login_button.click()
#
#     input_username = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "loginusername"))
#     )
#     input_username.send_keys("Admin@2024")
#
#     input_password = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "loginpassword"))
#     )
#     input_password.send_keys("Test@123")
#
#     submit_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]'))
#     )
#     submit_button.click()
#
#     # Explicitly wait for the page to load after logging in
#     time.sleep(5)
#
#
#
#     Logout_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="logout2"]'))
#     )
#     Logout_button.click()
#     # Wait for a while to observe the result
#     time.sleep(10)
#
# finally:
#     # Close the browser window
#     driver.quit()
#####################################END CODE ######################################################
