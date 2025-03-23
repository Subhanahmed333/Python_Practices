questions = [
    "Pakistan became independent in?",
    "What is the capital of Pakistan?",
    "Who is known as the founder of Pakistan?",
    "What is the national language of Pakistan?",
    "How many provinces does Pakistan have?"
]
choices =[[1946,1965,1947,1884],
          ["Karachi","Lahore","Hyderabad","Islamabad"],
          ["Alama Iqbal","Muhammad Ali Jinnah","Ayoub Khan","Liaquat ali khan"],
          ["Sindhi","Urdu","Pashto","Siraiki"],
          [5,7,10,4]
]

correct_answers = [3,4,2,2,4]
count_correct = 0

for i in range(len(questions)):
    print(questions[i])
    for j, option in enumerate(choices[i], 1):
        print(f"{j}. {option}")
        
    try:
        user_input = int(input("Enter your choice (1-4):"))
        if user_input == correct_answers[i]:
            print("Correct Answer")
            count_correct+=1
        else:
            print("Wrong Answer")
    except ValueError:
        print("Invalid input! Please enter a number.")

print("Total Correct Answers: ",count_correct)
        