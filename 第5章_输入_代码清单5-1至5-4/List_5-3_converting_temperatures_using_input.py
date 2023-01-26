#使用input()转化温度
print("This program converts Fahrenheit to Celsius.")
fahrenheit = float(input("Type in a temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5.0 / 9
print("That is ", end='')
print(celsius, end='')
print(" degrees Celsius.")
