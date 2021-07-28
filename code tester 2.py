import time

print("Welcome to the Buzzfeed Quiz.\nChoose which oufits best decribes your style and we'll tell you what subject you would teach as a school teacher !!")
time.sleep(2)

print("The Quiz will consit of 6 Multiple Choice Questions.\nThe Quiz will keep track of your score and at the end you will recieve your Final Decison.")
time.sleep(2)

print("Select a/b/c/d or Enter the Answer, to Answer Each Question.")
time.sleep(2)

print("Good Luck, and Let's Begin!!!")
score = 0

q_attempted = 0

print("")
  
# Question 1
print("Q1. On a night out do you prefer?:")
answer = input("A.  Dress \nB. Jeans and Blouse \nC. Romper \nD. Whatever is Clean \n").lower()
q_attempted += 1
if answer == "a" or answer == "b" or answer == "c" or answer == "d":
   print("Way to go!.")

print("")

# Question 2
print("Q2. When lounging around the house what do you wear?:")
answer = input("A. T-shirt and Sweatpants \n B. Nothing \n C. Bathing Suit \n D. Pajamas \n").lower()
q_attempted += 1
if answer == "a" or answer == "b" or answer == "c" or answer == "d":
   print("Such a bold choice.")

print("")

# Question 3
print("Q3. What are your go to shoes?:")
answer = input("A. Louboutins \n B. Nike \n C. Crocs \n D. UGGs \n").lower()
q_attempted += 1
if answer == "a" or answer == "b" or answer == "c" or answer == "d":
   print("Now thats what I call a statement piece!")

print("")

# Question 4
print("Q4. What is your favorite color scheme?:")
answer = input("A. Bright Summer Colors \n B. Black?/White \n C. Fall Colors \n D. Natural Colors \n").lower()
q_attempted += 1
if answer == "a" or answer == "b" or answer == "c" or answer == "d":
   print("Fake it till' you make it!")

print("")

# Question 5
print("Q5. What is your typical makeup routine?:")
answer = input("A. All Glam \n B. Natural Look \n C. Bare Face \n D. Only Special Occasions \n").lower()
q_attempted += 1
if answer == "a" or answer == "b" or answer == "c" or answer == "d":
   print("You Rock!")

print("")

# Question 6
print("Q6. What’s favorite type of jeans?:")
answer = input("A. Skinny Jeans \n B. Bootcut Jeans \n C. Boyfriend Cut Jeans \n D. Jean Shorts \n").lower()
q_attempted += 1
if answer == "a" or answer == "b" or answer == "c" or answer == "d":
   print("I love it !")
