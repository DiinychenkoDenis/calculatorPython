from colorama import init
from colorama import Fore, Back, Style
print ( Back.RED )

print ( 'Добро пожаловать в калькулятор' )
what = input ("Что будем делать (+,-,*,/): ")

print ( Back.CYAN )
a = float( input ("Введите первое число: "))
print ( Back.GREEN )
b = float( input ("Введите второе число: "))
if what != "+":
else:
	c =  a + b 
	print ( Back.RED )
	print ("Результат: " + str(c))

if what == "*":
	c =  a * b 
	print ( Back.RED )
	print ("Результат: " + str(c))
elif what == "/":
	c =  a / b 
	print ( Back.RED )
	print ("Результат: " + str(c))
elif what == "-":
	c = a - b 
	print ( Back.RED )
	print ("Результат: " + str(c))

input()