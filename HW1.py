#Rebecca Driever, Alayna Myrick, Jacqueleine Ngo, Ana Parra Vera

### practice with regular expressions and web-scraping

#load relevant packages
import re
import bs4 as bs
import requests
#input file path to mock data
file_name = 'mock_data.csv'

## transform birthday column from European (DD/MM/YYYY) to US date format (MM/DD YYYY)

open_file = open(file_name,'r')
#compile the birthday pattern
pattern = re.compile(r'([0-9]{2})\.([0-9]{2})\.(20[0-9]{2})')
for line in open_file:
    #reorder the birthday using groups
    new_line = pattern.sub(r'\2/\1 \3',line)
    print(new_line)
open_file.close()

## strip everything except the email column

open_file = open(file_name,'r')
#compile the email pattern
pattern = re.compile(r'.*?,([-A-Za-z.]+@[-A-Za-z.]+).*')
for line in open_file:
    #reorder the email using groups
    new_line = pattern.sub(r'\1',line)
    print(new_line)
open_file.close()

## convert all rows to "name[TAB]birthday" and strip the rest. birthday column should be in US date format. TABs allow you to copy and paste results into excel.

open_file = open(file_name,'r')
#compile the patterns
pattern = re.compile(r'([0-9]{2})\.([0-9]{2})\.(20[0-9]{2}).*?([A-Za-z]+ [A-Z]\. [A-Za-z]+).*')
for line in open_file:
    #reorder name and birthday
    new_line = pattern.sub(r'\4\t\2/\1 \3',line)
    print(new_line)
open_file.close()

## strip everything excepy lat_long and reorder entries to be "long[TAB]lat"

open_file = open(file_name,'r')
#compile the lat/long pattern
pattern = re.compile(r'.*"(-?[0-9]+\.[0-9]+), (-?[0-9]+\.[0-9]+)".*')
for line in open_file:
    #reorder the lat/long using groups
    new_line = pattern.sub(r'\2\t\1',line)
    print(new_line)
open_file.close()


## find US news top stories, read & print the URL of the second current top story to the screen. navigate to the webpage of the second top story, and print header as well as first 3 sentences of the main body to the screen

#input original url
url='https://www.usnews.com/'
#create user credentials (avoid 403 error)
headers = {
    'User-Agent': 'Mozilla/5.0',
}
#receive response
response = requests.get(url, headers=headers)

#convert response to "soup" object to allow html parsing
soup = bs.BeautifulSoup(response.text,'html.parser')

#find the top stories from the home page based on the class name
mydivs = soup.findAll("div", {"class": "ArmRestTopStories__CollapseBorderContentBox-s1vkad-0 kkieLV s85n6m5-0-Box-cwadsP fHRMIQ"})

#Find all a tags of the second top story
links = mydivs[1].findAll('a')

#find the link to the second top story
new_url = links[0].get('href')

#open the new link to the second top story
response2 = requests.get(new_url, headers=headers)

#convert the second top story page to a soup object
soup2 = bs.BeautifulSoup(response2.text,'html.parser')

#find the header
header = soup2.findAll("h1")[0].text

#find the body text
paragraphs = soup2.findAll('div', {"class": "Raw-s14xcvr1-0 AXWJq"})

#combine all body text into one string
all_text = ''
for p in paragraphs:
    all_text = all_text + p.text

#split the created string  into sentences
sentences = all_text.split('.')

#print the header and first three sentences of second top story
print(header)
for sentence in sentences[0:3]:
    print(sentence)
