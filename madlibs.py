 

"""
Creating a MadLibs Game 
    Mad Libs is a phrasal template word game which consists of one player 
    prompting others for a list of words to substitute for blanks in a story 
    before reading aloud. The game is frequently played as a party game or as a pastime
    https://www.youtube.com/watch?v=8ext9G7xspg
"""
 
 
 # string concatenation (putting strings together)
 # suppose that we need to create a string that syas "subcribe to ___"
youtube = "Ruben" # some string value

# possible ways to do it. 
print("Subscribe to " + youtube)
print("Subscribe to {}".format(youtube))
print(f"Subscribe to {youtube}")


adj = input("Type an Adjective: ") 
verb = input("Type an Verb: ")
verb2 = input("Type another Verb: ") 
famous_person = input("Type a famous person: ")

madlib = f"Computer programming is as {adj} as playing video game! It is a new ways of doing things and I like it because \
it make sound {verb}. Stay fresh and {verb2}, like your are {famous_person} "

print(madlib)