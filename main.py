from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "covid_1.ico",
        timeout = 6
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        # notifyMe("Abhishek","Lets stop the spread of the virus together")
        myHtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDatastr = ""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            myDatastr += tr.get_text()
        myDatastr = myDatastr[1:]

        itemList = myDatastr.split('\n\n')

        states = ['Uttar Pradesh','Maharashtra','Bihar']
        for item in itemList[0:23]:
            dataList = item.split('\n')
            
            if dataList[1] in states:
                # print(dataList)
                nTitle = 'Cases of Covid-19'
                nText = f"State {dataList[1]} \nIndian : {dataList[2]} Foreign : {dataList[3]} \nCured : {dataList[4]} \nDeaths : {dataList[4]}"
                notifyMe(nTitle,nText)
                time.sleep(2)
        time.sleep(1800)

    


    #print(myHtmlData)