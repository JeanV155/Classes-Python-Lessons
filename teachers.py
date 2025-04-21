import json

# Load existing data from FlashCard.json if it exists
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

# Function to add a new flashcard


def add_flashcard(question, answer):
    q = {
        "Question":question,
        "Answer":answer
    }
    # Write the updated dictionary back to the JSON file
    with open("FlashCard.json", "w") as file:
        json.dump(q, file, indent=4)




             
    
        
    
         
       

       
        