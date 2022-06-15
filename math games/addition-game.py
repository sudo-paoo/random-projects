import random

def game():
    correct = 0
    incorrect = 0
    while True:
        first_num = random.randint(1, 100)
        second_num = random.randint(1, 100)
        answer = first_num + second_num
        print(f"Problem: {first_num} + {second_num}\n")
        try:
            user_answer = int(input("Enter your answer: "))
            if user_answer == answer:
                print("Your answer is correct.")
                correct += 1
                print(f"Correct: {correct}\nIncorrect: {incorrect}")
                continue
            else:
                print("Sorry, wrong answer.")
                incorrect += 1
                print(f"Correct: {correct}\nIncorrect: {incorrect}")
                continue
        except ValueError:
            print("Sorry, I didn't understand that. Here's a new question")


if __name__ == "__main__":
    game()
