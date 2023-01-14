from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from datetime import datetime as time, timezone as tz

import time as clock
import pandas as pd
from os.path import exists

def get_quotation():

	options = Options()
	options.headless = True
		
	browser = webdriver.Chrome(options=options)
	browser.get('https://www.google.com/search?q=bitcoin+hoje+dolar')

	btc = '//*[@id="crypto-updatable_2"]/div[3]/div[2]/span[1]'

	quotation = browser.find_element('xpath',btc).text.replace('.','').replace(',','.')

	return float(quotation)


flag = -1
quotation = -1
q = -1

while True:

	utc_time = time.now(tz.utc)

	h, m = map(int, utc_time.strftime("%H,%M").split(','))

	d = int(utc_time.strftime("%d"))
	
	if m % 5 == 0 and m != flag:
		
		if quotation == q:
			clock.sleep(10)
			q = get_quotation()	

		if quotation != q:			
			quotation = q
		else:
			quotation = quotation

		if quotation == q:

			flag = m			

			data = {
				'DIA': [d],
			    'HORA': [h],
			    'MINUTO': [m],
			    'COTACAO': [quotation]
			}

			df = pd.DataFrame(data)

			file = 'btc.csv'

			if (exists(file)):
				df.to_csv(file, mode='a', index=False, header=False)
			else:
				df.to_csv(file, index=False, header=["DIA","HORA","MINUTO","COTACAO"])

			print("SUCCESS!",h,m,quotation)

