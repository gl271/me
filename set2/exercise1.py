"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['i', 'am', 'debugging','this', 'stuff', 'loop', 'time']
#I think it will print the first word in the some_words
for word in some_words:
    print(word)
# I think it will go through all the variable words then stop
for x in some_words:
    print(x)
# it will print all the words in the some_words bracket
print(some_words)

# will print some words if it contains more than 3 words in the brackets, hence len = list length
if len(some_words) > 3:
    print('some_words contains more than 3 words')

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    #prints what our computer or laptop processes are 
    print(platform.uname())

usefulFunction()
