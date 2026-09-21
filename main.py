#Full Data of all stories 
STORIES = {
            "a": {
                "name": "Superhero Story",
                "prompts": {
                "title": "Enter the title of your Superhero Story: ",
                "superhero_name": "Enter a Superhero name: ",
                "adjective1": "Enter an Adjective: ",
                "city": "Enter a city: ",
                "villain_name": "Enter a Villain Name: ",
                "adjective2": "Enter an adjective: ",
                "verb1": "Enter a Verb: ",
                "noun1": "Enter a Noun: ",
                "superpower": "Enter a Superpower: ",
                "verb2": "Enter a Verb: ",
                "noun2": "Enter a Noun: "
                },
                "template": """
                Title:  {title}
                ===================================
                It was a {adjective1} night in {city} when {superhero_name} suddenly received an emergency call. The evil {villain_name} was trying to {verb1} the city's most valuable {noun1}!

                Without hesitation, the {adjective2} hero activated their incredible {superpower} and raced toward the scene. When they arrived, they decided to {verb2} the villain using nothing but a {noun2}.

                After an intense battle, the city was finally safe once again. Everyone cheered for {superhero_name}, the greatest hero the city had ever known!
                """
                },
            "b": {
                "name": "Space Adventure",
                "prompts": {
                "title": "Enter the title of your Space Adventure: ",
                "name": "Enter a Name: ",
                "adjective1": "Enter an Adjective: ",
                "planet": "Enter a Planet Name: ",
                "noun1": "Enter a Noun: ",
                "alien_name": "Enter an Alien Name: ",
                "noun2": "Enter a Noun: ",
                "adjective2": "Enter an Adjective: ",
                "space_object": "Enter a Space Object: ",
                "verb": "Enter a Verb: ",
                "noun3": "Enter a Noun: "
                },
                "template": """
                Title:  {title}
                ===================================
                Captain {name} woke up aboard a {adjective1} spaceship somewhere near the mysterious planet {planet}. Suddenly, an alarm began to beep. The ship's computer detected a strange {noun1} approaching at incredible speed.

                Captain {name} looked out of the window and saw {alien_name}, a {noun2} alien floating beside the ship. The alien sent a message warning the crew about a {adjective2} {space_object} heading directly toward them.

                Captain {name} decided to {verb} the ship as quickly as possible. Unfortunately, they accidentally crashed into a giant {noun3}! Somehow, the crew survived and returned home with the strangest space adventure in history. 
                """
                },
            "c": {
                "name": "Haunted House",
                "prompts": {
                "title": "Enter the title of your Space Adventure: ",
                "name": "Enter a Name: ",
                "adjective1": "Enter an Adjective: ",
                "planet": "Enter a Planet Name: ",
                "noun1": "Enter a Noun: ",
                "alien_name": "Enter an Alien Name: ",
                "noun2": "Enter a Noun: ",
                "adjective2": "Enter an Adjective: ",
                "space_object": "Enter a Space Object: ",
                "verb": "Enter a Verb: ",
                "noun3": "Enter a Noun: "
                },
                "template": """
                Title:  {title}
                ===================================
                One {adjective1} night, {name} decided to explore an abandoned {place} that everyone in town said was haunted. As soon as they entered, they noticed a strange {noun1} sitting in the middle of the hallway.

                Suddenly, they heard  {scary_sound} coming from upstairs. {name} decided to {verb1} toward the noise, even though every part of their body told them to run away. 
                At the top of the stairs, they met {words["ghost_name"]}, a {adjective2} ghost who had been trapped inside the house for hundreds of years.

                The ghost asked {name} to {verb2} the mysterious {noun2} hidden beneath the floorboards. But when they opened it... the lights went out!
                """
                }
}






# Story template choice – function should return variable called chosen_template, 
def story_template():
    
    while True:
        choice = input("Enter the lowercase letter of the Story Template you wish to use:  \n" 
        "A) Superhero Story \n" 
        "B) Space Adventure \n" 
        "C) Haunted House \n")

        if choice in STORIES:
            chosen_template = STORIES[choice]
            break
        else:
            print("Invalid Input, try again")
            continue
            
    print(f"You have chosen {chosen_template["name"]}")
    return chosen_template

   
        



# Input Validation () - function will validate each input returns word -- Strip whitespace, checks its not empty and contains acceptable characters 
def input_validation(prompt):
   
    
    while True:
       user_input = input(prompt)
       word = user_input.strip()
       if word == "":
           print("Invalid Input.Enter input necessary")
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
def get_words(chosen_template):
    answers = []
    for prompt in chosen_template["prompts"].values():
        answer = input_validation(prompt)
        answers.append(answer)

    words = dict(zip(chosen_template["prompts"].keys(), answers))
    return words




# Get Story (array from input_based_on_story) – function will use array of inputs to create array of sentences based on input of chosen story
def get_story(words, chosen_template):
    words["title"] = words["title"].upper()
    story = chosen_template["template"].format_map(words)
    
    return story










#Main -- Format all functions together in correct order 
def main():
    
    chosen_template = story_template()
    words = get_words(chosen_template)
    story = get_story(words, chosen_template)
    print(story)
    




main()









