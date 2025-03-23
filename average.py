def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

avg = average(4,6,1,6,1,7)
print(f"Average: {round(avg,2)}")