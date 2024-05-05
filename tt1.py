from bs4 import BeautifulSoup
import numpy as np

def get_required_values(file_path):
    soup = BeautifulSoup(open(file_path), "html.parser")

    listing_name = None
    listing_price = np.NaN
    listing_picture_url = None
    product_details = None
    name_of_seller = None
    is_trusted_supplier = False
    product_rating = np.NaN

    ans = {"Lisiting Name": listing_name, 
           "Lisiting Price": listing_price,
           "Lisiting Picture URL": listing_picture_url,
           "Product Details": product_details,
           "Name of the Seller": name_of_seller,
           "Is Trusted Supplier": is_trusted_supplier,
           "Product Rating": product_rating
          }

    # GET Listing Name
    listing_name_list = soup.select('span.Text__StyledText-oo0kvp-0.gpVzIL')
    if listing_name_list:
        listing_name = listing_name_list[0].text.strip()

    # GET Listing Price
    listing_price_list = soup.select('h4.Text__StyledText-oo0kvp-0.fka-Dwo')
    if listing_price_list:
        listing_price = listing_price_list[0].text.strip().strip("₹")

    # GET Listing Picture URL
    listing_picture_url_list = soup.find_all('div', class_="ProductDesktopImage__ImageWrapperDesktop-sc-8sgxcr-0 darDKL")
    for div in listing_picture_url_list:
        picture = div.find('picture')
        if picture:
            sources = picture.find_all('source')
            for source in sources:
                listing_picture_url = source.get('srcset')
    
    # GET Product Details
    product_details_list = soup.find('div', class_="Card__BaseCard-b3n78k-0 WvMul ProductDescription__DetailsCardStyled-sc-1tmqkzf-0 eHfqpm ProductDescription__DetailsCardStyled-sc-1tmqkzf-0 eHfqpm")
    if product_details_list:
        paragraphs = product_details_list.find_all('p')
        for paragraph in paragraphs:
            product_details = paragraph.text.strip()

    # GET Name of the Seller
    name_of_seller_list = soup.find('span', class_="Text__StyledText-oo0kvp-0 fFihtW ShopCardstyled__ShopName-du9pku-6 gdULmH ShopCardstyled__ShopName-du9pku-6 gdULmH")
    if name_of_seller_list:
        name_of_seller = name_of_seller_list[0].text.strip()
    
    # GET Trusted Supplier or not
    is_trusted_supplier_list = soup.find('div', class_="Card__BaseCard-b3n78k-0 iRtiAW ShopCardstyled__ShopCardWrapper-du9pku-1 kCgmDc ShopCardstyled__ShopCardWrapper-du9pku-1 kCgmDc")
    if is_trusted_supplier_list:
        inner_div = is_trusted_supplier_list.find('div', class_="ShopCardstyled__MTrustedBadge-du9pku-10 brgtMn")
        if inner_div:
            is_trusted_supplier = True
    

    # GET Product Ratings - Star
    product_rating_list = soup.find('span', class_="Text__StyledText-oo0kvp-0 tQNiu")
    if product_rating_list:
        product_rating = product_rating_list[0].text.strip()

    

    return {"Lisiting Name": listing_name, 
           "Lisiting Price": listing_price,
           "Lisiting Picture URL": listing_picture_url,
           "Product Details": product_details,
           "Name of the Seller": name_of_seller,
           "Is Trusted Supplier": is_trusted_supplier,
           "Product Rating": product_rating
          }

