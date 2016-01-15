import os
import re
import requests
import urllib
import datetime
from lxml import html

categories = ["telefoane-mobile", "tablete", "smartwatches-accesorii",
              "televizoare", "monitoare-lcd-led", "desktop-pc", "laptopuri",
              "componente", "console-hardware", "console-portabile", "jocuri-consola-pc"]

def downloadImage(link, name):
    resource = urllib.urlopen("http://" + link)
    name = re.sub('[^\w\-_\. ]', '_', name)
    name = name.encode('ascii','ignore')
    output = open(name + ".jpg","wb")
    output.write(resource.read())
    output.close()

def saveProductInfoToFile(productName, productPrice):
    name = re.sub('[^\w\-_\. ]', '_', productName)
    name = name.encode('ascii','ignore')
    output = open(name + ".txt", "w")
    output.write(productName.encode('ascii', 'ignore') + '\n')
    output.write(productPrice + '\n')
    output.close()

def getProductInfo(link):
    response = requests.get(link)
    tree = html.fromstring(response.content)
    productName = tree.xpath('//div[@id="offer-title"]/h1/text()')
    productPriceElement = tree.xpath('//div[@class="prices"]/span')
    productImagePathElement = tree.xpath('//a[@class="gallery-image"]')

    if len(productName) != 0:
        productName = productName[0]
        productPrice = productPriceElement[0].attrib['content']
        productImagePath = productImagePathElement[0].attrib['data-original']
        productImagePath = productImagePath[2:]

        print productName + ' ' + productPrice + ' ' + productImagePath

        # save file with product info
        saveProductInfoToFile(productName, productPrice)

        # download the image
        downloadImage(productImagePath, productName)

def getProductsFromCategory(category):
    os.chdir(category)
    lastResponse = requests.get('http://www.emag.ro/' + category + '/p1/c')
    for page_index in range(1, 200):
        print page_index
        response = requests.get('http://www.emag.ro/' + category + '/p' + str(page_index) + '/c')
        tree = html.fromstring(response.content)
        linksToProductsElements = tree.xpath('//a[@class="link_imagine"]')

        if (lastResponse != response):
            lastResponse = response
            for linkToProductElement in linksToProductsElements:
                link = 'http://www.emag.ro' + linkToProductElement.attrib['href']

                # get the product related info
                getProductInfo(link)
        else:
            break
    os.chdir("..")

def main():
    print categories
    for category in categories:
        print category

        startTime = datetime.datetime.now()
        print 'Started gathering info about products in category at: '
        print startTime

        # create a new directory where all the products files will be placed
        if not os.path.exists(category):
            os.makedirs(category)

        getProductsFromCategory(category)

        endTime = datetime.datetime.now()
        print 'Finished gathering info about products in category at: '
        print endTime
        print 'It took: '
        print(endTime - startTime)

if __name__ == '__main__':
    main()