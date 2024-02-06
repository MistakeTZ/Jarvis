from extractor import NumberExtractor

comma = (
    "и",
    "запятая",
)
equal = (
    "равно",
    "равен",
)
acts = {
    '*': (
        "умножить на",
        "умножить",
        "помножить на",
        "помножить",
        "на"
    ),
    '/': (
        "поделить на",
        "поделить",
        "разделить на",
        "разделить"
    ),
    '+': (
        "плюс",
        "прибавить к",
        "прибавить"
    ),
    '-': (
        "вычесть",
        "-"
    )
}
drob_first = {
    "десять тысячных|десяти тысячная": 10**4,
    "сто тысячных|сто тысячная": 10**5,
    "десять миллионных|десяти миллионная": 10**7,
    "сто миллионных|сто миллионная": 10**8
}
drob = {
    "вторых|вторая": 2,
    "третьих|третья": 3,
    "четвертых|четвертая": 4,
    "пятых|пятая": 5,
    "шестых|шестая": 6,
    "седьмых|седьмая": 7,
    "восьмых|восьмая": 8,
    "девятых|девятая": 9,
    "десятых|десятая": 10,
    "оддинадцатых|одиннадцатая": 11,
    "двенадцатых|двенадцатая": 12,
    "тринадцатых|тринадцатая": 13,
    "четырнадцатых|четырнадцатая": 14,
    "пятнадцатых|пятнадцатая": 15,
    "шестнадцатых|шестнадцатая": 16,
    "семнадцатых|семнадцатая": 17,
    "восемнадцатых|восемнадцатая": 18,
    "девятнадцатых|девятнадцатая": 19,
    "двадцатых|двадцатая": 20,
    "сотых|сотая": 100,
    "тысячных|тысячная": 1000,
    "миллионных|миллионная": 10**6,
    "миллиардных|миллиардная": 10**9
}
var = {
    "икс": None,
    "игрек": None,
    "зет": None,
    "а": None,
    "б": None,
    "це": None,
    "де|да": None,
    "кей|ка": None,
    "ай": None,
    "джей": None
}


def calculate(string):
    eq = None
    for el in equal:
        if el in string:
            a = string.split(" " + el + " ")
            if len(a) != 2:
                return "Введено неверное число аргументов"
            eq = is_cell(a[0])
            if eq == None:
                return "Не найдена ячейка записи"
            string = a[1]
            break

    act = None
    args = []

    for key in acts.keys():
        for el in acts[key]:
            if el in string:
                act = key
                args = string.split(" " + el + " ")
                break
    if act == None:
        if " минус " in string:
            act = '-'
            args = string.split(" минус ")
        elif eq != None:
            args.append(string)

    print(act)
    print(args)
    if eq == None and (act == None or len(args) != 2):
        return "Введено неверное число аргументов"
    
    arguments = []
    after_comma = 0
    for i in range (len(args)):
        cell = is_cell(args[i])
        if cell != None:
            arguments.append(var[cell])
        else:
            num, after = to_num(args[i])
            after_comma = max(after, after_comma)
            if num != None:
                arguments.append(num)
            else:
                phrase = ""
                if len(args) == 2:
                    phrase = ["первый ", "второй "][i]
                return phrase + "аргумент не распознан"
    print(arguments)
            
    res = 0
    if len(arguments) == 1:
        res = arguments[0]
    else:
        if act == '*':
            res = arguments[0] * arguments[1]
        elif act == '/':
            res = arguments[0] / arguments[1]
        elif act == '+':
            res = arguments[0] + arguments[1]
        elif act == '-':
            res = arguments[0] - arguments[1]
        res = round(res, after_comma + 1)
    result = str(res)
    '''num2text(res)'''
    
    if eq != None:
        var[eq] = res
        return "В ячейку {} занесено число {}".format(eq.split('|')[0], result)
    else:
        return result

        
def is_cell(cell):
    for key in var.keys():
            a = key.split('|')
            if cell in a:
                return key
    return None


def to_num(string):
    if "минус" in string:
        mul = -1
        string = string.split("минус ")[1]
    else:
        mul = 1

    cel = ""
    after_point = ""
    divider = 1
    for el in comma:
        if " " + el + " " in string:
            a = string.split(" " + el + " ")
            cel = a[0]
            after_point = a[1]
            divider = -1
            break
    if "целых" in string:
        a = string.split(" целых ")
        cel = a[0]
        after_point = a[1]
    if cel == "":
        cel = string

    after_point_num = None
    if after_point != "":
        cel_num, _ = parse_numbers(cel, 1)
        if cel_num == None:
            return None, 0
        if divider == -1:
            after_point_num = parse_numbers(after_point, 1)
            divider = len(str(after_point_num))
        else:
            after_point_num, divider = parse_numbers(after_point, 2)
    else:
        cel_num, divider = parse_numbers(cel, 0)
    if cel_num == None or (after_point_num == None and after_point != ""):
        return None, 0
    
    if after_point_num == None:
        res = cel_num / divider
    else:
        res = cel_num + after_point_num / divider
    res *= mul
    
    if after_point_num == None and divider == 1:
        return res, 0
    else:
        if divider % 10 == 0:
            return res, len(str(res).split('.')[1])
        else:
            return res, 1

    
def parse_numbers(string, type):
    '''
    type: 1 = целое 2 = дробное 0 = любое
    '''
    print("Строка: {}\nТип: {}".format(string, type))

    replaced = 1
    if type != 1:
        for key in drob_first.keys():
            for el in key.split('|'):
                if el in string:
                    string = string.replace(el, "")
                    replaced = drob_first[key]
                    break
        if replaced == 1:
            for key in drob.keys():
                for el in key.split('|'):
                    if el in string:
                        string = string.replace(el, "")
                        replaced = drob[key]
                        break
        if replaced == 1 and type == 2:
            return None, 1

    inp = to_n(string)
    if inp.isnumeric():
        return int(inp), replaced
    return None, 1

def to_n(text):
    return extractor.replace_groups(text).replace(" ", "")
    

if __name__ == "__main__":
    extractor = NumberExtractor()

    while True:
        calc = input("Введите пример: ")
        print(calculate(calc))