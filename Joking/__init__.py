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

'''
Not done yet
def chuck_norris_joke():
    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
    headers = {
	    "accept": "application/json",
	    "X-RapidAPI-Key": "blank",
	    "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
   }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
'''

def random_joke():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt"
    response = requests.request("GET", url)
    print(response.text)

def JOD():
    url = "https://jokes.one/joke-of-the-day/jod"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    print(soup.find('p').text)

def Multiple_Jokes(n):
    for i in range(n):
        url = "https://icanhazdadjoke.com/"
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        print(soup.find('p').text)

def sjoke(Joke_id):
    url = f"https://icanhazdadjoke.com/j/{Joke_id}"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    print(soup.find('p').text)

def search_for_joke(Search_term):
    url = f"https://icanhazdadjoke.com/search?term={Search_term}"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    print(soup.find('td').text)

def Random_knock_knock_joke():
    import random
    ran_int = random.randint(1, 148)
    url = f"http://www.jokes4us.com/knockknockjokes/random/knockknock{ran_int}.html"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    print(soup.find('font').text)

def skkjoke(Joke_id):
    url = f"http://www.jokes4us.com/knockknockjokes/random/knockknock{Joke_id}.html"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    print(soup.find('font').text)

def DarkJoke():
    url = "https://v2.jokeapi.dev/joke/Dark?format=txt"
    response = requests.request("GET", url)
    print(response.text)

def Pun():
    url = "https://v2.jokeapi.dev/joke/Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt"
    response = requests.request("GET", url)
    print(response.text)

def version():
    print("2.4.7")