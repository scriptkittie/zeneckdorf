def checkIfNumber(s):
    try:
        s = int(s)
        return True
        
    except Exception:
        return False

#Before we start, we create a function that checks whether or not a number that is
#input is an integer.  If it does, we have it pass and continue on.  If it isn't
#an integer, we return it as an error and ask the user to input an integer.

##def fib(sequence):
##    if (sequence < 0):
##        return sequence
##    if (sequence == 0):
##      return sequence
##  if(sequence == 1):
##      return sequence
##  return fib(sequence - 1) + fib(sequence - 2)

#This function is the longer version of the shorter function below.
#We define this function as the fib function, which will be what will
#generate the fibonacci sequence without any specific rules.  We create
#and if statement stating that if the sequence integer in the argument is lower
#than 0, to prompt the user again.  We make another if statement stating that if
#the number input is 0, to once again prompt.  We make a last if statement if it's
#1, to also prompt the user again -- as these numbers don't really generate a sequence
#but only return themselves.  If it is none of those limitations, we have a calculation
#of where we return the input subtrated by one, and another value subtracted by 2, these
#two values continue on down a tree that helps calculate our sequence.
    

# def algorithm(user_number):
#     last_generated_number = -1
#     i = 0
#     number_list = list()
#     while(last_generated_number < user_number):
#         last_generated_number = fib(i)
#         number_list.append(last_generated_number)
#         i = i+1

#This is the second part of the longer algorithm, this is the function that actually takes fib1 and
#the values of the sequence we calculated above, and stores and arranges them.  We create a variable that is 
#called "last generated number", suggesting it to be -1.  We can choose any number, since it isn't ever used, 
#and we end up overwriting it anyway.  This is just a placeholder of an integer value.  We then create the 
#variable i to tell what sequence we will be on, versus last_generated_number #will be used  to temporarily store 
#the last generated number of our sequence.  We create a number list, where we assign it to a list for our sequence.
#We then add the last generated number to the number_list that we are storing, and at each time we increment the next
#sequence one more.  An example, user input 4. So we started out with i = 0, and we have 0 in our numbers list so far!
# Afterwards, the code runs and adds an increment "i" by 1. i = 1.  The function fib is then called with the value of i
#and making fib(1) = 1.  The calculated number then is appended to the numbers_list. Our numbers list now has the values: 0,1
#Then we increment i to "2". We then call fib with the value of 2, and the result we get back is "1"(1 is the third term 
#of the fibonacci sequence). The stored list is then now has: 0,1,1.  This continues until we store up to a sequence number
#that would be greater than 4, which ends up to be i=5, which produces 8.  So we remain with just 0,1,1,2,3.

def algorithm_short(fib1):
    fib_list = [0,1]
    while fib_list[-1] < fib1:
        fib_list.append(fib_list[-1] + fib_list[-2])
    number_list = list()
    
    while sum(number_list) < fib1:

        number_list.append(max(
                [max_num 
                for max_num in fib_list 
                    if max_num <= fib1 - sum(number_list)
                ]))
        
    return number_list
               
#The commented algorithm was the longer function, this is the shorter algorithm that does the same
#thing but this is a little more elegant.  We create the function algorithm_shorter and still use the fib1.
#We then create a list called fib_list, and we have the values [0.1] in it, as most numbers will have 0 and 1 as 
#the first part of their sequence.  If the user inputs 0 or 1, the while loop stating that if the last number in
#the stored sequence is greater than the fib1 or equal, it will return as false, and break the loop.
#However, if it is still less than the fib1, we ask that we add to the fib_list the last number fib_list[-1]
#and the second to the last number fib[-2].  This will create a third instance, and we will continue to the next
#while loop.  In the next while loop we state that the number_list, which we initialized above to just be a list,
#will have everything in it added by calling sum.  If the sum of the number list is less than fib1, we
#continue down the while loop, taking the max number that is within the list.  In the example, we take 4 as the
#fib1 input, we go through the list of 0, 1, 1, 2, 3.  We take the max number 3, and we evaluate the max_number in
#fib_list, and see if it is less than or equal to fib1 (being 4) subtraction by the sum of the number_list, which would be
#4-3, leaving it as 1.  It then goes down the list, which next would be 2, 2 + 3 would make it 6, so it loops back.  It is
#until it hits 1, that it is false again, breaks, and when it is done with the entire list it returns num_list with 3 and 1.
    
while(True):
    
    fib1 = raw_input("Please enter a number to start the fibonacci sequence:\n >")
    
    if (checkIfNumber(fib1) == False):
        print "Invalid value."
        continue
    
    elif(fib1 == "1"):
        break

    else: 
        fib1 = int(fib1)

    print "We are calculating the Zeneckdorf's sequence for" + str(fib1)
    print algorithm_short(fib1)

#We create one last while, stating that if the argument is true, we have fib1 be assigned the user input.
#We make an if statement saying to check the number if fib1 is not an int, we would print it as a invalid
#vaalue.  We had already initialized the function at the beginning to see if it is an integer.  If it is
#we continue, and it loops back up.  The else breaks it out of the if function, and we continue to the next
#if function, which asks whether or not fib1 is 1, if it is, we need to break because the sequence of 1
#would just be 1.  We create an else saying that the fib1 statement does end up a number, we convert it
#to an integer.  Afterwards, we print the statement that we are calculating the user input.  We then call
#and print the algorithm_short of fib, which will print our sequence.