#RUN THIS FIRST
import os
from selenium import webdriver
chrome_path = r"C:\Users\ThinkPad\Downloads\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)


fp=open("vr_links_list.txt")
lines=fp.readlines()
fp.close()

for line in lines:
	try:
		driver.get(line)
		line=line.split('\n')[0]
		line=line.split('=')[1]
		#new you have each url in each line
		#Getting Data from VR Games URLs
		
		os.mkdir(line)

		##Description
		description = driver.find_element_by_xpath("//div[@jsname='C4s9Ed']")
		description=description.text.encode('utf-8')
		#data=data+'\''+'description'+'\''+':'+'\''+description+'\''
		fp1=open(line+'/description.txt','w')
		fp1.write(str(description))
		fp1.close()
	

		##App Title
		app_title = driver.find_element_by_class_name("id-app-title")
		title=app_title.text
		fp1=open(line+'/title.txt','w')
		fp1.write(str(title))
		fp1.close()


		#App Subtitle
		app_subtitle = driver.find_element_by_xpath("//a[@class='document-subtitle primary']")
		subtitle=app_subtitle.text
		fp1=open(line+'/subtitle.txt','w')
		fp1.write(str(subtitle))
		fp1.close()
    
		#App Category
		app_category = driver.find_element_by_xpath("//a[@class='document-subtitle category']")
		category=app_category.text
		fp1=open(line+'/category.txt','w')
		fp1.write(str(category))
		fp1.close()

		#Rating Count
		rating_count = driver.find_element_by_class_name("rating-count")
		rating=rating_count.text
		fp1=open(line+'/rating.txt','w')
		fp1.write(str(rating))
		fp1.close()

		#Content Rating
		content_rating = driver.find_element_by_xpath("//span[@class='document-subtitle content-rating-title']")
		content_rating=content_rating.text
		fp1=open(line+'/content_rating.txt','w')
		fp1.write(str(content_rating))
		fp1.close()

		#Score
		score = driver.find_element_by_xpath("//div[@class='score']")
		score=score.text
		fp1=open(line+'/score.txt','w')
		fp1.write(str(score))
		fp1.close()


		#Rating Histogram
		rating_histogram = driver.find_element_by_xpath("//div[@class='rating-histogram']")
		hist=rating_histogram.text
		fp1=open(line+'/hist.txt','w')
		fp1.write(str(hist))
		fp1.close()


		#Details
		details = driver.find_elements_by_class_name("meta-info")
		fp1=open(line+'/details.txt','a')
		for d in details:
			print (d.text)
			fp1.write(str(d.text))
		fp1.close()
	except:
		pass
