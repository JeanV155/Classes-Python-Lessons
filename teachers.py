import json

try:
    with open("FlashCard.json", "r") as file:
        FlashCard_data = json.load(file)
except FileNotFoundError:
    FlashCard_data = {}

# Define the FlashCard class
class FlashCard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
             
    
        
    
         
       

       
        