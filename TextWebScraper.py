from selenium import webdriver
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def MicroCenter():
    search = str(input("What would you like to search: "))
    if " " in search:
        search = search.replace(" ", "+")

    my_url = 'https://www.microcenter.com/search/search_results.aspx?NTT= &NTK=all&page=1'
    my_url = my_url.replace(" ", f"{search}")

    page = 1
    for i in range (5):
        my_url = my_url.replace("page="f"{page-1}", "page="f"{page}")
        print("Showing results from page " + str(page))
        page += 1
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        containers = page_soup.findAll("li", {"class":"product_wrapper"})
        container = containers[0]

        print("\n")
        for container in containers:
            brand_container = container.findAll("a")
            brand = brand_container[1]["data-brand"]
            product_name = brand_container[3].text
            price_container = container.findAll("span", {"itemprop":"price"})
            price = price_container[0].text

            print("Brand:", brand)
            print("Product Name:", product_name)
            print("Price:", price)
            print("\n")

def Newegg():
    search = str(input("What would you like to search: "))
    if " " in search:
        search = search.replace(" ", "+")

    my_url = 'https://www.newegg.ca/p/pl?d= &page=1'
    my_url = my_url.replace(" ", f"{search}")


    page = 1
    for i in range (5):
        my_url = my_url.replace("page="f"{page-1}", "page="f"{page}")
        print("Showing results from page " + str(page))
        page = page + 1

        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        containers = page_soup.findAll("div", {"class":"item-cell"})
        container = containers[0]

        print("\n")
        for container in containers:
            product_name = container.img["title"]
            price_container = container.findAll("li", {"class", "price-current"})
            price = price_container[0].text.replace("\xa0", "")
            shipping_container = container.findAll("li", {"class", "price-ship"})
            shipping_cost = shipping_container[0].text

            print("Product Name:", product_name)
            print("Price:", price)
            print("Shipping Cost:", shipping_cost)
            print("\n")

def Staples():
    search = str(input("What would you like to search: "))
    if " " in search:
        search = search.replace(" ", "+")


    my_url = 'https://www.staples.ca/search?query= &indices%5Bshopify_products%5D%5Bpage%5D=1'
    my_url = my_url.replace(" ", f"{search}")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options)
    driver.create_options()

    x = 1
    page = 1

    for i in range (5):
        my_url = my_url.replace("page%5D="f"{page-1}", "page%5D="f"{page}")
        print("Showing results from page " + str(page))
        driver.get(my_url)
        products = driver.find_elements_by_class_name('ais-hits--item')
        page = page + 1
        print("\n")
        
        for product in products:
            titles = '//*[@id="alogolia-index-tabpanel-0"]/div/div[2]/div[3]/div/div['+ str(x) + ']/div/div[3]/div[2]/div/a'
            title = product.find_element_by_xpath(titles).text
            prices = '//*[@id="alogolia-index-tabpanel-0"]/div/div[2]/div[3]/div/div[' + str(x) + ']/div/div[4]/div/div[1]/span'
            price = product.find_element_by_xpath(prices).text
            x = x + 1
        
            print("Product Name:", title)
            print("Price:", price)
            print("\n")
        x = 1
    driver.close()

def Visions():
    search = str(input("What would you like to search: "))
    if " " in search:
        search = search.replace(" ", "+")

    my_url = 'https://www.visions.ca/catalogue/category/ProductResults.aspx?px=0&categoryId=0&searchText= '
    my_url = my_url.replace(" ", f"{search}")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options)
    driver.create_options()

    x = 1
    page = 0

    for i in range (5):
        my_url = my_url.replace("px="f"{page-1}", "px%5D="f"{page}")
        print("Showing results from page " + str(page))
        driver.get(my_url)
        products = driver.find_elements_by_class_name('prodlist-itembox')
        page = page + 1
        print("\n")
        
        for product in products:
            title = product.find_element_by_class_name('prodlist-title').text
            price = product.find_element_by_class_name('prodlist-priceinfo-leftbox').text 

            print("Product Name:", title)
            print("Price:", price)
            print("\n")
    driver.close()


def MemoryExpress():
    search = str(input("What would you like to search: "))
    if " " in search:
        search = search.replace(" ", "%20")

    my_url = "https://www.memoryexpress.com/Search/Products?Search= &Page=1"
    my_url = my_url.replace(" ", f"{search}")
    page = 1
    z=0
    for i in range (5):
        my_url = my_url.replace("Page="f"{page-1}", "Page="f"{page}")
        print("Showing results from page " + str(page))
        page = page + 1
        
        uClient = uReq(my_url)
        page_html = uClient.read()
        
        page_soup = soup(page_html, "html.parser")

        containers = page_soup.findAll("div",{"class":"c-shca-icon-item"})
        container = containers[0]
        product_summary =  container.findAll("div",{"class":"c-shca-icon-item__body-name"})
        for container in containers:
            product_summary =  container.findAll("div",{"class":"c-shca-icon-item__body-name"})
            product = product_summary[0].text.strip()
            z+=1
            product_summary =  container.findAll("div",{"class":"c-shca-icon-item__body-name"})
            price_summary = (container.findAll("div",{"class":"c-shca-icon-item__summary-prices"}))
            if len(page_soup.findAll("div",{"class":"c-shca-icon-item c-shca-icon-item--has-sale"})) > 0:
                price_container = container.findAll("div",{"class":"c-shca-icon-item__summary-list"})
                price = price_container[0].span.text.strip()
            else:
                price = price_summary[0].div.text.strip()
                
            print("Product: " + product)
            print("Price :" + price)
            print("\n")
    uClient.close()        
def NewWebsiteLoop():
    print("Welcome to the Webscraper!")
    print("(M)icroCenter\n(N)ewEgg\n(S)taples\n(V)isions Electronics\n(E) Memory Express\n(Q)uit Program")


def main():
    userQuitOption = False
    NewWebsiteLoop()
    userInput = str(input("Please pick a website that you would like to search your product on: "))
    userInput = userInput.capitalize()
    while userQuitOption == False:
        if userInput == "Q":
            userQuitOption = True
        else:    
            while userInput != "M" and userInput != "N" and userInput != "S" and userInput != "V" and userInput != "E":
                userInput = str(input("Please only enter F or M or N or S or V or E: "))
                userInput.capitalize()
                userInput = userInput.capitalize()

            if userInput == "O":
                Source()
                NewWebsiteLoop()
                userInput = str(input("Please pick a website that you would like to search your product on: "))
                userInput = userInput.capitalize()
                
            elif userInput == "M":
                MicroCenter()
                NewWebsiteLoop()
                userInput = str(input("Please pick a website that you would like to search your product on: "))
                userInput = userInput.capitalize()

            elif userInput == "N":
                Newegg()
                NewWebsiteLoop()
                userInput = str(input("Please pick a website that you would like to search your product on: "))
                userInput = userInput.capitalize()

            elif userInput == "S":
                Staples()
                NewWebsiteLoop()
                userInput = str(input("Please pick a website that you would like to search your product on: "))
                userInput = userInput.capitalize()

            elif userInput == "V":
                Visions()
                NewWebsiteLoop()
                userInput = str(input("Please pick a website that you would like to search your product on: "))
                userInput = userInput.capitalize()

            elif userInput == "E":
                MemoryExpress()
                NewWebsiteLoop()
                userInput = str(input("Please pick a website that you would like to search your product on: "))
                userInput = userInput.capitalize()
                    
    print("Exiting Program...")
    print("Thank you for using our program!")
main()

