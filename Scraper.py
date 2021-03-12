from bs4 import BeautifulSoup
import requests
import lxml


def elon_news():
    source = requests.get("https://www.google.com/search?q=Elon+Musk&source=lnms&tbm=nws").text
    soup = BeautifulSoup(source, 'lxml')

    for article in soup.find_all("div", class_="ZINbbc xpd O9g5cc uUPGi"):
        header = article.find("div", class_="BNeawe vvjwJb AP7Wnd").text

        # The summary contains the time and summary of the article, we are splitting the two items to put them in
        # different variables
        summary = article.find("div", class_="BNeawe s3v9rd AP7Wnd").text
        time = summary.split(" · ")[0]
        summary = summary.split(" · ")[1]

        # Link contains tracking information that we are removing off at the end of the link and unneeded text at the
        # start of the link
        dirty_link = (article.find("a")['href']).replace("/url?q=", "")
        link = dirty_link.split("&sa=U&")[0]

        print(header)
        print(summary)
        print(link)
        print(time)
        print("----------------------------------------------------------------------------------------------")

    else:
        print("Unable to find articles at this time...")
