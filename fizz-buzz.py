def fizz_buzz(x):
    # 3 fizz, 5 buzz, 15 fizzbuzz
    for i in range(1, x):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizz_buzz(101)
