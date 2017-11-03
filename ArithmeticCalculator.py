#!usr/bin/env python3

from ArrayStack import ArrayStack
import re

# Stack-Based Infix Python Calculator
# Last modified 11/02/2017

#######################################################################################
###                                                                                 ###
###                                                                                 ###
###        TO USE THE CALCULATOR JUST CALL  ArithmeticCalulator()                   ###
###        IN YOU MAIN FUNCTION                                                     ###
###                                                                                 ###
###                                                                                 ###
#######################################################################################

# Calculator evaluates + - * / operations
# Works with single level parenthesis as well as nested and multiple parenthesis
# Example: (2+3)*5
#          (2+4)*(5-3)
#          (5+(2-1)*3)+8
# Works with whitespace input
# Manages division y 0
# The calculator evaluates the syntax

def ArithmeticCalculator():
    calculation = "yes"
    while calculation == "yes":
        expr = input("Enter an expression: ")
        print(Calculator(expr))
        calculation = input("Do you want to perform other calculation?(yes/no): ")
        if calculation != "yes":
            print("Thank you")
            break
    return


def syntax(validexpression):
    validexpression = re.split("([()+-/*])", validexpression.replace(" ", ""))
    validexpression = [x for x in validexpression if x]
    if validexpression[0] == "+" or validexpression[0] == "-" or validexpression[0] == "*" or  validexpression[0] == "/" or validexpression[-1] == "+" or validexpression[-1] == "-" or validexpression[-1] == "*" or validexpression[-1] == "/":
        return False

    counter = 0
    for i in range(len(validexpression)):
        if validexpression[i] == "/" and validexpression[i+1] == "0":
            return False
        if (validexpression[i] == "+" or validexpression[i] == "-" or validexpression[i] == "*" or validexpression[i] == "/") and (validexpression[i+1] == "+" or validexpression[i+1] == "-" or validexpression[i+1] == "*" or validexpression[i+1] == "/"):
            return False
        if i == "(" or i == ")":
            i += 1

    if i % 2 != 0:
        return False
    return True


def Calculator(expression):
    if not syntax(expression):
        return "Syntax Error"
    numbers_stack = ArrayStack()
    op_stack = ArrayStack()
    expression = re.split("([()+-/*])", expression.replace(" ", ""))
    expression = [x for x in expression if x]

    for element in expression:
        if element.isdigit():
            numbers_stack.push(int(element))
        elif element == "(":
            op_stack.push(element)
        elif element == ")":
            while op_stack.top() != "(":
                operator = op_stack.pop()
                operand1 = numbers_stack.pop()
                operand2 = numbers_stack.pop()
                numbers_stack.push(operations(operator, operand1, operand2))
            op_stack.pop()
        elif element == "+" or element == "-" or element == "*" or element == "/":
            while (not op_stack.is_empty()) and precedence(element, op_stack.top()):
                operator = op_stack.pop()
                operand1 = numbers_stack.pop()
                operand2 = numbers_stack.pop()
                numbers_stack.push(operations(operator, operand1, operand2))
            op_stack.push(element)

    while not op_stack.is_empty():
        operator = op_stack.pop()
        operand1 = numbers_stack.pop()
        operand2 = numbers_stack.pop()
        numbers_stack.push(operations(operator, operand1, operand2))
    return numbers_stack.pop()


def precedence(pre1, pre2):
    if pre2 == "(" or pre2 == ")":
        return False
    if (pre1 == "*" or pre1 == "/") and (pre2 == "+" or pre2 == "-"):
        return False
    else:
        return True


def operations(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num2 - num1
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by 0")
            return -1
        return int(num2 / num1)
    return 0


def main():
    ArithmeticCalculator()


if __name__ == '__main__':
    main()
