# 5. STRING. A simple code that depicts the dialogue of the Captain and his Crew 
# from the opera "H.M.S. Pinafore" by Gilbert and Sullivan. It offers the user to input 
# the right phrases to acquire the right answers
while True:
    a = input("Start the dialogue!")
    if a == "My gallant crew, good morning":
        print("Sir, good morning!")
        break  
    else:
        print("You've done it wrong. Please, try again")

while True:
    b = input("Carry on!")
    if b == "I hope you’re all quite well":
        print("Quite well; and you, sir?")
        break  
    else:
        print("You've done it wrong. Please, try again")

while True:
    c = input("Carry on!")
    if c == "I am in reasonable health, and happy to meet you all once more":
        print("You do us proud, sir!")
        break  
    else:
        print("You've done it wrong. Please, try again")
