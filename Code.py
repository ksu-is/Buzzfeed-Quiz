print("Buzzfeed Quiz: Tell Us Your Style & We will Tell You What Subject You’ll Teach")
print("Please Put Your Answer As a Capital Letter")
#Questions the quiz will ask: 
question1 = input("On a night out do you prefer: \n A. A Dress \n B. Jeans and Blouse \n C. Romper \n D. Whatever is Clean \n Answer:")
question2 = input("What are your go to shoes: \n A. Louboutins \n B. Nike \n C. Crocs \n D. UGGs \n Answer:")
question3 = input("What’s favorite type of jeans: \n A. Skinny Jeans \n B. Bootcut Jeans \n C. Boyfriend Cut Jeans \n D. Jean Shorts \n Answer:")

#Evaluate answers
def quiz():
    if question1 == "A" and question2 == "A" and question3 == "A":
        print("You Would Teach English!")
    elif question1 == "B" and question2 == "A" and question3 == "A":
        print("You Would Teach Psychology!")
    elif question1 == "C" and question2 == "A" and question3 == "A":
            print("You Would Teach US History!")
    elif question1 == "D" and question2 == "A" and question3 == "A":
        print("You Would Teach Biology!")
    elif question1 == "A" and question2 == "B" and question3 == "A":
            print("You Would Teach Economics!")
    elif question1 == "A" and question2 == "C" and question3 == "A":
            print("You Would Teach Health!")
    elif question1 == "A" and question2 == "D" and question3 == "A":
            print("You Would Teach Calculus!")
    elif question1 == "A" and question2 == "A" and question3 == "B":
            print("You Would Teach World History!")
    elif question1 == "A"and question2 == "A" and question3 == "C":
            print("You Would Teach Physical Education!")
    elif question1 == "A" and question2 == "A"and question3 == "D":
            print("You Would Teach Environmental Science!")
    elif question1 == "A"and question2 == "B"and question3 == "B":
            print("You Would Teach Statistics!")
    elif question1 == "B"and question2 == "B"and question3 == "B":
            print("You Would Teach Physics!")
    elif question1 == "C"and question2 == "B"and question3 == "B":
            print("You Would Teach Biology!")
    elif question1 == "D" and question2 == "B"and question3 == "B":
            print("You Would Teach English!")
    elif question1 == "A" and question2 == "C" and question3 == "C":
            print("You Would Teach Psychology!")
    elif question1 == "B" and question2 == "C" and question3 == "C":
            print("You Would Teach US History!")
    elif question1 == "C" and question2 == "C" and question3 == "C":
            print("You Would Teach Psychology!")
    elif question1 == "D" and question2 == "C" and question3 == "C":
            print("You Would Teach Economics!")
    elif question1 == "A" and question2 == "D" and question3 == "D":
            print("You Would Teach Health!")
    elif question1 == "B" and question2 == "D" and question3 == "D":
            print("You Would Teach Calculus!")
    elif question1 == "C" and question2 == "D" and question3 == "D":
            print("You Would Teach World History!")
    elif question1 == "D" and question2 == "D" and question3 == "D":
            print("You Would Teach Physical Education!")
    elif question1 == "B" and question2 == "A" and question3 == "B":
            print("You Would Teach Environmental Science!")
    elif question1 == "B" and question2 == "C" and question3 == "B":
                    print("You Would Teach Physics!")
    elif question1 == "B" and question2 == "D" and question3 == "B":
                    print("You Would Teach Psychology!")
    elif question1 == "B" and question2 == "B" and question3 == "A":
                    print("You Would Teach US History!")
    elif question1 == "B" and question2 == "B" and question3 == "C":
                    print("You Would Teach Biology!")
    elif question1 == "B" and question2 == "B" and question3 == "D":
                    print("You Would Teach Health!")
    elif question1 == "C" and question2 == "A" and question3 == "B":
                    print("You Would Teach Psychology!")
    elif question1 == "D" and question2 == "A" and question3 == "B":
                    print("You Would Teach Music!")
    elif question1 == "B" and question2 == "A" and question3 == "D":
                    print("You Would Teach Calculus!")
    elif question1 == "C" and question2 == "A" and question3 == "D":
                    print("You Would Teach Statistics!")
    elif question1 == "D" and question2 == "A" and question3 == "D":
                    print("You Would Teach US History!")
    elif question1 == "B" and question2 == "A" and question3 == "C":
                    print("You Would Teach World History!")
    elif question1 == "C" and question2 == "A" and question3 == "C":
                    print("You Would Teach Environmental Science!")
    elif question1 == "D" and question2 == "A" and question3 == "C":
                    print("You Would Teach Health!")
    elif question1 == "C" and question2 == "B" and question3 == "A":
                    print("You Would Teach Home Economics!")
    elif question1 == "D" and question2 == "B" and question3 == "A":
                    print("You Would Teach Music!")
    elif question1 == "A" and question2 == "B" and question3 == "D":
                    print("You Would Teach Home Economics!")
    elif question1 == "C" and question2 == "B" and question3 == "D":
                    print("You Would Teach Music!")
    elif question1 == "D" and question2 == "B" and question3 == "D":
                    print("You Would Teach Psychology!")
    elif question1 == "A" and question2 == "B" and question3 == "C":
                    print("You Would Teach Health!")
    elif question1 == "C" and question2 == "B" and question3 == "C":
                    print("You Would Teach Home Economics!")
    elif question1 == "D" and question2 == "B" and question3 == "C":
                    print("You Would Teach Music!")
    elif question1 == "B" and question2 == "C" and question3 == "A":
                    print("You Would Teach Home Economics!")
    elif question1 == "C" and question2 == "C" and question3 == "A":
                    print("You Would Teach Music!")
    elif question1 == "D" and question2 == "C" and question3 == "A":
                    print("You Would Teach US History!")
    elif question1 == "A" and question2 == "C" and question3 == "B":
                    print("You Would Teach World History!")
    elif question1 == "C" and question2 == "C" and question3 == "B":
                    print("You Would Teach Statistics!")
    elif question1 == "D" and question2 == "C" and question3 == "B":
                    print("You Would Teach Calculus!")
    elif question1 == "A" and question2 == "C" and question3 == "D":
                    print("You Would Teach Biology!")
    elif question1 == "B" and question2 == "C" and question3 == "D":
                    print("You Would Teach Physics!")
    elif question1 == "C" and question2 == "C" and question3 == "D":
                    print("You Would Teach Psychology!")
    elif question1 == "D" and question2 == "C" and question3 == "D":
                    print("You Would Teach US History!")
    elif question1 == "B" and question2 == "D" and question3 == "A":
                    print("You Would Teach World History!")
    elif question1 == "C" and question2 == "D" and question3 == "A":
                    print("You Would Teach English!")
    elif question1 == "D" and question2 == "D" and question3 == "A":
                    print("You Would Teach Economics!")
    elif question1 == "A" and question2 == "D" and question3 == "B":
                    print("You Would Teach Biology!")
    elif question1 == "C" and question2 == "D" and question3 == "B":
                    print("You Would Teach Physics!")
    elif question1 == "D" and question2 == "D" and question3 == "B":
                    print("You Would Teach Environmental Science!")
    elif question1 == "A" and question2 == "D" and question3 == "C":
                    print("You Would Teach Physical Education!")
    elif question1 == "B" and question2 == "D" and question3 == "C":
                    print("You Would Teach Health!")
    elif question1 == "C" and question2 == "D" and question3 == "C":
                    print("You Would Teach Music!")
    elif question1 == "D" and question2 == "D" and question3 == "C":
                    print("You Would Teach Home Economics!")
quiz()

answer = input("Thank you for taking quiz! Would you like to play again? \n")
while answer.lower() == "yes":
    print("Buzzfeed Quiz: Tell Us Your Style & We will Tell You What Subject You’ll Teach")
    print("Please Put Your Answer As a Capital Letter")
#Questions the quiz will ask: 
    question1 = input("On a night out do you prefer: \n A. A Dress \n B. Jeans and Blouse \n C. Romper \n D. Whatever is Clean \n Answer:")
    question2 = input("What are your go to shoes: \n A. Louboutins \n B. Nike \n C. Crocs \n D. UGGs \n Answer:")
    question3 = input("What’s favorite type of jeans: \n A. Skinny Jeans \n B. Bootcut Jeans \n C. Boyfriend Cut Jeans \n D. Jean Shorts \n Answer:")
    quiz()
    answer = input("Thank you for taking quiz! Would you like to play again? \n" )