print(4, 8, 15, 16, 23, "42\n")

print(f"{4}\n{8}\n{15}\n{16}\n{23}\n{42}\n")

x = int(input("Число:"))
y = x + 1
z = y + 1
print(f"{x}\n{y}\n{z}\n")

first = int(input("1:"))
second = int(input("2:"))
third = int(input("3:"))
print(f"\n{first+second+third}\n")

K = int(input("Ребро:"))
V = K*K*K
P = 6*K*K
print(f"Объем куба:{V}\nПлощадь поверхностей:{P}\n")

Children = int(input("Число детей:"))
Apple = int(input("Количество яблок:"))
sum = Apple // Children
Remains = Apple % Children
print(f"Каждый получит {sum} яблок.\nВ корзине останется {Remains} яблок.\n")

D = int(input("Your number:"))
thousand = D // 1000
thousand_remain = D % 1000
hundred = thousand_remain // 100
hundred_remain = thousand_remain % 100
tens = hundred_remain // 10
tens_remain = hundred_remain % 10
zero = tens_remain // 1
print(f"The digit in the thousands position is {thousand}\n")
print(f"The number in the hundreds position is {hundred}\n")
print(f"The digit in the tens position is {tens}\n")
print(f"The digit in the position of units is {zero}\n")

population = int(input("Насление:"))
kill = population % 2
if  kill == 0:
    print(population//2)
elif kill > 0:
    print( (population + 1)/2 )

    try:

        num1 = float(input("Please type the first number: "))
        num2 = float(input("Please type the second number: "))

        operation = input("Please choose the operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':

            if num2 == 0:
                print("Error: Division by zero")
            else:
                result = num1 / num2
        else:
            print("Invalid operation choice")

        if 'result' in locals():
            print(f"{num1} {operation} {num2} = {result:.3f}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")