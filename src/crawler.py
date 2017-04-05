import requests
from bs4 import BeautifulSoup
import time

totalCarsScrapped = 0 # Python's indexing starts at zero
## Looping two links...
for url_page in range(1, 3):
    # print url_page

    websiteUrl = "https://www.nettiauto.com/en/vaihtoautot?page=" + repr(url_page)
    print repr("Scrapping ") + websiteUrl
    reqToWeb = requests.get(websiteUrl)

    # Get HTTP content
    # reqToWeb.content

    # HTML object
    soup = BeautifulSoup(reqToWeb.content)

    # Easy to read code
    # print soup.prettify()

    allCars = soup.find_all("div", {"class", "listingVifUrl"})
    # for index, car_item in enumerate(allCars, start=0):
        # print(index, item)

    for car in allCars:
        div_widthFull = car.find_all("div", {"class", "width_full"})[0]
        carItem = div_widthFull.find_all("div", {"class", "data_box"})[0]

        car_model = carItem.find_all("div", {"class", "make_model_link"})[0].text
        print repr("Model -> ") + car_model

        car_more_data = carItem.find_all("div", {"class", "clearfix_nett"})[0]
        price = car_more_data.find_all("div", {"class", "price_block"})[0].find_all("div", {"class", "main_price"})[0].text
        print repr("Price -> ") + price

        car_localization = car_more_data.find_all("div", {"class", "info_block"})[0].find_all("div", {"class", "location_info cleafix_nett"})[0].find_all("span", {"class", "list_seller_info"})[0].find_all("b", {"class", "gray_text"})[0].text
        print repr("Location -> ") + car_localization

        car_specs = car_more_data.find_all("div", {"class", "info_block"})[0].find_all("div", {"class", "vehicle_other_info clearfix_nett"})[0].find_all("ul")[0]
        # car_year = car_specs car_specs.contents[1].text
        #car_mileage = car_specs.contents[3].text
        #car_combustion_type = car_specs.contents[5].text
        #car_gear_mode = car_specs.contents[6].text
        #print repr("Year ") + car_year + repr(" mileage ") + car_mileage + repr(" type ") + car_combustion_type + repr(" mode ") + car_gear_mode
        print car_specs.contents
        totalCarsScrapped += 1

    print repr("Stopping thread 3 secs")
    time.sleep(3)  # delays for 3 seconds
    print repr("Resuming thread")

print repr("Total cars scrapped ") + repr(totalCarsScrapped)