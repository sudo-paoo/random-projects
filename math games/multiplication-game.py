import random

def game():
    correct = 0
    incorrect = 0
    while True:
        first_num = random.randint(1, 10)
        second_num = random.randint(1, 10)
        answer = first_num * second_num
        print(f"{first_num} × {second_num}\n")
        try:
            user_answer = input("Enter your answer: ")
            if user_answer == str(answer):
                print("Your answer is correct.")
                correct += 1
                print(f"Correct: {correct}\nIncorrect: {incorrect}")
                continue
            elif user_answer == 'q':
                print(f"Correct Answers: {correct}\nIncorrect Answers: {incorrect}\n")
                break
            else:
                print("Sorry, wrong answer.")
                incorrect += 1
                print(f"Correct: {correct}\nIncorrect: {incorrect}")
                continue
        except ValueError:
            print("Sorry, I didn't understand that. Here's a new question")
if __name__ == "__main__":
    game()
