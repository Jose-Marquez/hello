#Define a function called greet that takes a name as a string, then prints "Hello, <name>!" to the screen.

def greet(name):
    print("Hello {}!".format(name))

greet("world")

#Goldilocks is 135 cm tall, and she is very picky about the size of her bed.
#If the bed is shorter than 140 cm, or larger than 150 cm, then she is unhappy.
#Write a function called goldilocks that takes the length of a bed in cm and
#prints whether goldilocks is happy with it. Be sure to distinguish whether the bed is too small or too large!

def goldilocks(height):
    if (height<140):
        print("Too small!")
    elif (height>150):
        print("Too large!")
    else:
        print("Just right! :)")

goldilocks(139)
goldilocks(140)
goldilocks(150)
goldilocks(151)

#Write a function called square_list that takes a list of numbers and
#returns a list where each element has been squared.

def square_list(list):
    newList = []
    for number in list:
        newList.append(number**2)
    return newList

print(square_list([1,2,3]))

#Write a function called fibonacci_stop that returns a list of the Fibonacci numbers
#up to a specified maximum value. Recall that the Fibonacci sequence is a sequence
#in which the next number is the sum of the previous two numbers: 1, 1, 2, 3, 5, etc.

def fibonacci_stop(stop):
    list = [1]
    prev = 0
    index = 0
    new = list[index]
    while (new+prev<stop):
        list.append(new+prev)
        prev = new
        index += 1
        new = list[index]
    return list

print(fibonacci_stop(30))

#Define a function called clean_pitch that takes two lists, one representing measurements
#from the pitch instrument at certain points in time and the other representing the corresponding
#status signal. The function should return a cleaned list of the pitch angle, where “good” values
#are untouched and “bad” values are set to -999.

def inRange(pitch):
    return((pitch>=0) and (pitch<=90))

def clean_pitch(pitch,status):
    index = 0
    count = len(pitch)
    while index < count:
        if (status[index]):
            if not inRange(pitch[index]):
                pitch[index] = -999
        index += 1

    return pitch





x = [-1, 2, 6, 95]  # "raw" pitch angle at four time steps
status = [1, 0, 0, 0]  # status signal
print(clean_pitch(x, status))


