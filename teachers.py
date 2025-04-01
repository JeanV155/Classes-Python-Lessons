class FlashCards:
    def __init__(self, Questions, answers): 
        self.question = Questions
        self.answer = answers
        
        
    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def to_dict(self):
        return {"make": self.make, "model": self.model, "year": self.year, "image": self.image}

        