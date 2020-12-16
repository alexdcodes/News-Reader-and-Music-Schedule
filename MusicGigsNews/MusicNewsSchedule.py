import tkinter as tk
import requests
from bs4 import BeautifulSoup
import urllib.request

window = tk.Tk()
loadeddata = []


def gengui():
    window.geometry("700x500")
    window.title("Music Gig Application")


def body():
    greeting = tk.Label(text="Find your favorite bands live music:")
    greeting.pack()
    window.mainloop()


def grab(thecake):
    global loaddata
    for data in thecake:
        htmlatag = data.find("h2", class_="title").find("a")
        headline = htmlatag.getText()
        url = htmlatag.get("href")
        d = {"headline": headline,
                "url": url}
        loadeddata.append(d)


def getpayload():
    global loadeddata

    payload = "http://www.foxnews.com/"
    page = urllib.request.urlopen(payload)
    r = requests.get(payload)
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    for i in range(0, 15):
        foundmusic = soup.find_all("article", class_="article story-" + str(i))
        grab(foundmusic)


def displayinfo():
    global loadeddata
    print("Data about your favorite bands: \n")
    for i in range(0, len(loadeddata)):
        print(loadeddata[i]["headline"])
        print()
        print(loadeddata[i]['url'])
        ""


if __name__ == '__main__':
    getpayload()
    displayinfo()
    gengui()
    body()

