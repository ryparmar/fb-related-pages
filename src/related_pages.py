#!/usr/bin/env python3
import logging
import datetime
import copy
import argparse
import os, sys

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

### Basic script for scraping related pages of initial links. Related pages is dynamic part of FB page which
### is showed (not neccessarily, some pages have turned off this feature) after liking the page.
### Script enables to scrape also related pages of related pages of initial links -- set in_depth parameter to True
### After processing of each page the data are saved. After cca 50 pages FB starts to show notification -- you liked too many pages
### this notification can be ignored as the scraping is still working, but after another cca 30-50 pages different notification occure
### and further scraping is not possible. After a few days it is possible to scrape again.
### 
### Initially, I was not sure that page shows the same related pages at every visit, so it would more efficient to keep info
### whether the page has been processed already and if so, dont repeat the visit.


# Return list with related pages
def get_related(driver, printout=False):
    related = driver.find_elements_by_tag_name('a')
    related_pages = []
    for r in related:
        try:
            if r.get_attribute('aria-label') == 'Profile picture':
                related_pages.append(str(r.get_attribute('href')))
                if printout:
                    print(r.get_attribute('href'))
        except:
            logging.error("Selenium: get_attribute error in get_related function! The label might not exist.")
    return related_pages

# Save crawled data into file
def save(file, link, related):
    logging.info(f'Saving {link} into file.')
    if not related:
        logging.info(f"Missing related pages for {link}")
    
    with open(file, 'a') as f:
        f.write((link + ";" + ";".join(related) + '\n'))


if __name__ == '__main__':

    # Parse arguments
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('--links', default='links', type=str, help='path to the file with the initial links')
    parser.add_argument('--in_depth', default=False, type=str, help='if True, script will crawl also related pages of related pages')
    args = parser.parse_args()

    # Logging
    logging.basicConfig(filename='log', level=logging.INFO)
    start = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    outfile = 'data-' + start + '.csv'
    logging.info(f"Started at {start}")

    # Read the file with initial links
    INITIAL_LINKS = []
    if os.path.exists(args.links):
        with open(args.links, 'r') as f:
            for link in f.readlines():
                INITIAL_LINKS.append(link.strip())
    else:
        print("File with links does not exist!")
        sys.exit(0)

    # Set up Chrome session with Selenium webdriver
    driver = webdriver.Chrome(executable_path='/home/spaceape/chromedriver/chromedriver')
    driver.get('https://www.facebook.com/')
    sleep(1)

    # Set up the login data
    usr = input('Enter Email:')
    pwd = input('Enter Password:')
    if usr and pwd:
        logging.info('Login data received') 

        # Login to FB
        username_box = driver.find_element_by_id('email')
        username_box.send_keys(usr)
        sleep(1)

        password_box = driver.find_element_by_id('pass')
        password_box.send_keys(pwd)
        sleep(1)

        login_box = driver.find_element_by_name('login')
        login_box.click()
        sleep(10)
        logging.info('Logged to FB')

        # Crawl the pages and save their related pages
        crawled_links = copy.deepcopy(INITIAL_LINKS)
        for c, link in enumerate(crawled_links):
            sys.stdout.write('\r{}/{}  {}'.format(c, len(crawled_links), link))
            # print(f"Link {c}/{len(crawled_links)}")
            driver.get(link)
            sleep(3)

            divs = driver.find_elements_by_tag_name('div')
            for div in divs:
                try:
                    if div.get_attribute('aria-label') == 'Liked':  # page already liked
                        div.click()  # unlike
                        sleep(2)
                        div.click()  # like in order to see the offered pages
                        sleep(2)
                        
                        save(outfile, link, get_related(driver))  # save related pages of given link in the outfile

                        # append links to pages related to the initial pages
                        if args.in_depth and link in INITIAL_LINKS and c <= len(INITIAL_LINKS):
                            crawled_links += related #PAGES[link]
                            logging.info(f"{link} -- related added. Currently {len(crawled_links)} links")
                        sleep(2)
                        break  # stop - the desired 'Liked' button is listed as the first div which satisfy the if/elif condition
                        
                    elif div.get_attribute('aria-label') == 'Like':  # page not yet liked
                        div.click()  # like in order to see the offered pages
                        sleep(2)

                        save(outfile, link, get_related(driver))  # save related pages of given link in the outfile
                        if div.get_attribute('aria-label') == 'Liked':
                            div.click()  # unlike again

                        # append links to pages related to the initial pages
                        if args.in_depth and link in INITIAL_LINKS and c <= len(INITIAL_LINKS):
                            crawled_links += related #PAGES[link]
                            logging.info(f"{link} -- related added. Currently {len(crawled_links)} links")
                        sleep(2)
                        break  # stop - the desired 'Liked' button is listed as the first div which satisfy the if/elif condition
                except:
                    continue
                    # logging.error("Selenium: get_attribute error in the main! The label might not exist.")        

        logging.info('Finished')
        driver.quit()

    else:
        logging.error('Missing login data')
        driver.quit()
