# 正の整数を入力として受け取る
number = int(input("1つの自然数を入れてね: "))

if number % 15 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(str(number))