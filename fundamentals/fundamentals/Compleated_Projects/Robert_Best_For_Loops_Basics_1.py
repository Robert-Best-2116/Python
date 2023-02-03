#Print all integers from 0 to 150
for num in range(151):
    print(num) 
#Print all the multiples of 5 from 5 to 1,000
for num in range(5, 1001, 5):
    print(num)

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"

for num in range (1, 101):
    if num % 10 == 0:
        num = "Coding Dojo"
        print(num)
    elif num % 5 == 0:
        num = "Coding"
        print(num)
    else:
        print(num)

#Add odd integers from 0 to 500,000, and print the final sum.
total = 0
for num in range(5000000):
    if num % 2 == 1:
        total = num + total

print(total)
# most challenging so far. needed to find good documentation then tweak it to work properly. was still the hardest even after the last one. 

#Print positive numbers starting at 2018, counting down by fours

for num in range(2018, 0 , -4):
    print(num)

# the numbers will always be postitive beings that 4 is a postitive number

#Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = int(2)
highNum = (9)
mult = (3)

for num in range(lowNum, highNum ):
    if num % mult == 0:
        print(num)

#gotta thank stack overflow for this one, i had the modulus idea right but was usuing it wrong, something devided by a multiple of its self has a remander of zero, whichhhhh means its a multiple. some people are really good at math