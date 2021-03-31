import tkinter

calculatorValue = '0'
total = 0

def setDigit(num):
    global calculatorValue
    if isinstance(calculatorValue, float):
        calculatorValue = str(calculatorValue)
    elif str(num) == '0' and calculatorValue == '0':
        pass
    elif str(num) != '0' and calculatorValue == '0':
        calculatorValue = str(num)
        currentInput.set(calculatorValue)
    elif calculatorValue != '0':
        calculatorValue += str(num)
        currentInput.set(calculatorValue)

def setDecimal(dot):
    global calculatorValue
    if isinstance(calculatorValue, float):
        calculatorValue = str(calculatorValue)
    if dot not in calculatorValue:
        calculatorValue += dot
        currentInput.set(calculatorValue)
    else:
        pass

def equals():
    global total
    if calculatorValue != 0 and total == 0:
        currentInput.set(calculatorValue)
    else:
        currentInput.set(str(total))

def add():
    global calculatorValue
    global total


def subtract():
    pass

def multiply():
    pass

def divide():
    pass

def addParentheses(parentheses):
    pass

def deleteDigit():
    global calculatorValue
    if len(calculatorValue) > 1:
        calculatorValue = calculatorValue[:-1]
        currentInput.set(calculatorValue)
    elif len(calculatorValue) == 1 or calculatorValue == '0':
        calculatorValue = '0'
        currentInput.set(calculatorValue)

def clear():
    global calculatorValue
    global total
    calculatorValue = '0'
    total = 0
    currentInput.set(calculatorValue)

if __name__ == '__main__':
    mainWindow = tkinter.Tk()
    mainWindow.geometry('412x490+0+600')
    mainWindow.title('Calculator')
    currentInput = tkinter.StringVar()
    mainWindow.resizable(width = False, height = False)
    top_frame = tkinter.Frame(mainWindow)
    bottom_frame = tkinter.Frame(mainWindow)
    entry = tkinter.Entry(top_frame, width = 50, font = 'Verdana, 40', textvariable = currentInput)
    currentInput.set(calculatorValue)
    entry.pack()

    button0 = tkinter.Button(bottom_frame, text = '0', width = 28, height = 4, command = lambda: setDigit(0))
    button1 = tkinter.Button(bottom_frame, text = '1', width = 13, height = 4, command = lambda: setDigit(1))
    button2 = tkinter.Button(bottom_frame, text = '2', width = 13, height = 4, command = lambda: setDigit(2))
    button3 = tkinter.Button(bottom_frame, text = '3', width = 13, height = 4, command = lambda: setDigit(3))
    button4 = tkinter.Button(bottom_frame, text = '4', width = 13, height = 4, command = lambda: setDigit(4))
    button5 = tkinter.Button(bottom_frame, text = '5', width = 13, height = 4, command = lambda: setDigit(5))
    button6 = tkinter.Button(bottom_frame, text = '6', width = 13, height = 4, command = lambda: setDigit(6))
    button7 = tkinter.Button(bottom_frame, text = '7', width = 13, height = 4, command = lambda: setDigit(7))
    button8 = tkinter.Button(bottom_frame, text = '8', width = 13, height = 4, command = lambda: setDigit(8))
    button9 = tkinter.Button(bottom_frame, text = '9', width = 13, height = 4, command = lambda: setDigit(9))
    button_dot = tkinter.Button(bottom_frame, text = '.', width = 13, height = 4, command = lambda: setDecimal('.'))
    button_equal = tkinter.Button(bottom_frame, text = '=', width = 13, height = 4, command = lambda: equals())
    button_plus = tkinter.Button(bottom_frame, text = '+', width = 13, height = 4, command = lambda: add())
    button_minus = tkinter.Button(bottom_frame, text = '-', width = 13, height = 4, command = lambda: subtract())
    button_multiply = tkinter.Button(bottom_frame, text = 'X', width = 13, height = 4, command = lambda: multiply())
    button_divide = tkinter.Button(bottom_frame, text = '/', width = 13, height = 4,command = lambda: divide())
    button_back = tkinter.Button(bottom_frame, text = 'BACK', width = 28, height = 4, command = lambda: deleteDigit())
    button_clear = tkinter.Button(bottom_frame, text = 'C', width = 28, height = 4, command = lambda: clear())
    button_left_parentheses = tkinter.Button(bottom_frame, text = '(', width = 13, height = 4, command = lambda: addParentheses('('))
    button_right_parentheses = tkinter.Button(bottom_frame, text = ')', width = 13, height = 4, command = lambda: addParentheses(')'))
    button_percent = tkinter.Button(bottom_frame, text = '%', width = 13, height = 4)

    button0.grid(row = 6, column = 0, columnspan = 2)
    button1.grid(row = 5, column = 0)
    button2.grid(row = 5, column = 1)
    button3.grid(row = 5, column = 2)
    button4.grid(row = 4, column = 0)
    button5.grid(row = 4, column = 1)
    button6.grid(row = 4, column = 2)
    button7.grid(row = 3, column = 0)
    button8.grid(row = 3, column = 1)
    button9.grid(row = 3, column = 2)
    button_clear.grid(row = 2, column = 1)
    button_dot.grid(row = 6, column = 2)
    button_equal.grid(row = 6, column = 3)
    button_plus.grid(row = 2, column = 3)
    button_minus.grid(row = 3, column = 3)
    button_multiply.grid(row = 4, column = 3)
    button_divide.grid(row = 5, column = 3)
    button_back.grid(row = 2, column = 2)
    button_percent.grid(row = 2, column = 2)
    button_left_parentheses.grid(row = 2, column = 0)
    button_right_parentheses.grid(row = 2, column = 1)
    button_clear.grid(row = 1, column = 0, columnspan = 2)
    button_back.grid(row = 1, column = 2, columnspan = 2)

    top_frame.pack()
    bottom_frame.pack()
    mainWindow.mainloop()