import re

global memory
memory = '0'

def bt_to_int(bt):
    for a in range(1, len(bt)):
        if bt[a] not in ['0', '1', 'N']:
            raise ValueError()
        else:
            pass
    n = 0
    integer = 0
    while n < len(bt):
        if bt[len(bt) - n - 1] == 'N':
            digit = (-1)
        if bt[len(bt) - n - 1] == '0':
            digit = 0            
        if bt[len(bt) - n - 1] == '1':
            digit = 1
        integer = integer + (3 ** n) * digit
        n += 1
    return integer

def int_to_bt(n):
    bt = ''
    e = 0
    
    if n == 0:
        return '0'
    
    while abs(n) != (3 ** e):
        remainder = (n % (3 ** (e + 1))) / (3 ** e)

        if remainder == 2:
            remainder -= 3
            digit = 'N'
        else:
            remainder = int(remainder)
            digit = str(remainder)
        n -= (remainder * (3 ** e))
        bt = digit + bt
        e += 1
    num = n / (3 ** e)
    if num == -1:
        num = 'N'
    else:
        num = str(int(num))
    bt = num + bt

    return bt

def add(bt):
    global memory
    integer = bt_to_int(memory) + bt_to_int(bt)
    memory = int_to_bt(integer)
    return

def subtract(bt):
    global memory
    integer = bt_to_int(memory) - bt_to_int(bt)
    memory = int_to_bt(integer)
    return

def multiply(bt):
    global memory
    integer = bt_to_int(memory) * bt_to_int(bt)
    memory = int_to_bt(integer)
    return

def divide(bt):
    global memory
    if bt_to_int(bt) == 0:
        raise ZeroDivisionError()

    integer = int(bt_to_int(memory) / bt_to_int(bt))
    memory = int_to_bt(integer)
    return

def remainder(bt):
    global memory
    if bt_to_int(bt) == 0:
        raise ZeroDivisionError()

    integer = bt_to_int(memory) % bt_to_int(bt)
    memory = int_to_bt(integer)
    return

def negate():
    global memory
    integer = bt_to_int(memory) * (-1)
    memory = int_to_bt(integer)
    return

def store(bt):
    global memory
    memory = bt
    return

def memory_as_int():
    global memory
    return bt_to_int(memory)

def memory_as_bt():
    global memory
    return memory

def evaluate(string):
    global memory

    if string[0] not in ['+', '-', '*', '/', '%', '=']:
        raise Exception
    else:
        pass

    string = string.replace(' ', '')
    clean_list = []
    clean_list = re.split('(\w+)', string)
    clean_list.remove('')

    for n in range(0, len(clean_list)):
        if clean_list[n] == '=':
            store(clean_list[n+1])
        elif clean_list[n] == '+':
            add(clean_list[n+1])
        elif clean_list[n] == '-':
            subtract(clean_list[n+1])
        elif clean_list[n] == '*':
            multiply(clean_list[n+1])
        elif clean_list[n] == '/':
            divide(clean_list[n+1])
        elif clean_list[n] == '%':
            remainder(clean_list[n+1])

    return memory
            
def REPL():
    result = ''
    print('Please input. Input quit to exit: ')
    userInput = input()
    if userInput != 'quit':
        try:
            result = evaluate(userInput)
            print('memory = ', result)
            print('decimal = ', bt_to_int(result))
        except ZeroDivisionError:
            print('Division by zero')
        except ValueError:
            print('Invalid number')
        except Exception:
            print('Invalid input')


if __name__ == '__main__':
    REPL()
