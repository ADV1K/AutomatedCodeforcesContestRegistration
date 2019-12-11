# A simple script which registers for all the contest available on codeforces while keeping a MAX_CONTESTS limit in mind
import os
import sys
import chromedriver_binary  # Adds chromedriver binary to path

from selenium import webdriver
from selenium.common.exceptions import *


LOGIN_URL = "http://codeforces.com/enter"
CONTESTS_URL = "http://codeforces.com/contests"
MAX_CONTESTS = 2  # join atmost 10 contests and quit


def login(driver, take_screenshot=True):
	"log into codeforces"
	driver.get(LOGIN_URL)
	if "Login into Codeforces" in driver.page_source:
		handleBox = driver.find_element_by_id('handleOrEmail')
		handleBox.send_keys(HANDLE)
		passwordBox = driver.find_element_by_id('password')
		passwordBox.send_keys(PASSWORD)
		submitBtn = driver.find_element_by_xpath('//*[@class="submit"]')
		if take_screenshot:
			driver.save_screenshot("login.png")
		submitBtn.click()


def displayDetails(contest):
	"display contest details"
	values = [e.text for e in contest.find_elements_by_tag_name('td')]
	items = ['name', 'writers', 'start', 'lenght', 'time left', 'registered']
	print('=' * 50)
	for item, value in zip(items, values):
		print(f"{item:15} : {value}")


def register(contest_url, driver, counter=0):  # i is used to take screenshots
	"register for a contest though contest link"
	driver.get(contest_url)
	driver.save_screenshot(f'contest{counter}.png')
	submitBtn = driver.find_element_by_xpath('//*[@class="submit"]')
	submitBtn.click()


def main():
	# chromedriver_path = os.join(os.getcwd(), 'chromedriver.exe')  # chromedriver-binary handles this
	driver = webdriver.Chrome()
	# login into codeforces and take a screenshot
	login(driver, take_screenshot=True)

	# get to the contests page and take a screenshot
	driver.get(CONTESTS_URL)
	driver.save_screenshot('contests.png')

	contest_links = []
	contests = driver.find_elements_by_xpath('//*[@id="pageContent"]/div[1]/div[1]/div[6]/table/tbody/tr')[1:]  # all the contests
	for i, contest in zip(range(MAX_CONTESTS), contests):
		displayDetails(contest)  # display the details to the screen
		try:  # try gettting the contest registratin link
			contest_link = contest.find_element_by_xpath('//*[@class="red-link"]').get_attribute('href')
			contest_links.append(contest_link)
		except NoSuchElementException:  # registration hasn't started yet
			pass

	for i, contest_link in enumerate(contest_links):
		register(contest_link, driver, counter=i)

	driver.quit()


if __name__ == '__main__':
	# raise Exception("why are you so lazy!!! change your username and password in the source and comment this line and then run the script again")
	try:
		HANDLE = sys.argv[1]
		PASSWORD = sys.argv[2]
		main()
	except IndexError:
		print("Usage: python register_contests.py <HANDLE> <PASSWORD>")
