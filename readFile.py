fp=open("vr_links_list.txt")
lines=fp.readlines()
fp.close()

for line in lines:
  try:
    #new you have each url in each line
    #Getting Data from VR Games URLs
    driver.get(line)

    ##Description
    description = driver.find_element_by_xpath("//div[@jsname='C4s9Ed']")
    description.text

    ##App Title
    app_title = driver.find_element_by_class_name("id-app-title")
    app_title.text

    #App Subtitle
    app_subtitle = driver.find_element_by_xpath("//a[@class='document-subtitle primary']")
    app_subtitle.text
    
    #App Category
    app_category = driver.find_element_by_xpath("//a[@class='document-subtitle category']")
    app_category.text

    #Rating Count
    rating_count = driver.find_element_by_class_name("rating-count")
    rating_count.text

    #Content Rating
    content_rating = driver.find_element_by_xpath("//span[@class='document-subtitle content-rating-title']")
    content_rating.text

    #Score
    score = driver.find_element_by_xpath("//div[@class='score']")
    score.text

    #Rating Histogram
    rating_histogram = driver.find_element_by_xpath("//div[@class='rating-histogram']")
    rating_histogram.text

    #Details
    details = driver.find_elements_by_class_name("meta-info")
    for d in details:
      print d.text
  except:
    pass
