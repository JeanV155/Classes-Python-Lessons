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
    FlashCard_data[question] = flashcard.to_dict()  # Save in dictionary
    with open("FlashCard.json", "w") as file:
        json.dump(FlashCard_data, file, indent=4)

# Teacher mode: prompt the teacher to input question-answer pairs
def teacher_mode():
    print("Welcome to Teacher Mode!")
    while True:
        question = input("Enter the question (or 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        answer = input("Enter the answer: ")
        add_flashcard(question, answer)
        print(f"Flashcard for '{question}' added successfully.")

# Student mode: prompt the student with questions and track their score
def student_mode():
    print("Welcome to Student Mode!")
    score = 0
    streak = 0
    total_flashcards = len(FlashCard_data)
    
    for question, card in FlashCard_data.items():
        answer = input(f"Question: {question}\nYour Answer: ")
        if answer.lower().strip() == card["answer"].lower().strip():
            score += 1
            streak += 1
            print("Correct!")
            if streak >= 3:  # Bonus for streaks
                score += 1  # Award bonus point
                print("Streak bonus! +1 point")
        else:
            streak = 0  # Reset streak on wrong answer
            print(f"Incorrect. The correct answer is: {card['answer']}")
    
    print(f"\nYour total score: {score}/{total_flashcards}")

# Main loop to allow the user to choose between Teacher and Student modes
def main():
    while True:
        mode = input("Select mode (teacher/student or 'exit' to quit): ").lower()
        if mode == "teacher":
            teacher_mode()
        elif mode == "student":
            student_mode()
        elif mode == "exit":
            break
        else:
            print("Invalid mode, please choose 'teacher' or 'student'.")

if __name__ == "__main__":
    main()

        

 
    
        
        


    

     

             
    
        
    
         
       

       
        