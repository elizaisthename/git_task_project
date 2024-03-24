# asking the user to input the swimming time
swim_time = int(input("Enter the time taken for swimming, in minutes, please: "))

# asking the user to input the cycling time
cycle_time = int(input("Enter the time taken for cycling, in minutes, please: "))

# asking the user to input the running time
run_time = int(input("Enter the time taken for running, in minutes, please: "))

total_minutes = swim_time+cycle_time+run_time

if total_minutes <= 100:
    print("Provincial colours")
elif total_minutes <= 105:
    print("Provincial Half Colours")
elif total_minutes <= 110:
    print("Provincial Scroll")
elif total_minutes >= 111:
    print("No award")
