import requests
from bs4 import BeautifulSoup
import pandas as pd

#url = "https://www.amazon.in/Canon-1500D-Digital-Camera-S18-55/product-reviews/B07BS4TJ43/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber=2"

reviewlist=[]
def get_soup(url):
    response=requests.get(url)
    soup= BeautifulSoup(response.text,'html.parser')
    return soup

def get_reviews(soup): 
    reviews = soup.find_all('div',{'data-hook':'review'})
    try:
        for item in reviews:
            review = {
            'product':soup.title.text.replace('Amazon.in:Customer reviews:','').strip(),
            'title ':item.find('a',{'data-hook':'review-title'}).text.strip(),
            'rating':float(item.find('i',{'data-hook':'review-star-rating'}).text.replace('out of 5 stars','').strip()),
            'body': item.find('span',{'data-hook':'review-body'}).text.strip(),
            }
            reviewlist.append(review)
    except:
        pass
for x in range(1,999):
    soup = get_soup(f'https://www.amazon.in/pTron-Studio-Wireless-Bluetooth-Headphones/product-reviews/B07XL8HFNC/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Getting page:{x}')
    get_reviews(soup) 
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break

df = pd.DataFrame(reviewlist)
df.to_csv('reviews.csv')
print('Madhu.')