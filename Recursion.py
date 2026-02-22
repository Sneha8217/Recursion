def increment_and_print(counter: int):
    if counter >= 10:
        return
    
    counter = counter + 1
    print(counter)
    increment_and_print(counter)

# Function call
increment_and_print(0)
