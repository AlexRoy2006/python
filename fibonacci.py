def fibonacci_no(n):
    first_number=1
    second_number=0
    third_number=0
    for i in range(n):
        print(third_number)
        third_number=first_number+second_number
        first_number=second_number
        second_number=third_number
fibonacci_no(69)