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
def get_words(chosen_template):
    inputs = []
    prompts = {}
    if chosen_template == "Superhero Story":
        prompts = {
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


        }
    elif chosen_template == "Space Adventure":
        prompts = {
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
        }
    
    elif chosen_template == "Haunted House":
        prompts = {
            "title": "Enter the title of your Haunted House: ",
            "name": "Enter a Name: ",
            "adjective1": "Enter an Adjective: ",
            "place": "Enter a type of building: ",
            "noun1": "Enter a Noun: ",
            "scary_sound": "Enter a Scary Sound: ",
            "verb1": "Enter a Verb: ",
            "ghost_name": "Enter a Ghost Name: ",
            "adjective2": "Enter an Adjective: ",
            "verb2": "Enter a Verb: ",
            "noun2": "Enter a Noun: "

        }


    for prompt in prompts.values():
        input = input_validation(prompt)
        inputs.append(input)

    words = dict(zip(prompts.keys(), inputs))
    return words




# Get Story (array from input_based_on_story) – function will use array of inputs to create array of sentences based on input of chosen story
def get_story(words, chosen_template):
    title = words["title"].upper()

    if chosen_template == "Superhero Story":
        story = f"""
                Title:  {title}
                ===================================
                It was a {words["adjective1"]} night in {words["city"]} when {words["superhero_name"]} suddenly received an emergency call. The evil {words["villain_name"]} was trying to {words["verb1"]} the city's most valuable {words["noun1"]}!

                Without hesitation, the {words["adjective2"]} hero activated their incredible {words["superpower"]} and raced toward the scene. When they arrived, they decided to {words["verb2"]} the villain using nothing but a {words["noun2"]}.

                After an intense battle, the city was finally safe once again. Everyone cheered for {words["superhero_name"]}, the greatest hero the city had ever known!
        """
    elif chosen_template == "Space Adventure":
        story = f"""
                Title:  {title}
                ===================================
                Captain {words["name"]} woke up aboard a {words["adjective1"]} spaceship somewhere near the mysterious planet {words["planet"]}. Suddenly, an alarm began to beep. The ship's computer detected a strange {words["noun1"]} approaching at incredible speed.

                Captain {words["name"]} looked out of the window and saw {words["alien_name"]}, a {words["noun2"]} alien floating beside the ship. The alien sent a message warning the crew about a {words["adjective2"]} [space object] heading directly toward them.

                Captain {words["name"]} decided to {words["verb"]} the ship as quickly as possible. Unfortunately, they accidentally crashed into a giant {words["noun3"]}! Somehow, the crew survived and returned home with the strangest space adventure in history. 
        """
    
    elif chosen_template == "Haunted House":
        story = f"""
                Title:  {title}
                ===================================
                One {words["adjective1"]} night, {words["name"]} decided to explore an abandoned {words["place"]} that everyone in town said was haunted. As soon as they entered, they noticed a strange {words["noun1"]} sitting in the middle of the hallway.

                Suddenly, they heard  {words["scary_sound"]} coming from upstairs. {words["name"]} decided to {words["verb1"]} toward the noise, even though every part of their body told them to run away. 
                At the top of the stairs, they met {words["ghost_name"]}, a {words["adjective2"]} ghost who had been trapped inside the house for hundreds of years.

                The ghost asked {words["name"]} to {words["verb2"]} the mysterious {words["noun2"]} hidden beneath the floorboards. But when they opened it... the lights went out!
        """

    return story











#Main -- Format all functions together in correct order 
def main():
    story_template
    chosen_template = story_template()
    words = get_words(chosen_template)
    story = get_story(words, chosen_template)
    print(story)
    return




main()









