# from collections import Counter

def gpa(*grades):
    total = 0
    sum_of_credit_hours = []
    grades_count = []
    while True:
        grades = input("Enter your Grade : ")
        if grades == "done" or grades == "Done":
            final_Grade = total/sum(sum_of_credit_hours)
            print("Your total GPA: ",round(final_Grade,2)) 
            break
        grades_count.append(grades)
        credit_hour = int(input("Enter the credit hour of the Course: "))
        match grades:
            case "A+"|"a+":
                credit_score = 4.0
                sum_of_credit_hours.append(credit_hour)
                print(sum_of_credit_hours)
                total += credit_score * credit_hour
            case "A"|"a":
                credit_score = 3.6
                sum_of_credit_hours.append(credit_hour)
                total += credit_score * credit_hour
            case "B+"|"b+":
                credit_score = 3.2
                sum_of_credit_hours.append(credit_hour)
                total += credit_score * credit_hour
            case "B"|"b":
                credit_score = 2.8
                sum_of_credit_hours.append(credit_hour)
                total += credit_score * credit_hour
            case "C+"|"c+":
                credit_score = 2.4
                sum_of_credit_hours.append(credit_hour)
                total += credit_score * credit_hour
            case "C"|"c":
                credit_score = 2.0
                sum_of_credit_hours.append(credit_hour)
                total += credit_score * credit_hour
            case "D+"|"d+":
                credit_score = 1.5
                sum_of_credit_hours.append(credit_hour)
                total +=credit_score * credit_hour
            case "D"|"d":
                credit_score = 1.0
                sum_of_credit_hours.append(credit_hour)
                total += credit_score * credit_hour
            case "F"|"f":
                credit_score = 0
                sum_of_credit_hours.append(credit_hour)
                total += credit_score
            case _:
                print("Invalid Grade, Try Again")
    # order_count = Counter(grades_count)
    # print(order_count)
                
              
gpa()