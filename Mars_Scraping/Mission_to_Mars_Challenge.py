#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the Mars NASA news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[14]:


df.to_html()


# In[15]:


browser.quit()


# In[16]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)


# In[17]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.class_title')


# In[11]:


slide_elem.find('h2', class_='content_title')


# In[12]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = [{'img_url': 'https://marshemispheres.com/images/full.jpg', 'title': 'Cerberus Hemisphere Enhanced'}, {'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg', 'title': 'Schiaparelli Hemisphere Enhanced'}, {'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg', 'title': 'Syrtis Major Hemisphere Enhanced'}, {'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg', 'title': 'Valles Marineris Hemisphere Enhanced'}]

# 3. Write code to retrieve the image urls and titles for each hemisphere.
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url = f'https://marshemispheres.com/images/{img_url_rel}'
#for img_url in 


# In[13]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[18]:


# 5. Quit the browser
browser.quit()


# In[ ]:




