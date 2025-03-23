#KBC Game
questions = [
    "Pakistan became independent in?",
    "What is the capital of Pakistan?",
    "Who is known as the founder of Pakistan?",
    "What is the national language of Pakistan?",
    "How many provinces does Pakistan have?"
]

q1_choices = [1946,1965,1947,1884]
q2_choices = ["Karachi","Lahore","Hyderabad","Islamabad"]
q3_choices = ["Alama Iqbal","Muhammad Ali Jinnah","Ayoub Khan","Liaquat ali khan"]
q4_choices = ["Sindhi","Urdu","Pashto","Siraiki"]
q5_choices = [5,7,10,4]

correct_answers = 0

print(questions[0])
print(q1_choices)
q1_input = int(input("Enter the answer: "))
if q1_input == q1_choices[2]:
    print("Correct Answer")
    correct_answers += 1
else:
    print("Wrong Answer")
    
print(questions[1])
print(q2_choices)
q2_input = input("Enter the answer: ")
if q2_input == q2_choices[3]:
    print("Correct Answer")
    correct_answers += 1
else:
    print("Wrong Answer")
    
print(questions[2])
print(q3_choices)
q3_input = input("Enter the answer: ")
if q3_input == q3_choices[1]:
    print("Correct Answer")
    correct_answers += 1
else:
    print("Wrong Answer")
    
print(questions[3])
print(q4_choices)
q4_input = input("Enter the answer: ")
if q4_input == q4_choices[1]:
    print("Correct Answer")
    correct_answers += 1
else:
    print("Wrong Answer")
    
print(questions[4])
print(q5_choices)
q5_input = int(input("Enter the answer: "))
if q5_input == q5_choices[3]:
    print("Correct Answer")
    correct_answers += 1
else:
    print("Wrong Answer")
        
print("Total Correct Answers: ",correct_answers)
if correct_answers == 5:
    print("You Have Won 700 Million Dollars")
else:
    print("Better Luck Next Time")