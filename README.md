# Retail Pricing Module <img src='https://www.inderdhillon.com/files/logo-gray.png' width=100 align='right'>
>Inder Dhillon <br>
>inderdhillon.com <br>

### Description:
Basic program with a GUI to pull up prices from a given retail website using BeautifulSoup. Currently modelled after factorydirect.ca but easily applicable to other websites.


##### Example:
![example](https://inderdhillon.com/files/projects/project5.png)

### Overview:
When I was working at _Factory Direct_ we had to pull up prices by searching the website for product name. The sales associates had no way of pulling up the prices using the barcodes of the products. I created this module to solve that problem for our location.

##### Modules used:
tkinter: Making the GUI<br>
BeautifulSoup: Getting particular tags from the html text<br>
lxml: Faster parsing for BeautifulSoup for my test case<br>
requests: Get the html text for the website
