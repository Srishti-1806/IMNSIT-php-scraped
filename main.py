import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://imsnsit.org/imsnsit/tender_notifications.php"

page = requests.get(url)

soup=BeautifulSoup(page.text,"html.parser")
#print(soup.prettify)
data=(soup.find_all("b"))     #yaar ye toh list haiiiiiii........hahahahhahhaha

'''a=(data.__sizeof__())
for i in range(0,a):
    print(data[i])'''

tableOfTitles= [title.text for title in data]
df = pd.DataFrame(columns=tableOfTitles)
df = df.drop(df.columns[0], axis=1)
  

data2=soup.find_all("tr")

for i in data2[2:]:
    row_data= i.find_all("td")
    individual_data=[data2.text for data2 in row_data]
    if individual_data==['']:
        continue
    else:
        length=len(df)
        df.loc[length]= individual_data
        df.to_csv( r'C:\Users\DINESH KUMAR\Desktop\imnsit\data.csv')
        