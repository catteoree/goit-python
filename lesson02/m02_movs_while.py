from typing import Counter


counter = 0

while True:
    
    user_input = input(">>> ")
    counter += 1
    if user_input == "q" or counter >= 5:
        break
    
    else:
        print(f"You printed: {user_input}")
        