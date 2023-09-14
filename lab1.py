## 1 task
intNum = 10
floatNum = 10.5
boolType = True
stringType = "Maksim Dukal"
print(intNum, type(intNum), floatNum, type(floatNum), boolType, type(boolType), stringType, type(stringType))

## 2 task

first = int(input("введи перше"))
second = int(input("веди друге"))
operation = input("введи знак")

match operation:
    case "+":
        print(first+second)
    case "-":
        print(first-second)    
    case "*":
        print(first*second)
    case "/":
        print(first/second)
    case _ :
        print("введи шось нормальне")


## 3 task

res = 0
while True:
    print("наказуйте")
    print("1 - додавання")
    print("2 - віднімання")
    print("3 - множення")
    print("4 - ділення")
    print("6 - вихід")
    choise = input("введіть свій вибір")
    match choise:
        case "1":
            res = res + int(input("введіть число"))
            print(res)
        case "2":
            res = res - int(input("введіть число"))
            print(res)
        case "3":
            res = res * int(input("введіть число"))
            print(res)
        case "4":
            res = res / int(input("введіть число"))
            print(res)
        case 6 :
            break
        case _ :
            print("введи шось нормальне")
print(res)







