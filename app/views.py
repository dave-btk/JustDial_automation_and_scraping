from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager  # chrome

# from webdriver_manager.firefox import GeckoDriverManager  # firefox

driver = webdriver.Chrome(ChromeDriverManager().install())  # chrome
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())  # firefox

driver.get('https://www.amazon.in/')

# Checking the name of website
assert 'Online' in driver.title
print(driver.title)

# for entering data in search box
item_to_search = "intel i9 11th gen processor"
# item_to_search = "asofnija"
search_box = driver.find_element_by_id('twotabsearchtextbox')
search_box.clear()
search_box.send_keys(item_to_search)
search_box.send_keys(Keys.RETURN)

# for many pages

try:
    pages = driver.find_element_by_class_name('a-pagination')
except:
    pages = 0
if not pages == 0:
    try:
        total_pages = pages.find_elements_by_class_name('a-disabled')
        print(total_pages[-1].text)
        print("")
        total_pages = int(total_pages[-1].text)
    except:
        total_pages = 1

    current_page_url = ""
    final_list = []
    for y in range(1, total_pages + 1):
        print("start------", y)
        print(current_page_url)
        if not y == 1:
            print('working')
            driver.get(current_page_url)
        items = driver.find_elements_by_class_name('s-asin')
        item_list = []
        for x in items:
            # print(x.text)
            print("image_url :", x.find_element_by_class_name('s-image').get_attribute('src'))
            print("product name :", x.find_element_by_tag_name('h2').text)

            try:
                price = x.find_element_by_class_name('a-price-whole').text
            except:
                price = "NaN"
            print("product price(in Rs) :", price)

            try:
                get_by = x.find_element_by_class_name('s-align-children-center').text
            except:
                get_by = "NaN"
            print("Get by :", get_by)

            try:
                rating = x.find_element_by_class_name('a-size-small').text
            except:
                rating = "No reviews"
            print("product reviews :", rating)
            print("----")
            item_dict1 = {
                "image_url": x.find_element_by_class_name('s-image').get_attribute('src'),
                "product name": x.find_element_by_tag_name('h2').text,
                "product price(in Rs)": price,
                "Get by": get_by,
                "product reviews": rating,
            }
            item_list.append(item_dict1)
        print(item_list)
        final_list = final_list + item_list

        pages1 = driver.find_element_by_class_name('a-pagination')
        if not y == 1:
            next_page = pages1.find_elements_by_class_name('a-normal')
            next_page[-1].click()
        else:
            next_page = pages1.find_element_by_class_name('a-normal')
            next_page.click()
        # total_pages = pages1.find_elements_by_class_name('a-disabled')
        # print(total_pages[-1].text)
        # # print(next_page.text)

        print(driver.current_url)
        current_page_url = driver.current_url
        print("end----------------")
    print("final---", final_list)
# for 2 or less pages


# extraction code


# items = driver.find_elements_by_class_name('s-asin')
# for x in items:
#     # print(x.text)
#     print("image_url :", x.find_element_by_class_name('s-image').get_attribute('src'))
#     print("product name :", x.find_element_by_tag_name('h2').text)
#
#     try:
#         price = x.find_element_by_class_name('a-price-whole').text
#     except:
#         price = "NaN"
#     print("product price(in Rs) :", price)
#
#     try:
#         get_by = x.find_element_by_class_name('s-align-children-center').text
#     except:
#         get_by = "NaN"
#     print("Get by :", get_by)
#
#     try:
#         rating = x.find_element_by_class_name('a-size-small').text
#     except:
#         rating = "No reviews"
#     print("product reviews :", rating)
#     print("----")
#
# pages = driver.find_element_by_class_name('a-pagination')
# next_page = pages.find_element_by_class_name('a-normal')
# total_pages = pages.find_elements_by_class_name('a-disabled')
# print(total_pages[-1].text)
# # print(next_page.text)
# next_page.click()


# driver.implicitly_wait(0.4)
# time.sleep(1)

# print(driver.current_url)
# driver.close()
