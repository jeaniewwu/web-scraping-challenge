#!/usr/bin/env python
# coding: utf-8

# In[5]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import pymongo
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[6]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[7]:


url = 'https://redplanetscience.com/'
browser.visit(url)


# In[8]:


html = browser.html
soup = bs(html, 'html.parser')

    


# In[9]:


info = soup.find("div", {"class": "content_title"}).get_text()
print (info)


# In[10]:


content = soup.find("div", {"class": "article_teaser_body"}).get_text()
print (content)


# # NASA Mars News

# # JPL Mars Space Images - Featured Image

# In[11]:


imageurl = 'https://spaceimages-mars.com/'
browser.visit(imageurl)


# In[12]:


figure=browser.find_by_tag('button')[1]


# In[13]:


figure.click()


# In[14]:


html = browser.html
imagesoup = bs(html, 'html.parser')


# In[15]:


image = imagesoup.find("img", class_= "fancybox-image").get('src')
print (image)


# In[16]:


feature_image_url=f"https://spaceimages-mars.com/{image}"
print(feature_image_url)



# In[17]:


mars_facts='https://galaxyfacts-mars.com/'
mars_fact_table=pd.read_html(mars_facts)
df = mars_fact_table[0]
df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
html_table = df.to_html()
html_table


# In[18]:


astrogeology_url="https://marshemispheres.com/"


# In[19]:


browser.visit(astrogeology_url)
html = browser.html
soup = bs(html, 'html.parser')
main_url = soup.find_all('div', class_='item')
titles=[]
hemisphere_img_urls=[]      







# In[20]:


for img in main_url:
    title = img.find('h3').text
    url = img.find('a')['href']
    hem_img_url= astrogeology_url+url
 
    browser.visit(hem_img_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    hemisphere_img_original= soup.find('div',class_='downloads')
    hemisphere_img_url=hemisphere_img_original.find('a')['href']
    
    print(hemisphere_img_url)
    img_data=dict({'title':title, 'img_url':hemisphere_img_url})
    hemisphere_img_urls.append(img_data)


# In[21]:


hemisphere_img_urls


# In[ ]:




