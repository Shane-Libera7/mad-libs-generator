# Story template choice – function should return variable called chosen_template, 
# string of the template chosen which will be referred to the rest of the code. 
# To dictate sentence formation and word input
def story_template():
    
    while True:
        choice = input("Enter the lowercase letter of the Story Template you wish to use:  " \
        "A) Superhero Story " \
        "B) Space Adventure " \
        "C) Haunted House ")
        if choice == "a":
            chosen_template = "Superhero Story"
            break
        elif choice == "b":
            chosen_template = "Space Adventure"
            break
        elif choice == "c":
            chosen_template = "Haunted House"
            break
        else: 
            print("Invalid input please try again")
            continue
    
    print(f"You have chosen {chosen_template}")
    return chosen_template

   
        



# Input Validation () - function will validate each input returns word -- Strip whitespace, checks its not empty and contains acceptable characters 
def input_validation(prompt):
   
    
    while True:
       user_input = input(prompt)
       word = str(user_input).strip()
       if word == "":
           print("Invalid Input. Enter input necessary")
           continue
       elif all(character.isalpha() or character  in " -" for character in word):
           print("Input Accepted")
           break
       else:
           print("Invalid input. Enter input necessary")
           continue
           
           
    return word 
    





# Input based on request (chosen template) – function will use input validation to ask each kind of word in order needed for chosen template 
# return array of words needed in order of the story 
def 




# Get Story (array from input_based_on_story) – function will use array of inputs to create array of sentences based on input of chosen story







#Format Story-- collect unformatted story and creat title + add line breaks and capitalisation to print full story in aesthetic format 




#Main -- Format all functions together in correct order 
def main():
    story_template()
    return




main()









