print("Welcome to the love calculator")
name1 = input("what is the first name? ").lower()
name2 = input("what is the second name? ").lower()

name1_score = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
name2_score = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
print(name1_score)
print(name2_score)

final_score = int(str(name1_score) + str(name2_score))

if final_score < 10 or final_score > 90:
    print(f"your score is {final_score} you go together like mentos and coke")
elif final_score >40 and final_score < 50:
    print(f"your score is {final_score} you are good together")
else:
    print(f"your score is {final_score}")