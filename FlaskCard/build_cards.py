import openai
import uuid
import json
from cards import *

OPENAI_KEY = ""
openai.api_key = OPENAI_KEY

user_prompt = "create a card for math problem please"
system_prompt = "You should return a single jason string of the form {{card_front: <front-string>,card_back:<back-string>}} where front-string is a simple math problem and the back-string is the answer to that problem."


class BuildCards:
    # Create a single card using a prompt
    def create_card(user_prompt:str,chat_log:list = []):
        system_prompt = "You should return a single jason string of the form {{\"card_front\": <front-string>,\"card_back\":<back-string>}} where front-string is a simple math problem and the back-string is the answer to that problem."
        new_prompts = messages = [
                {"role":"user","content":user_prompt},
                {"role":"system","content":system_prompt}
            ]
        
        while True:
            messages = chat_log + new_prompts
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = messages
            )

            card_json = response["choices"][0]["message"]["content"]
            try:
                return BuildCards.convert_json_to_card(card_json)
            except:
                continue
    
    # Convert a json string representation to a card object and store it in the card_table
    def convert_json_to_card(card_json:str):
        card_dict = json.loads(card_json)
        card_id = get_uuid(Card)
        card = Card(card_id = card_id,**card_dict)
        return card
    

    # Check if a json string is valid representation of a card
    def is_valid_json_card(json_card):
        try:
            card_dict = json.loads(json_card)
            attributes = ["card_front","card_back"]
            if all(attr in card_dict for attr in attributes):
                return True
            else:
                return False
        except:
            return False

class ManageDecks:
    def create_deck(deck_name:str,card_list:list):
        deck_id = get_uuid(Deck)
        deck = Deck(deck_id = deck_id,deck_name = deck_name,size = 0)
        for card in card_list:
            card.deck_id = deck_id
    
    def view_deck(deck_id):
        return Card.query(deck_id = deck_id)
        


            
            

    