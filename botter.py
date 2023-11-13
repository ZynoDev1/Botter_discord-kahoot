from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException 
from selenium import webdriver
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FireFoxOptions

def main():
    pin = None
    amount = None
    print('Standby waiting for orders :skull:')
    while True: 
        if pin is not None and amount is not None:
            print("PIN:", pin)
            print("AMOUNT:", amount)
            break  
        try:
            with open("pins.txt", "r") as pin_file:
                pin_str = pin_file.read().strip()
                if pin_str:
                    pin = int(pin_str)
            with open("botammount.txt", "r") as amount_file:
                amount_str = amount_file.read().strip()
                if amount_str:
                    amount = int(amount_str)
        except FileNotFoundError:
            print("Waiting for pins.txt and botammount.txt to be available...")
        except ValueError:
            print("Invalid value in pins.txt or botammount.txt")
            
    options = FireFoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    def bot():
        print("LOADING BOT  BOTNUMBER| "+ str(amount))
        driver.get("https://kahoot.it")
        fucktard = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div[3]/div[2]/main/div/form/input")
        fucktard.click()
        fucktard.send_keys(pin)
        startbutton = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div[3]/div[2]/main/div/form/button")
        startbutton.click()
        time.sleep(0.65)
        try:
            userfield = driver.find_element(By.ID, "nickname")    
        except NoSuchElementException:
             print("""Element with ID 'nickname' not found.
                      Most likely invalid pin returning to main program""")
             with open("pins.txt", "w") as pin_file:
                pin_file.write("")
             with open("botammount.txt", "w") as amount_file:
                amount_file.write("")
             main()
        userfield.click()
        userfield.send_keys('stfu fuck you ') 
        start = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div/div[2]/main/div/form/button")
        start.click()
        print(' BOT SUCCESFULLY JOINED BOTNUMBER| ' + str(amount))
        driver.execute_script("window.open('about:blank', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
    while amount > 0:
        bot()  
        amount = amount - 1  # 
#cleanup
    if amount == 0:
        print('done Removing bots in 20 seconds')
        with open("pins.txt", "w") as pin_file:
            pin_file.write("")
        with open("botammount.txt", "w") as amount_file:
            amount_file.write("")
        time.sleep(20)
        print('Bots removed ')
        driver.quit()
        main()
main()