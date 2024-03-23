# String concatenation

# A few ways to do this
# print ("invented by " + name)
# print ("invented by {}".format(name))
# print (f"invented by {name}")

# We're going to create out mad lib.

print("Please write what is requested\n")

adjective1 = input("Adjective: ")
nationality = input("Nationality: ")
person = input("Name of person: ")
noun1 = input("Noun: ")
adjective2 = input("Adjective: ")
noun2 = input("Noun: ")
adjective3 = input("Adjective: ")
adjective4 = input("Adjective: ")
pluralNoun = input("Plural noun: ")
noun3 = input("Noun: ")
number1 = input("Number: ")
shapes = input("Shapes: ")
food1 = input("Food: ")
food2 = input("Food: ")
number2 = input("Number: ")

madlib = f"Pizza was invented by a {adjective1} {nationality} chef named \
{person}. To make a pizza, you need to take a lump of {noun1}, and \
make a thin, round {adjective2} {noun2}. Then you cover it with \
{adjective3} sauce, {adjective4} cheese, and fresh chopped \
{pluralNoun}. Next you have to bake it in a very hot {noun3}. When \
it is done, cut it into {number1} {shapes}. Some kids like {food1} \
pizza the best, but my favorite is the {food2} pizza. if I could, I \
would eat pizza {number2} times a day!"


print(madlib)
