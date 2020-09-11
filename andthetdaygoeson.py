import datetime
while True:
    user_input = input("Enter a list of real numbers separated by space: ")
    try:
        my_list = [float(x) for x in user_input.split()]
    except ValueError:
        print("Some of the values were invalid. Try again.")
        continue
    if not my_list:
        print("You didn't enter any values. Try again.")
        continue
    break
print("\n")
userList = user_input.split()

start_time = datetime.datetime.now()
sum1 = 0
for num in userList:
    sum1 += float(num)
    average = sum1 / len(my_list)
print("Average = ", average)
end_time = datetime.datetime.now()
time_diff = end_time - start_time
execution_time = time_diff.total_seconds() * 1000
print(execution_time)
