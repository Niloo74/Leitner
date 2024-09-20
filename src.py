
#class for making a flashcard 
from collections import deque
from datetime import datetime, timedelta




class FlashCards:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def get_answer(self):
        return self.answer
    
    def get_question(self):
        return self.question
    
    def to_string(self):
        return self.question + " : " + self.answer
    
    def review(self):
        response =input(self.question + "(Next)\n") == self.answer
        if response == self.answer:
            print("Correct!")
            return True
        elif response == "next":
            return False
        else:
            if input("Incorrect! \nCorrect Answer is: "+ self.answer + " would you like to use your answer as correct?(Y/N):") == "Y":
              return True
            else: 
                return False  
    
#class for making each box (ussually they are between 1-5)
class Box:
    def __init__(self, level):
        self.level = level
        self.cards = deque()
        self.last_reviewed = datetime.now()  # Correctly use datetime.now()
        self.review_interval = timedelta(days=2**level)  # Correctly use timedelta

    def add_card(self, card):
        self.cards.append(card)

    def review_card(self):
        if self.cards:
            return self.cards.popleft()
        return None

    def needs_review(self):
        # Check if the appropriate number of days has passed since last review
        return datetime.now() - self.last_reviewed >= self.review_interval

    def mark_reviewed(self):
        # Update last review time to now
        self.last_reviewed = datetime.now()

    def time_until_due(self):
        # Returns how much time is left until the next review
        return self.review_interval - (datetime.now() - self.last_reviewed)


    def time_until_due(self):
        # Returns how much time is left until the next review
        return self.review_interval - (datetime.now() - self.last_reviewed)
    

    def has_cards(self):
        return len(self.cards) > 0  
    
    def get_level(self):
        return self.level
    
    def remove_card(self):
        self.cards.pop()
    
    def to_string(self):
     for card in self.cards:
        print(card.to_string())  # Print each card's string representation


class LeitnerSystem:
    def __init__(self):
        #the five boxes we need till graduation of cards
        self.boxes = [Box(i) for i in range(1, 6)]

    def add_card(self, card):
        # Add card to the first box
        self.boxes[0].add_card(card)
    
    def move_card(self, card, current_box_level, correct):
       if correct and current_box_level < 5:
        # Move card to the next box (increment level)
             self.boxes[current_box_level].add_card(card)
       else:
            # Move card back to Box 1 if incorrect
            self.boxes[0].add_card(card)

    

    def review_box(self, box_level):
        box = self.boxes[box_level - 1]  # Access the correct box
        if box.needs_review():
            print(f"Box {box.level} is due for review.")
        else:
            # Give feedback if reviewing early
            time_left = box.time_until_due()
            print(f"Box {box.level} is not due yet. You are reviewing it {time_left.days} days and {time_left.seconds // 3600} hours early.")
            proceed = input("Do you still want to review it? (yes/no): ").strip().lower()
            if proceed != "yes":
                return

        # Proceed with the review
        cards_to_review = list(box.cards)  
        for card in cards_to_review:
        # The card is already removed from the deque by review_card() method
            box.review_card()  # Remove the card from the box
            if card.review():  # If the answer is correct
                self.move_card(card, box.get_level(), True)  # Move the card to the next box
            else:
                self.move_card(card, box.get_level(), False)  # Move the card to Box 1

            box.mark_reviewed()  # Mark the box as reviewed
    

def 

def main():
    leitner_system = LeitnerSystem()

    # Add cards to Box 1
    
    leitner_system.boxes[0].add_card(FlashCards("What is 2 + 2?", "4"))
    leitner_system.boxes[0].add_card(FlashCards("What is the capital of France?", "paris"))
    print("Tthe box1 is now: ")
    leitner_system.boxes[0].to_string()
    # Try reviewing Box 1
    leitner_system.review_box(1)
    print("Tthe box1 is now: ")
    leitner_system.boxes[0].to_string()

    print("Tthe box2 is now: ")
    leitner_system.boxes[1].to_string()



class Main:
    main()