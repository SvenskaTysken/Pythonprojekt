def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Ange (A, B, C, eller D) :")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)
#-----------------------
def check_answer(answer, guess):

    if answer == guess:
        print("Rätt svar!")
        return 1
    else:
        print("Fel svar...")
        return 0
#-----------------------
def display_score(correct_guesses, guesses):
    print("-----------------------------------------")
    print("RESULTAT")
    print("-----------------------------------------")

    print("FACIT: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("DINA SVAR: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Ditt resultat är: "+str(score)+"%")

#-----------------------
def play_again():

    response = input("Vill du spela igen? : (ja/nej) :")
    response = response.upper()

    if response == "JA":
        return True
    else:
        return False

#-----------------------

questions = {
 "Vad heter Justus i mellannamn?: ": "A",
 "Vem var justus idol när han var liten? :": "D",
 "Vilken är Justus sanna etnicitet :": "D",
 "Hur lång är Justus?: ": "C"
}

options = [["A. Kristoffer", "B. Abdirahman", "C. Stefan", "D. Ali-reza"],
          ["A. Heinrich Himmler", "B. Allah", "C. Einstein", "D. Johan Thim"],
          ["A. Jude", "B. Tysk", "C. Marsian", "D. Den Ariska rasen"],
          ["A. Lång", "B. Inte så lång", "C. 187cm resp. 23cm", "D. Längre än Hasbullah"]]

new_game()

while play_again():
    new_game()

print("Hejdå!")
