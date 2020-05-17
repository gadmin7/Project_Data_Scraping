from selenium import webdriver
import pandas as pd
import time


driver = webdriver.Chrome(r"C:\Users\GAURI TOSHNIWAL\Documents\cosylab\chromedriver.exe")  #replace your chromedriver path
driver.get("https://metahashtags.com/")
time.sleep(5)
search = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/input')

search.send_keys('food')


button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/button')
button.click()
time.sleep(6)
i=1
while True:
    try:
        hastag_text                 =     driver.find_element_by_xpath(f'//*[@id="scrollable-food"]/li[{i}]/div/div[1]/div/div/div[1]/button').text  # select and store hastag
        no_of_post                  =     driver.find_element_by_xpath(f'//*[@id="scrollable-food"]/li[{i}]/div/div[1]/div/div/div[2]/span[1]/span[1]/b').text #select and store no of post for hastag
        no_of_post_publish_per_hour =     driver.find_element_by_xpath(f'//*[@id="scrollable-food"]/li[{i}]/div/div[1]/div/div/div[2]/span[1]/span[2]/b').text #selct and store no. of post per hour for hastag
        avg_likes                   =     driver.find_element_by_xpath(f'//*[@id="scrollable-food"]/li[{i}]/div/div[1]/div/div/div[2]/span[2]/span[1]/b').text #select and store avg. likes on a post
        min_likes                   =     driver.find_element_by_xpath(f'//*[@id="scrollable-food"]/li[{i}]/div/div[1]/div/div/div[2]/span[2]/span[2]/b').text #select and store minimum likes on post
        avg_comment                 =     driver.find_element_by_xpath(f'//*[@id="scrollable-food"]/li[{i}]/div/div[1]/div/div/div[2]/span[3]/span/b').text #select and store no of comments
        i+=1 # increment list element counter
        print(hastag_text," ",no_of_post," ",no_of_post_publish_per_hour," ",avg_likes," ",min_likes," ",avg_comment)


    except selenium.common.exceptions.NoSuchElementException:
        driver.execute_script('window.scrollTo(0, document.getElementById("wrapper-food").scrollHeight);')

    time.sleep(2)

driver.close()

#//*[@id="scrollable-food"]/li[2]




# /html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/ul/li[1]/div/div[1]/div/div/div[1]/button
# /html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/ul/li[2]/div/div[1]/div/div/div[1]/button
