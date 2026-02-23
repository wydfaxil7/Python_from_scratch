questions = [
    ["Who made Facebook?", "Mark Zuckerberg", "Bill Gates", "Steve Jobs", "Elon Musk", 1],
    
    ["What is the capital of Pakistan?", "Lahore", "Karachi", "Islamabad", "Peshawar", 3],
    
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    
    ["Who wrote Romeo and Juliet?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain", 2],
    
    ["What is 9 x 8?", "72", "64", "81", "69", 1],
    
    ["Which gas do plants absorb?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],
    
    ["Who invented the light bulb?", "Albert Einstein", "Thomas Edison", "Nikola Tesla", "Isaac Newton", 2],
    
    ["Which is the largest continent?", "Africa", "Europe", "Asia", "Australia", 3],
    
    ["What is the square root of 144?", "10", "11", "12", "14", 3],
    
    ["Which country won the Cricket World Cup 1992?", "India", "Pakistan", "Australia", "England", 2],
    
    ["What does CPU stand for?", "Central Power Unit", "Central Processing Unit", "Computer Personal Unit", "Control Processing Unit", 2],
    
    ["Who painted the Mona Lisa?", "Van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo", 3],
    
    ["Which language is used to style web pages?", "HTML", "Python", "CSS", "C++", 3],
    
    ["Which language is used to style web pages?", "HTML", "Python", "CSS", "C++", 3],
    
    ["What is the largest ocean?", "Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Arctic Ocean", 3]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

money = 0

for i in range(0, len(questions)):
    
    q = questions[i]
    print(f"\nYour Next question for Rs. {levels[i]} is: ")
    print("\nQ::  ",q[0].upper())
    print(f"a. {q[1]}        b. {q[2]}")
    print(f"c. {q[3]}        d. {q[4]}")
    reply = int(input("\nEnter your answer (1-4) : "))
    if (reply == q[-1]):
        print(f"\n                CORRECT ANDWER! \nYou have won {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else: 
        print("WRONG ANSWER :(")
        break

print(f"\nYour takehome money amount is Rs. {money}, CONGRATULATIONS!")