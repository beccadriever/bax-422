#!/usr/bin/env python
# coding: utf-8

# In[1]:


# BAX-422 HW3
# Michael Chen, Rebecca Driever, Rayna Ji


# In[2]:


## Part 1: Dealing with Unicode ##


# In[3]:


# import necessary packages
from bs4 import BeautifulSoup
import requests
import re
from collections import Counter


# In[4]:


# a) Write a program that connects to the page:
# https://www.thyssenkrupp-elevator.com/kr/products/multi/


# In[5]:


# define url
url = "https://www.thyssenkrupp-elevator.com/kr/products/multi/"
# submit GET request
request = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})


# In[6]:


# b) Augment your code to save the page to your file system 
# in the same directory as your code script and name it "elevator.htm". 
# Make sure to save it using UTF8 (Unicode).


# In[7]:


# save request text to file
with open("elevator.htm", "w", encoding="utf-8") as file:
    file.write(request.text)


# In[8]:


# c) Open the file (saved in section b) using a STANDARD TEXT EDITOR 
# (make sure it supports Unicode) or open it in a programming language 
# as TXT only.


# In[9]:


# open the saved file
with open("elevator.htm", "r", encoding='utf-8') as file:
    text = file.read()


# In[10]:


# d) Create a single search-and-replace RegEx that strips all <tag>s 
# + run it. If you are using a programming language, 
# print the output to the screen.


# In[11]:


# strip all html tags
text_stripped = re.sub(re.compile('<.*?>'), '', text)
# print output to screen
print(text_stripped)


# In[12]:


# e) Create a single search-and-replace RegEx that grabs 
# the Korean character that occurs right before "." 
# (the end of the sentence). 
# If you are using a programming language, print the output to the screen. 


# In[13]:


# create regex to trim white space
trim_white_space = re.compile(r'\s')
text_stripped = trim_white_space.sub('', text_stripped)


# In[14]:


text_stripped


# In[15]:


# create regex pattern to strip everything not before a period
# or not a Korean character
pattern = re.compile(r'[a-zA-Z\.()\]]*?(.(?!\.))')
new_text = pattern.sub('', text_stripped)
# print result to screen
print(new_text)


# In[16]:


# f) What is the Korean character that occurs the most? 
# Print it to the screen. 


# In[17]:


# get an of characters and their counts and take only first
common_character = Counter(new_text).most_common(1)
# take first list from array
common_character = common_character[0]
# print character to the screen
print(common_character[0])


# In[18]:


## Part2 ##


# In[19]:


# a) Write a program that logs into your account 
# (Hint: you might need to include your cookies. 
# Look into the source code when you log in using your browser 
# and look for your username and info. 
# Is this a GET or POST request? 
# Use this information to help you write your code to log in)


# In[20]:


# navigate to sign-in url
url2 = "https://www.allrecipes.com/account/signin/"
# get html doc
request2 = requests.get(url2, headers={'user-agent': 'Mozilla/5.0'})
# create soup object
soup = BeautifulSoup(request2.content)


# In[21]:


# find sign-in form
form = soup.find("form", {"name": "signinForm"})
# create variable for token since it seems to be variable
csrToken = form.find("input", {"name": "SocialCsrfToken"})['value']
# create data object to fill out form
data = {"ReferringType": "",
        "ReferringUrl": "https://www.allrecipes.com/",
        "ReferringAction": "",
        "ReferringParams": "",
        "AuthLayoutMode": "Standard",
        "SocialCsrfToken": csrToken,
        "txtUserNameOrEmail": "cookforall@yahoo.com",
        "password": "Cookforall",
        }
# submit post request to log in with data, and retrieve html
login_request = requests.post(url2, headers={'user-agent': 'Mozilla/5.0'}, data=data) 


# In[22]:


# b) Verify that you are logged in by "looking for your username" 
# in the HTML response of section (a). 
# Find your username and print it to the screen.


# In[23]:


# create soup object from logged-in html file
soup_loggedin = BeautifulSoup(login_request.content)
# find username
username = soup_loggedin.find("span", class_="username").text
# print username to screen
print(username)

