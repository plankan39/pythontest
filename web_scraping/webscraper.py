from selenium import webdriver

url = 'https://www.youtube.com/kallehallden/videos'
browser = webdriver.Chrome()

browser.get(url)

browser.find_element_by_xpath('//*[@id="thumbnail"]').click()
