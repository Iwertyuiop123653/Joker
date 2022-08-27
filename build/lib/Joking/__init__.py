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


def chuck_norris_joke():
    import requests
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.request("GET", url)
    dict = response.text
    import json
    test_string = dict 
    dict = json.loads(test_string)
    print(dict.get('value'))

def random_joke():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt"
    response = requests.request("GET", url)
    print(response.text)

def JOD():
    url = "https://jokes.one/joke-of-the-day/jod"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    print(soup.find('p').text)
    return soup.find('p').text

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
    return soup.find('p').text

def search_for_joke(Search_term):
    url = f"https://icanhazdadjoke.com/search?term={Search_term}"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    print(soup.find('td').text)
    return soup.find('td').text

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
    return soup.find('font').text

def DarkJoke():
    url = "https://v2.jokeapi.dev/joke/Dark?format=txt"
    response = requests.request("GET", url)
    print(response.text)

def Pun():
    url = "https://v2.jokeapi.dev/joke/Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt"
    response = requests.request("GET", url)
    print(response.text)

def Submit_joke(Q, Punchline, Your_name="Anonymous", twitter="@Null"):
    url = "https://backend-omega-seven.vercel.app/api/addjoke"
    payload = {
        "name": Your_name,
        "twitter": twitter,
        "question": Q,
        "punchline": Punchline
    }
    response = requests.request("POST", url, json=payload)
    print(response.text)
    return response.text

def yo_mama_joke_slash_insults():
    import random
    Joke_id = random.randint(1, 1000)
    url = f"http://www.jokes4us.com/yomamajokes/random/yomama{Joke_id}.html"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    print(soup.find('font').text)
    return soup.find('font').text

def animal_joke():
    import random
    jokes = ["Q. There are ten cats standing on a boat. One cat jumps off the boat, how many more cats are left?\nA. None, because the cats were all copy cats!", "Q. What did the duck say when he bought lipstick?\nA. “Put it on my bill.”", "Q. What do you call a rabbit that has fleas?\nA. Bugs bunny.", "Q. Which place should you never consider taking a dog?\nA. We should never take a dog to a Flea Market.", "Q. What did the SNAIL say while riding on the turtles back?\nA. Wheeeeeeeee", "Q. How does a lion greet the other animals in the field?\nA. “Pleased to eat you.”", "Q. What kind of key opens a banana?\nA. A monkey.", "Q. What money do cats use to go shopping?\nA. Cats use kitty cash!", "Q. What do you call a monkey in the war field\nA. A baboon", "Q. Why did the witches team lose the baseball game?\nA. Their bats flew away.", "Q. Where did the cat go when it lost its tail?\nA. To the retail store!", "Q. What's a shark's favorite sandwich?\nA. Peanut butter and jellyfish!", "Q. When building a house, what tool do dinosaurs use the most?\nA. They frequently use a dino-saw", "Q. What pine has the longest needles?\nA. A porcupine.", "Q. What is the best way to cook a gator?\nA. In a crock-pot", "Q. What do you call a pig that is never fun to hang out with?\nA. The pig will be called a boar.", "Q. Why are giraffes so slow to apologize?\nA. It takes them a long time to swallow their pride.", "Q. What is the difference between a cat that follows you and a cat that got photocopied?\nA. One is a copy cat, and the other is a cat copy.", "Q. When dinosaurs keep scoring touchdowns, what does its team get?\nA. The team will keep getting dino-scores!", "Q. Which day do fish hate?\nA. Fryday.", "Q. What is the name of the movie when the stars are a pig and a dinosaur?\nA. The perfect name for the movie is “Jurassic pork”!", "Q. What do you call a lazy baby kangaroo?\nA. A pouch potato.", "Q Why couldn't the leopard play hide and seek?\nA. Because he was always spotted.", "Q. What is the difference between swine flu and bird flu?\nA. You need an oink-ment for the swine flu but a tweet-ment for the bird flu.", "Q. What animal has the whiskers of a cat, fur of a cat, a tail of a cat, ears of a cat, but is not a cat?\nA. The animal is a kitten!", "Q. What is the name of the scary dinosaur that was raised by pigs?\nA. Its name was porkasaurus rex!", "Q. What is the nickname of a person that puts his right hand inside the large mouth of a scary T-Rex?\nA. The perfect nickname to give is “Lefty”!", "Q. Since the chickens wake up when the rooster crows, when do all the ducks wake up?\nA. The ducks get up at the quack of dawn!", "Q. Why did the pig have ink all over its face?\nA. Because it came out of the pen."]
    jokenum = random.randint(0, 28)
    print(jokes[jokenum])

__version__ = '2.8.0'