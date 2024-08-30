# import sqlite3
import random


# myconnection = sqlite3.connect("questionsdb")
# mycursor = myconnection.cursor()
# mycursor.execute(
#     "CREATE table question_table IF NOT EXISTS Values(question_id PRIMARY KEY INTEGER, question TEXT, answer TEXT, option1 TEXT, option2 TEXT, option3 TEXT)")
# questionList = ["What is the capital of Bogota"]

class Question:
    def __init__(self, question, answer, option1, option2, option3):
        self.question = question
        self.answer = answer
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3


listofQuestions = [
    Question("What is the capital of France?", "Paris", "Oslo", "Madrid", "London"),
    Question("Which planet is known as the Red Planet?", "Mars", "Venus", "Jupiter", "Saturn"),
    Question("Who painted the Mona Lisa?", "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo"),
    Question("What is the largest mammal in the world?", "Blue Whale", "African Elephant", "Giraffe", "Hippopotamus"),
    Question("Which element has the chemical symbol 'O'?", "Oxygen", "Gold", "Silver", "Iron"),
    Question("Leopold Bloom is a character in which novel?", "Ulysses", "1984", "The Edible Woman",
             "Pride and Prejudice"),
    Question("Who wrote the play 'Romeo and Juliet'?", "William Shakespeare", "Charles Dickens", "Jane Austen",
             "Mark Twain"),
    Question("What is the largest organ in the human body?", "Skin", "Heart", "Liver", "Brain"),
    Question("Which country is home to the kangaroo?", "Australia", "New Zealand", "South Africa", "Brazil"),
    Question("What is the hardest natural substance on Earth?", "Diamond", "Gold", "Iron", "Quartz")
]

print(len(listofQuestions))
questionIndex = 0


def checkRight(question, answer, input):
    isright = False
    for myquestions in listofQuestions:
        if (myquestions.question == question):
            if (input == myquestions.answer):
                isright = True
                print("Correct Answer")
            else:
                print("Wrong Answer")
    return isright


while (True):
    options = [listofQuestions[questionIndex].answer,
               listofQuestions[questionIndex].option1,
               listofQuestions[questionIndex].option2,
               listofQuestions[questionIndex].option3]

    random.shuffle(options)
    answer = listofQuestions[questionIndex].answer
    myInput = input(
        listofQuestions[questionIndex].question + "\n" + "A " + options[0] + "\n" + "B " + options[1] + "\n" + "C " +
        options[
            2] + "\n" + "D " +
        options[3] +
        "\n" + "Press q to quit"
    ).strip()

    if (myInput.casefold() == "q"):
        break

    if (myInput.casefold() == "a"):
        myInput = options[0]
    elif (myInput.casefold() == "b"):
        myInput = options[1]
    elif (myInput.casefold() == "c"):
        myInput = options[2]
    elif (myInput.casefold() == "d"):
        myInput = options[3]

    myboolean = checkRight(listofQuestions[questionIndex].question, listofQuestions[questionIndex].answer,
                           myInput.strip())
    if (myboolean):
        if (questionIndex >= len(listofQuestions) - 1):
            questionIndex = 0
        else:
            questionIndex = questionIndex + 1
        continue
