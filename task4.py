'''
The Finnish Patent and Registration Office (PRH) offers an open API, where you can access information about public companies 
in Finland. A guide for accessing this API can be found here: https://avoindata.prh.fi/index_en.html, 
and more specifically https://avoindata.prh.fi/tr_en.html. 
Get familiar with the given API, and implement a Python program that is capable of answering these questions:

How many limited companies (companyForm==OY) have been registered to the municipality of Ylitornio 
(registeredOffice==Ylitornio) after the date 1978-3-14? 
How many of them have ceased to exist?
Similarly as above, what is the amount of registered and the amount of ceased limited companies for the municipality 
of Merikarvia? How about for Parikkala?
The program should utilize the open PRH API and print a report that features answers for these questions.

'''

import requests

# Looping through all three municipality url
for municipality_name in ['Ylitornio', 'Merikarvia','Parikkala']:
    base_url = 'https://avoindata.prh.fi/tr/v1?totalResults=true&registeredOffice={}&companyForm=OY&companyRegistrationFrom=1978-03-14'.format(municipality_name)
    #print(base_url)
    res = requests.get(base_url)
    data = res.json()
    print('The no. of companies with OY in',municipality_name ,':', data['totalResults'])
    


# Finding cease companies in there municipalities
for municipality_name in ['Ylitornio', 'Merikarvia','Parikkala']:
    ceased_url = 'https://avoindata.prh.fi/tr/v1/publicnotices?totalResults=true&resultsFrom=0&registeredOffice={}&noticeRegistrationFrom=1978-03-14&noticeRegistrationType=END'.format(municipality_name)
    response = requests.get(ceased_url)
    data2 = response.json()
    print('Ceased  companies in ',municipality_name ,':', data2['totalResults'])


