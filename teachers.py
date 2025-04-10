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

# Teacher mode: prompt the teacher to input question-answer pairs
def teacher_mode():
    while True:
        question = input("Enter the word/phrase (question): ")
        if question.lower() == 'exit':
            break
        answer = input("Enter the answer: ")
        
        # Add the flashcard to the dictionary and save it to the file
        add_flashcard(question, answer)
        print(f"Flashcard added: {question} -> {answer}")  


# Start teacher mode
teacher_mode() 

def student_mode():
     
        
             
    
        
    
         
       

       
        