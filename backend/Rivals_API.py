import requests
from dotenv import load_dotenv
import os

load_dotenv()

class RivalsApi:
    def __init__(self):
        self.base_url = "https://mrapi.org/api/"
        self.headers = {
            "X-API-Key": os.getenv("RIVALS_API_KEY"),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            }

    # RETURNS id FOR USERNAME
    def get_player_id(self, player_name):
        url = self.base_url + f'player-id/{player_name}'

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            return e
    
    # RETURNS PLAYER CAREER DATA GIVEN id
    def get_player(self, player_id):
        url = self.base_url + f'player/{player_id}'

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return e

    # RETURNS PLAYERS RECENT MATCHES 
    def get_matches(self, player_id):
        url = self.base_url + f"player-match/{player_id}"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return e
        
    def get_hero(self, hero_name):
        url = self.base_url + f"hero/{hero_name}"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return e

api = RivalsApi()
uid = api.get_player_id('purplestoke')
print(uid)
heroes = [
    "Adam Warlock",
    "Black Panther",
    "Black Widow",
    "Captain America",
    "Cloak & Dagger",
    "Doctor Strange",
    "Groot",
    "Hawkeye",
    "Hela",
    "Hulk",
    "Human Torch",
    "Invisible Woman",
    "Iron Fist",
    "Iron Man",
    "Jeff The Land Shark",
    "Loki",
    "Luna Snow",
    "Magik",
    "Magneto",
    "Mantis",
    "Mister Fantastic",
    "Moon Knight",
    "Namor",
    "Peni Parker",
    "Psylocke",
    "Rocket Raccoon",
    "Scarlet Witch",
    "Spiderman",
    "Squirrel Girl",
    "Star Lord",
    "Storm",
    "The Punisher",
    "The Thing",
    "Thor",
    "Venom",
    "Winter Soldier",
    "Wolverine"
]