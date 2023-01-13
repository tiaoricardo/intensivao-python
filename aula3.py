from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

browser = webdriver.Chrome()

browser.get('https://www.google.com/')

xinput = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input' 
xdolar = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'

browser.find_element('xpath',xinput).send_keys('cotação dolar')
browser.find_element('xpath',xinput).send_keys(Keys.ENTER)

quotation = browser.find_element('xpath',xdolar).get_attribute('data-value')

print(quotation)

df = pd.read_excel('input/aula3/Produtos.xlsx')

df.loc[df["Moeda"] == 'Dólar', 'Cotação'] = float(quotation)
df['Preço de Compra'] = df['Cotação'] * df['Preço Original']
df['Preço de Venda'] = df['Preço de Compra'] * df['Margem']

df.to_excel('output/aula3/Produtos_novo.xlsx', index=False)

browser.quit()
