import sqlite3
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

con = sqlite3.connect('servel.db')
cur = con.cursor()


#This example requires Selenium WebDriver 3.13 or newer
#url5 = 'https://finra-markets.morningstar.com/BondCenter/Results.jsp?debtOrAssetClass=3%2C6&issuerName=&traceOrCusipOrBloomberg=151191AZ6&state=&cusipOrFinraSymbol=&cusipOrFinraSymbol=&cusipOrFinraSymbol=&cusipOrFinraSymbol=&showResultsAs=T&spdsType=&treasuryOrAgencyType=&subProductType=&debtInstrumentType=&debtInstrumentType=&securityDescription=&industryGroup=&convertibleflag=&industrySubtype=&sourceOfPayment=&proceedsUse=&issuingAgency=&collateralOrAssetType=&couponType=&detailedCouponType=&couponRate=&couponRate=&interestFrequency=&interestFrequency=&interestType=&maturityDate=&maturityDate=&moodysRating=&moodysRating=&standardAndPoorsRating=&standardAndPoorsRating=&traceInvestmentGrade=&beginningOrNextCallDate=&beginningOrNextCallDate=&poolNumber=&masterDealId=&trancheId=&tradeDate=&tradeDate=&tradeYield=&tradeYield=&tradePrice=&tradePrice=&agency=&productDescription=&couponRate=&maturityCode=&settlementMonth=&tradeDate=&tradeDate=&productType=&amortizationType=&maturity=&maturity=&coupon=&coupon=&weightedAverageCoupon=&weightedAverageCoupon=&weightedAverageMaturity=&weightedAverageMaturity=&weightedAverageLoan=&weightedAverageLoan=&averageLoanSize=&averageLoanSize=&loanToValueRatio=&loanToValueRatio=&tradeDate=&tradeDate=&SubProductType=ABS&issuerName=&subProductAssetDescription=&rule144aindicator=&couponType=&couponRate=&couponRate=&maturityDate=&maturityDate=&moodysRating=&moodysRating=&tradeDate=&tradeDate=&tradePrice=&tradePrice=&SubProductType=CMO&issuerName=&subProductAssetDescription=&rule144aindicator=&couponType=&couponRate=&couponRate=&maturityDate=&maturityDate=&moodysRating=&moodysRating=&tradeDate=&tradeDate=&tradePrice=&tradePrice=&showAdvancedSearch=hide&postData=%7B%22Keywords%22%3A%5B%7B%22Name%22%3A%22debtOrAssetClass%22%2C%22Value%22%3A%223%2C6%22%7D%2C%7B%22Name%22%3A%22showResultsAs%22%2C%22Value%22%3A%22T%22%7D%2C%7B%22Name%22%3A%22traceOrCusipOrBloomberg%22%2C%22Value%22%3A%22151191AZ6%22%7D%5D%7D'
servel = 'https://www.servelelecciones.cl/'
driver = webdriver.Firefox()
driver.get(servel)
driver.find_element_by_link_text("En Chile").click()
time.sleep(4)
driver.find_element_by_link_text("División Geográfica").click()
comunas = driver.find_element_by_id('selComunas')
objecto_select = Select(comunas)
#hay que llegar hasta el numero 347
for j in range(1,5):
    objecto_select.select_by_index(j)
    #WebDriverWait(driver,timeout=30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="divCabecera"]/h5/span[1]')))
    TEXTO_COMUNA ='//*[@id="selComunas"]/option[{}]'.format(j+1) 
    time.sleep(4)
    comuna = driver.find_element_by_xpath(TEXTO_COMUNA).text
    print(comuna)
    print('*****j :',j)
    for i in [4,7,10,13,19,22]:
        print('****i:  ', i)
        XPATH_CANDIDATO = '//table/tbody/tr[{}][@class="nivelDos ng-scope"]/td[1]/small/span'.format(i)
        XPATH_VOTOS = '//table/tbody/tr[{}][@class="nivelDos ng-scope"]/td[3]/small/span'.format(i)
        XPATH_PORCENTAJE = '//table/tbody/tr[{}][@class="nivelDos ng-scope"]/td[4]/small/span'.format(i)
        candidato = driver.find_element_by_xpath(XPATH_CANDIDATO).text
        votos = driver.find_element_by_xpath(XPATH_VOTOS).text
        votos = votos.replace('.','')
        porcentaje = driver.find_element_by_xpath(XPATH_PORCENTAJE).text
        porcentaje = porcentaje.replace('%','')
        porcentaje = porcentaje.replace(',','.')
        print(candidato)
        print(votos)
        print(porcentaje)
        cur.execute("INSERT INTO primarias VALUES(?,?,?,?)",(comuna,candidato,votos,porcentaje))
        con.commit()

con.close()
driver.close()

