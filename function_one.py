def __init__(self):
        self.score = 0
        self.attempts = 10

    def generate_problem(self):
        number1 = random.randint(1, 100)
        number2 = random.randint(number1 + 1, 200)
        return number1, number2

    def subtract(self, number1, number2):
        result = number1 - number2
        return result

    def check_answer(self, number1, number2, answer):
        correct_result = self.subtract(number1, number2)
        if correct_result == answer:
            self.score += 1
            return "Correct"
        else:
 return "Incorrect. The correct answer is: {}".format(correct_result)

    def play_game(self):
        for _ in range(self.attempts):
            number1, number2 = self.generate_problem()
            print("What is {} - {}".format(number1, number2))
            for i in range(2):
                user_answer = int(input("Enter your answer: "))
                result = self.check_answer(number1, number2, user_answer)
                print(result)print("Your final score is: {}".format(self.score))


