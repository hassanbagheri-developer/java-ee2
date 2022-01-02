from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select



op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

# driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
driver.get('http://demo.guru99.com/test/upload/')
btn_upload = driver.find_element_by_id("uploadfile_0")
btn_upload.send_keys('C:\\test.txt')












# driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
# driver.get('https://www.varzesh3.com/')
# selector = Select(driver.find_element_by_xpath('//*[@id="widget76"]/div[3]/div[1]/select'))
# selector.select_by_index(2)




# driver.get('https://github.com/')

# driver.find_element_by_partial_link_text('Sign in').click()
# # time.sleep(5)

# username = driver.find_element_by_xpath('//*[@id="login_field"]')
# username.send_keys('usernaem_developer@gmail.com')
# password = driver.find_element_by_xpath('//*[@id="password"]')
# password.send_keys('usernaem_developer')

# butm_sign_in = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
# butm_sign_in.click()












# driver.close()
















