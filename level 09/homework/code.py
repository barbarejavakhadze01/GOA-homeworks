#1) დაწერეთ პითონის პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს ორი რიცხვი და შემდეგ დაბეჭდოს მათი ჯამი.
num1 = int(input("enter number a; "))
num2 = int(input("enter number b; "))
result = num1 + num2
print(num1 ,'+', num2, '=', result)

#2)დაწერეთ პითონის პროგრამა, რომელიც ითვლის მართკუთხედის ფართობს. პროგრამამ უნდა სთხოვოს მომხმარებელს მართკუთხედის სიგანე და სიმაღლე.


length = int(input("enter length of rectangle; "))
width = int(input("enter width of rectangle; "))
result = length * width
print(length , '*' , width, '=', result)
            

#3) დაწერეთ პითონის პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ დაბეჭდოს ამ რიცხვის ორმაგი.
n1m = int(input("enter number c; "))
n2m = int(input("enter number d; "))
n3 = 2
result2 = ((n1m + n2m) * n3)
print(result2)



#4)დაწერეთ პითონის პროგრამა, რომელიც ითვლის მართკუთხედის პერიმეტრს. პროგრამამ უნდა სთხოვოს მომხმარებელს მართკუთხედის სიგანე და სიმაღლე.
length = int(input("enter length of rectangle; "))
width = int(input("enter width of rectangle; "))
perimetri = 2
result3 = ((length + width) * perimetri)
print(result3)



#5) დაწერეთ პითონის პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ დაბეჭდოს ამ რიცხვის კვადრატი(გამოიყენეთ ** - ოპერატორი
number_1 = int(input("enter number e; "))
number_2 = int(input("enter number f; "))
result4 = ((number_1 + number_2) * (number_1 + number_2))
print(result4)