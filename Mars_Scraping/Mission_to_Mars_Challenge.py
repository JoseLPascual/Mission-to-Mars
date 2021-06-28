# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    hemisphere_image_urls = []

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data

# Visit the Mars NASA news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.class_title')

slide_elem.find('h2', class_='content_title')

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = [{'img_url': 'https://marshemispheres.com/images/full.jpg', 'title': 'Cerberus Hemisphere Enhanced'}, {'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg', 'title': 'Schiaparelli Hemisphere Enhanced'}, {'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg', 'title': 'Syrtis Major Hemisphere Enhanced'}, {'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg', 'title': 'Valles Marineris Hemisphere Enhanced'}]

# 3. Write code to retrieve the image urls and titles for each hemisphere.
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url = f'https://marshemispheres.com/images/{img_url_rel}'
#for img_url in 

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls