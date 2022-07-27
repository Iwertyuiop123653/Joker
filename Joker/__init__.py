import requests
from bs4 import BeautifulSoup

def random_dad_joke():
    url = "https://icanhazdadjoke.com/"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    print(soup.find('p').text)

def programming_joke():
    url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt"
    response = requests.request("GET", url)
    print(response.text)

#not complete yet
#def chuck_norris_joke():
#    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
#    headers = {
#	    "accept": "application/json",
#	    "X-RapidAPI-Key": "2438e24119mshcb8c5b0532b594fp12cd6cjsna4090ec4d7dc",
#	    "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
#   }
#    response = requests.request("GET", url, headers=headers)
#    print(response.text)

def random_joke():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt"
    response = requests.request("GET", url)
    print(response.text)