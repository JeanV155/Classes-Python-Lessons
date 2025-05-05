import json

# Base User class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"

# FlashCard class
class FlashCard:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def to_dict(self):
        return {"prompt": self.prompt, "answer": self.answer}

# Teacher class
class Teacher(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def add_flashcards(self):
        print("\n--- Teacher Mode ---")
        
        # Load existing data manually (no with)
        try:
            file = open("FlashCards.json", "r")
            existing_data = json.load(file)
            file.close()
        except FileNotFoundError:
            existing_data = []

        # Loop to add new flashcards
        while True:
            prompt = input("Enter a word/phrase (or type 'exit' to stop): ")
            if prompt.lower() == "exit":
                break
            answer = input("Enter the correct answer: ")
            card = FlashCard(prompt, answer)
            existing_data.append(card.to_dict())  # Append to existing list
            print("Flashcard added!\n")

        # Save back to the file
        file = open("FlashCards.json", "w")
        json.dump(existing_data, file, indent=4)
        file.close()

        print("✅ All flashcards saved to FlashCards.json.")

# Student class
class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def study_flashcards(self):
        print("\n--- Student Mode ---")
        
        # Try to load flashcards
        try:
            file = open("FlashCards.json", "r")
            cards_data = json.load(file)
            file.close()
        except FileNotFoundError:
            print("No flashcards found. Ask your teacher to add some first.")
            return

        score = 0
        streak = 0

        for card in cards_data:
            print("\nQuestion:", card["prompt"])
            user_input = input("Your answer: ")

            if user_input.strip().lower() == card["answer"].strip().lower():
                streak += 1
                bonus = 1 if streak > 1 else 0
                earned = 1 + bonus
                score += earned
                print(f" Correct! (+{earned} point{'s' if earned > 1 else ''}) | Streak: {streak}")
            else:
                print(f" Incorrect. The correct answer was: {card['answer']}")
                streak = 0

        print(f"\nFinal Score: {score} point{'s' if score != 1 else ''}")

# Main program
def main():
    mode = input("Choose mode: (1) Teacher  (2) Student\nEnter 1 or 2: ").strip()

    if mode == "1":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        teacher = Teacher(name, email)
        print(teacher.display_info())
        teacher.add_flashcards()

    elif mode == "2":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        student = Student(name, email)
        print(student.display_info())
        student.study_flashcards()

    else:
        print("Invalid input. Please enter 1 or 2.")

main()
