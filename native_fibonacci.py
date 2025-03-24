def fibonnaci(number):
    count = 1
    first_num = 0
    second_num = 1
    while count<number:
        print(first_num,end=" ")
        new_number = second_num + first_num
        first_num = second_num
        second_num = new_number
        count+=1
        
            
fibonnaci(16)
