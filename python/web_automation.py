from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import lxml 
import math
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import re

start_time = time.perf_counter()

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('google-api.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)
sheet = client.open('google-drive-file-name')
# get the first sheet of the Spreadsheet
chromedriver_location = "filepath/chromedriver"

sheet_instance = sheet.get_worksheet(0)
og_records_data = sheet_instance.get_all_records()
row = 2

for i in og_records_data:
	if (not i['redeemed']):
		card_type = i['card_type']
		card_number = i['card_num']
		pin = str(i['pin']).zfill(10)
		first_name = i['first_name']
		last_name = i['last_name']
		email = i['email']
		amount = i['amount']

		# print('Pin: ', pin.zfill(10))
	
		options = webdriver.ChromeOptions()
		options.add_experimental_option("detach", True)
		driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver_location)
		driver.get('https://redeem.giftcards.com/')
		time.sleep(6) 

		try:
			accept_cookies = '//*[@id="truste-consent-button"]'
			driver.find_element_by_xpath(accept_cookies).click()
		except:
			continue
		
		time.sleep(1)

		username_input = '//*[@id="cardCode"]'
		password_input = '//*[@id="root"]/section[1]/section/div/div[2]/div[2]/form/div[2]/div/input'
		login_submit = '//*[@id="root"]/section[1]/section/div/div[2]/div[2]/form/button'

		driver.execute_script("window.scrollTo(0, 300)") 
		time.sleep(3) 

		driver.find_element_by_xpath(username_input).send_keys(card_number)
		driver.find_element_by_xpath(password_input).send_keys(pin)
		driver.find_element_by_xpath(login_submit).click()

		time.sleep(7)
		card_type_path_h4h = '//*[@id="tilesContainer"]/div/div/div[2]/div/div/div[1]/span'
		card_type_path_cty = '//*[@id="tilesContainer"]/div/div/div[4]/div/div/div[1]/span'

		for z in range(3):
			try:
				if (card_type == "H4H" and "Home Depot" in driver.find_element_by_xpath(card_type_path_h4h+'/img').get_attribute('alt')):
					driver.find_element_by_xpath(card_type_path_h4h).click()
					print('H4H Card Type: ', driver.find_element_by_xpath(card_type_path_h4h+'/img').get_attribute('alt'))
				elif (card_type == "C2Y" and "Home Depot" in driver.find_element_by_xpath(card_type_path_cty+'/img').get_attribute('alt')):
					driver.find_element_by_xpath(card_type_path_cty).click()
					print('C2Y Card Type: ', driver.find_element_by_xpath(card_type_path_cty+'/img').get_attribute('alt'))
				else: 
					sys.exit()
			except:
				time.sleep(3)

		time.sleep(3)

		dollar_value_1 = '/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/label'
		dollar_value_2 = '/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/label'
		dollar_value_3 = '/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[3]/label'

		if (int(float(driver.find_element_by_xpath(dollar_value_1).text.strip('$').strip())) == amount):
			driver.find_element_by_xpath(dollar_value_1).click()
		elif (int(float(driver.find_element_by_xpath(dollar_value_2).text.strip('$').strip())) == amount):
			driver.find_element_by_xpath(dollar_value_2).click()
		else:
			driver.find_element_by_xpath(dollar_value_3).click()

		time.sleep(1)

		# dollar_value = '/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[3]/label'
		# print(driver.find_element_by_xpath(dollar_value).get_attribute('value'))
		# driver.find_element_by_xpath(dollar_value).click()

		add_to_basket = '/html/body/div[2]/div/div/div[2]/div[1]/div[2]/button'
		driver.find_element_by_xpath(add_to_basket).click()

		time.sleep(3)

		checkout = '//*[@id="appTopBarPortal"]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/div/a/button'
		driver.find_element_by_xpath(checkout).click()

		driver.execute_script("window.scrollTo(0, 300)") 
		time.sleep(2) 

		first_name_path = '//*[@id="confirmationForm"]/div[1]/div[1]/div[1]/div[1]/div/input'
		driver.find_element_by_xpath(first_name_path).send_keys(first_name)

		last_name_path = '//*[@id="confirmationForm"]/div[1]/div[1]/div[1]/div[2]/div/input'
		driver.find_element_by_xpath(last_name_path).send_keys(last_name)

		email_path = '//*[@id="confirmationForm"]/div[1]/div[1]/div[1]/div[3]/div/input'
		confirm_email_path = '//*[@id="confirmationForm"]/div[1]/div[1]/div[1]/div[4]/div/input'
		driver.find_element_by_xpath(email_path).send_keys(email)
		driver.find_element_by_xpath(confirm_email_path).send_keys(email)

		driver.execute_script("window.scrollTo(0, 600)") 
		time.sleep(2) 

		acknowledge = '//*[@id="confirmationForm"]/div[1]/div[1]/div[3]/div[1]/div/label/span'
		confirm_emails = '//*[@id="confirmationForm"]/div[1]/div[1]/div[3]/div[2]/div/label/span'

		driver.find_element_by_xpath(acknowledge).click()
		driver.find_element_by_xpath(confirm_emails).click()

		card_type_verify = driver.find_element_by_xpath('//*[@id="confirmationForm"]/div[1]/div[2]/div[1]/div/span[1]').text
		amount_verify = driver.find_element_by_xpath('//*[@id="confirmationForm"]/div[1]/div[2]/div[1]/div/span[2]').text
		amount_verify = float(amount_verify.strip('$').strip())

		# print('Verified Amount: ', int(amount_verify))

		if (int(amount) == int(amount_verify) and "Home Depot" in card_type_verify):
			place_order = '//*[@id="confirmationForm"]/div[2]/button'
			# print('Is button enabled: ', driver.find_element_by_xpath(place_order).is_enabled())
			time.sleep(1)
			driver.find_element_by_xpath(place_order).click()
		else:
			sys.exit()

		time.sleep(2)

		confirm_1 = '/html/body/div[3]/div/div/button[2]'
		confirm_2 = '/html/body/div[2]/div/div/button[2]'

		if (driver.find_element_by_xpath(confirm_1).text == "Confirm" or driver.find_element_by_xpath(confirm_2).text == "Confirm"):
			try:
				driver.find_element_by_xpath(confirm_1).click()
			except:
				driver.find_element_by_xpath(confirm_2).click()
		else:
			print("Can't find confirm button")
			sys.exit()
		time.sleep(5)

		sheet_instance.update_cell(row, 8, 'yes')
		found_card = False  

		for y in range(10):
			view_egift = '//*[@id="reactRoot"]/div/div[2]/div/div[1]/div[2]/table/tbody/tr/td[3]/a'
			try:
				if (driver.find_element_by_xpath(view_egift).is_enabled()):
					url = driver.find_element_by_xpath(view_egift).get_attribute('href')
					sheet_instance.update_cell(row, 12, url)
					driver.find_element_by_xpath(view_egift).click()
					time.sleep(5)
					f = requests.get(url)
					for line in f.text.splitlines():
						if ("eGift Card:" in line.strip()):
							card_number = re.findall(r'[0-9]{23}', line.strip(" "))
							sheet_instance.update_cell(row, 10, ''.join(card_number))
						if ("PIN:" in line.strip()):
							pin = re.findall(r'[0-9]{4}', line.strip(" "))
							print('New Gift Card Pin: ', pin)
							sheet_instance.update_cell(row, 11, ''.join(pin))
					# tabs = driver.window_handles
					# driver.switch_to_window(tabs[1])
					break
			except:
				time.sleep(6)
		
		time.sleep(5)
		updated_sheet_instance = sheet.get_worksheet(0)
		updated_records_data = updated_sheet_instance.get_all_records()

		if (updated_records_data[row-2]['url']):
			for handle in driver.window_handles:
				driver.switch_to.window(handle)
				driver.close()

		row += 1
	else:
		row += 1
		continue


print('Program took ', time.perf_counter() - start_time)
