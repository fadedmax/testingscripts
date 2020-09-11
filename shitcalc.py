print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplacation")
print ("4. Division")
print ("5. Primes to 100")
print ("6. Find factors")
print ("")
question = input("Please select a option")

if question == "1":
    num1 = int(input("Enter first number: "))
    print (num1)
    num2 = int(input("Enter second number: "))
    print (num2)
    print ("")
    ans = num1 + num2
    print (ans)
if question == "2":
    num1 = int(input("Enter first number: "))
    print (num1)
    num2 = int(input("Enter second number(what will be subtracted): "))
    print (num2)
    print ("")
    ans = num1 - num2
    print (ans)
if question == "3":
    num1 = int(input("Enter first number: "))
    print (num1)
    num2 = int(input("Enter second number: "))
    print (num2)
    print ("")
    ans = num1 * num2
    print (ans)
if question == "4":
    num1 = int(input("Enter first number: "))
    print (num1)
    num2 = int(input("Enter second number: "))
    print (num2)
    print ("")
    ans = num1 / num2
    print (ans)
if question =="5":
   print ("")
   print ("2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 and lastly 97.")    
if question == "6":
    print ("test")
