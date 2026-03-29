art='''

                                                                                                                                                                   
    ,o888888o.           .8.          8 8888         ,o888888o.    8 8888      88 8 8888                  .8.    8888888 8888888888 ,o888888o.     8 888888888o.   
   8888     `88.        .888.         8 8888        8888     `88.  8 8888      88 8 8888                 .888.         8 8888    . 8888     `88.   8 8888    `88.  
,8 8888       `8.      :88888.        8 8888     ,8 8888       `8. 8 8888      88 8 8888                :88888.        8 8888   ,8 8888       `8b  8 8888     `88  
88 8888               . `88888.       8 8888     88 8888           8 8888      88 8 8888               . `88888.       8 8888   88 8888        `8b 8 8888     ,88  
88 8888              .8. `88888.      8 8888     88 8888           8 8888      88 8 8888              .8. `88888.      8 8888   88 8888         88 8 8888.   ,88'  
88 8888             .8`8. `88888.     8 8888     88 8888           8 8888      88 8 8888             .8`8. `88888.     8 8888   88 8888         88 8 888888888P'   
88 8888            .8' `8. `88888.    8 8888     88 8888           8 8888      88 8 8888            .8' `8. `88888.    8 8888   88 8888        ,8P 8 8888`8b       
`8 8888       .8' .8'   `8. `88888.   8 8888     `8 8888       .8' ` 8888     ,8P 8 8888           .8'   `8. `88888.   8 8888   `8 8888       ,8P  8 8888 `8b.     
   8888     ,88' .888888888. `88888.  8 8888        8888     ,88'    8888   ,d8P  8 8888          .888888888. `88888.  8 8888    ` 8888     ,88'   8 8888   `8b.   
    `8888888P'  .8'       `8. `88888. 8 888888888888 `8888888P'       `Y88888P'   8 888888888888 .8'       `8. `88888. 8 8888       `8888888P'     8 8888     `88. 

    '''


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

def modulus(n1,n2):
    return n1%n2

def floor(n1,n2):
    return n1//n2

def exponent(n1,n2):
    return n1**n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulus,
    "//":floor,
    "**":exponent,
}

# print(operations["*"](4, 8))


def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()

           







