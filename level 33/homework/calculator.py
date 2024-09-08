# განსაზღვრეთ ფუნქცია სახელწოდებით simple_calculator, რომელიც იღებს სამ არგუმენტს:

# num1: პირველი რიცხვი (მთლიანი ან float).
# num2: მეორე რიცხვი (მთლიანი ან float).

# ოპერაცია: სტრიქონი, რომელიც განსაზღვრავს შესასრულებლად ოპერაციას. ის შეიძლება იყოს „დამატება“, „გამოკლება“, „გამრავლება“ ან „გაყოფა“.
# ფუნქციის შიგნით,

# გამოიყენეთ if და elif განცხადებები, რათა დაადგინოთ რომელი ოპერაცია უნდა შეასრულოთ ოპერაციის არგუმენტის მნიშვნელობიდან გამომდინარე.

# ფუნქციამ უნდა დააბრუნოს ოპერაციის შედეგი.

# თუ ოპერაცია არის „გაყოფა“ და num2 არის 0, ფუნქციამ უნდა დააბრუნოს „შეცდომა: ნულზე გაყოფა შეუძლებელია“.
# ჩაწერეთ კოდი, რომ გამოიძახოთ ფუნქცია სხვადასხვა ოპერაციებით და დაბეჭდოთ შედეგები.

def simple_calculator(a, b):

    print('1. addition')
    print('2. subtraction')
    print('3. multiplication')
    print('4. split')

    choose = input('choose an action : ')

    if choose == "addition":
        print(a + b)
    elif choose == "subtraction":
        print(a - b)
    elif choose == "multiplication":
        print(a * b)
    elif choose == "split":
        if b == 0:
            print('It cannot be divided by zero')
        else:
            print(a // b)
    else:
        print('Unknown operation')

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

simple_calculator(a, b) 