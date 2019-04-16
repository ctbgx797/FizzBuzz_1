# 正の整数を入力として受け取る
number = int(input("1つの自然数を入れてね: "))

if number % 3 == 0:
    output = "Fizz"
else:
    output = str(number)

print(output)
