#!/usr/bin/env python
# coding: utf-8

# In[1]:


# BAX 422 HW-2
# Group 7
# Michael Chen, Rebecca Driever, Rayna Ji


# In[2]:


## PART A ## 
# Use eBay URL, and fetch eBay's search result page for "samsung tv". 
# Save the result to a file. Name the file as "ebay_samsung_tv_01.htm"


# In[3]:


# import necessary packages
from bs4 import BeautifulSoup
import requests
import time


# In[4]:


# set URL 
URL = "https://www.ebay.com/sch/samsumg+tv"
# get html code
r = requests.get(URL, headers={'user-agent': 'Mozilla/5.0'})


# In[6]:


# create file and save html code to it
with open("ebay_samsung_tv_01.htm", "w") as file:
    file.write(str(r.text))


# In[7]:


## PART B ##
# Write a loop to download the first 10 pages of search results. 
# Save each of these pages and name it as required. 
# Each request is paused by 10 seconds.


# In[9]:


# set page number to start at 2 since we already have first page
pgn = 2
# we only want first 10 pages
while pgn <= 10:
    # the pgn variable in the url is all that changes
    url = 'https://www.ebay.com/sch/i.html?_nkw=samsung+tv'+'&_pgn='+str(pgn)
    # get html content for each page
    response = requests.get(url, headers = {'user-agent': 'Mozilla/5.0'})
    # if page 10, no need for leading 0 in page number
    if pgn == 10:
        with open("ebay_samsung_tv_"+str(pgn)+".htm", "w") as file:
            file.write(str(response.text))
    # if page 1-9, need a leading 0 in the page number
    else:
        with open("ebay_samsung_tv_0"+str(pgn)+".htm", "w") as file:
            file.write(str(response.text))
    # see that each page was saved
    print("Page "+str(pgn)+" Saved")
    # go to the next page
    pgn+=1
    # pause ten seconds between each request
    time.sleep(10)


# In[ ]:


## PART C ##
# Loop through the pages you downloaded in (b) (i.e. the saved files)
# open and parse them into an internal object of your 
# programming language of choice. 
# The object should allow you to select elements from it. 
# Next, find the sponsored items on each search result page 
# and print their URL to the screen.


# In[10]:


# create new variable for page number
pgn_r = 1
# we only want first 10 pages
while pgn_r <= 10:
    # page 10 was named differently, so need to code differently
    if pgn_r == 10:
        # create soup object from file
        soup_r = BeautifulSoup(open("ebay_samsung_tv_"+str(pgn_r)+".htm"))
        # find each sponsored tv via the header with the specific class tag
        sponsored = soup_r.find_all("h3", class_="s-item__title s-item__title--has-tags")
        # for each sponsored tv on the page, print the link
        for tv in sponsored:
            print(tv.parent['href'])
    else:
        # create soup object from file
        soup_r = BeautifulSoup(open("ebay_samsung_tv_0"+str(pgn_r)+".htm"))
        # find each sponsored tv via the header with the specific class tag
        sponsored = soup_r.find_all("h3", class_="s-item__title s-item__title--has-tags")
        # for each sponsored tv on the page, print the link
        for tv in sponsored:
            print(tv.parent['href'])
    pgn_r+=1

