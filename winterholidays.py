#requirements
#create a function called winter holiday()
#take one parameter 
#- string
#returns a summary of an event from ur holiday
import random
good_things=["i hung out with friends", "i had a lot of fun"]
bad_things=["i slept too much","i ate to much"]
random_bad_thing=random.choice(bad_things)
random_good_thing=random.choice(good_things)
def winter_holiday(good_or_bad: str) -> str:
    if good_or_bad.lower() ==  "good":
        return random_good_thing
    if good_or_bad.lower() ==  "bad":
        return random_bad_thing
        


print(winter_holiday("bad"))

