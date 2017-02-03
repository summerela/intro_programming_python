'''Create a script called hw3.py
Write a function that takes a minimum and maximum number as an argument.  - check
Your function should print out the following for each number in the range:
This number {} is at index {} in the list.  - check
If a number is divisible by 3, print the following sentence instead (use string formatting):  - check
"The number {} is divisible by 3 and at index {} in the list."  - check
Add a docstring to the beginning of your script providing your thoughts on how a user -check
might break your function (fix them if you know how!)


HOW CAN IT BE BROKE?
I don't think it can be broken.  Though it took many iterations
to get to this point.  At one point, a Max number that was actually
lower than the Min number would've broken it.
I've played with a few different versions of multiple entries
and so far it's working.'''


minnum = int(input("Please type a low number:"))

#Use a function to get (and ensure) a max number

def ensure_bignum(minnum):
    bignum = int(input("Please type a big number: "))
    while bignum <= minnum:
        print("Sorry, it must be bigger than your first number.")
        bignum = int(input("Please type a big number: "))
    return bignum

maxnum = ensure_bignum(minnum)



#Calculate the length of our list by subtracting the large from small number.
length = maxnum - minnum
#       testingline print(length)



#This section defines the list name and
# then builds the list.  It does this by using the 'append' function
# to build it 1 by 1 until we get to the Max num.

lowtohighlist = [minnum,maxnum]
#       testingline print(lowtohighlist)
nextnum=minnum+1
#       testingline print(nextnum)
lowtohighlist.append(minnum)
#       testingline print(lowtohighlist)





#create the list which starts with the "low number" and tops out at the "high number"

newlist=[minnum]
for counter in range(length):
#testingline    print("counter=",counter, "length=",length)
    lastnumberinlist=newlist[len(newlist)-1]
    nextnumberinlist = lastnumberinlist + 1
#testingline    print("lastnumberinlist=",lastnumberinlist, "nextnumber is=", nextnumberinlist)
    newlist.append(nextnumberinlist)
#testingline    print(newlist)

print("This is your list: ",newlist)



#this starts to do the real work.
#it walks through the list and does that actual analysis and printing.

for position in range(length+1):
    walkthelist = newlist[position]
#testingline    print("\twalkthelist=", walkthelist)
    if walkthelist%3==0:
        print("DIVISIBLE BY 3 WARNING....Number {} at position {} is divisble by 3".format(walkthelist,position))
    else:
        print("Number {} is at position {} in the list".format(walkthelist, position))

