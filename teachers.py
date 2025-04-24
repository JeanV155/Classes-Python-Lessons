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

    def to_dict(self):
        return {"question": self.question, "answer": self.answer}

# Function to add a new flashcard
def add_flashcard(question, answer):
    flashcard = FlashCard(question, answer)
    FlashCard_data[question] = flashcard.to_dict()
    with open("FlashCard.json", "w") as file:
        json.dump(FlashCard_data, file, indent=4)

# Teacher mode
def teacher_mode():
    print("Welcome to Teacher Mode!")
    while True:
        question = input("Enter the question (or 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        answer = input("Enter the answer: ")
        add_flashcard(question, answer)
        print(f"Flashcard for '{question}' added successfully.")

# Student mode
def student_mode():
    print("Welcome to Student Mode!")
    score = 0
    total_flashcards = len(FlashCard_data)

    for question, card in FlashCard_data.items():
        answer = input(f"Question: {question}\nYour Answer: ")
        if answer == card["answer"]:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {card['answer']}")

    print(f"\nYour total score: {score}/{total_flashcards}")

# Menu to start the program
if __name__ == "__main__":
    mode = input("Choose mode (teacher/student): ").lower()
    if mode == "teacher":
        teacher_mode()
    elif mode == "student":
        student_mode()
    else:
        print("Invalid mode selected.")


        

 
    
        
        


    

     

             
    
        
    
         
       

       
        