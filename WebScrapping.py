import requests
from bs4 import BeautifulSoup
import xlsxwriter

URL = "https://www.wilko.com/en-uk/search/?text=wilko"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

quotes = []  # a list to store quotes

table = soup.find('div', attrs={'class': 'product__listing product__grid'})
Products = []
prodlist = []
ptuple = ()
count = 0
for productdetails in table.findAll('div', attrs={'class': 'product-item js-product-data'}):
    product = {}
    Products = []
    product['ProductID'] = str(productdetails.get('data-sku'))
    Products.append(product['ProductID'])
    product['Name'] = str(productdetails.get('data-product-name'))
    Products.append(product['Name'])
    product['Instore'] = str(productdetails.get('data-in-store-only'))
    Products.append(product['Instore'])
    product['stock'] = str(productdetails.get('data-stock-level-status-code'))
    Products.append(product['stock'])
    product['Price'] = str(productdetails.get('data-price'))
    Products.append(product['Price'])
    product['Add_on'] = str(productdetails.get('data-add-on'))
    Products.append(product['Add_on'])
    product['was_price'] = str(productdetails.get('data-was-price-value'))
    Products.append(product['was_price'])
    #    product['was_price_formatted'] = str(productdetails.get('data-was-price-formatted-value'))
    #    Products.append(product['was_price_formatted'])
    # Products.append(product)
    print(product)
    prodlist.append(product)
#    count+=1
#    if(count==5):
#        break


workbook = xlsxwriter.Workbook('ProductData.xlsx')
# By default worksheet names in the spreadsheet will be
# Sheet1, Sheet2 etc., but we can also specify a name.
worksheet = workbook.add_worksheet("PDP")
# Start from the first cell. Rows and
# columns are zero indexed.
row = 0
col = 0
for heading in product.keys():
    worksheet.write(row, col, heading)
    col += 1
# print(prodlist)
row = 1
col = 0
for prod in prodlist:
    col = 0
    for key, coldata in prod.items():
        worksheet.write(row, col, coldata)
        col += 1
    row += 1

workbook.close()