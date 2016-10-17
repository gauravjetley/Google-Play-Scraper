from selenium import webdriver
chrome_path = r"C:\Users\Gaurav Jetley\Documents\Selenium\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)

#Getting the Titles of all VR Games
driver.get("https://play.google.com/store/search?q=VR&c=apps&docType=1&sp=CAFiBAoCVlJ6BRgAwAECigECCAE%3D:S:ANO1ljK5bfA")
links = driver.find_elements_by_class_name("details")
Attributes("href")
for link in links:
    print(link.text)

#Getting the URLs of all VR Games
vr_links_list = open('C:/Users/Gaurav Jetley/Documents/Selenium/Google Play Scraper/vr_links_list.txt','w')
for link in driver.find_elements_by_class_name("title"):
    print>>vr_links_list, link.get_attribute("href")
vr_links_list.close()
