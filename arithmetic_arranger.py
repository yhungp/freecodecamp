def arithmetic_arranger(l: list, show: bool):
    if l.__len__() > 5: return "Error: Too many problems."

    solutions = []
    
    for op in l:
        if "+" in op:
            op = str(op).replace(" ", "").split("+")

            if not op[0].isnumeric() or not op[1].isnumeric(): return "Error: Numbers must only contain digits."
            if op[0].__len__() > 4 or op[1].__len__() > 4: return "Error: Numbers cannot be more than four digits."

            result = int(op[0]) + int(op[1])
            solutions.append(formatter(op[0], op[1], result, "+"))

        elif "-" in op:
            op = str(op).replace(" ", "").split("-")
            
            if not op[0].isnumeric() or not op[1].isnumeric(): return "Error: Numbers must only contain digits."
            if op[0].__len__() > 4 or op[1].__len__() > 4: return "Error: Numbers cannot be more than four digits."
            
            result = int(op[0]) - int(op[1])
            solutions.append(formatter(op[0], op[1], result, "+"))

        elif "*" in op or "/" in op:
            return "Error: Operator must be '+' or '-'."

    solutions = ["    ".join([ele[i] for ele in solutions] )for i in range(4) ]
    solutions = "\n".join(solutions)

    if show: print(solutions)

    return solutions

        
def formatter(val1, val2, result, operation):
    if str(val1) >= str(val2):
        width = str(val1).__len__() + 2
    else:
        width = str(val2).__len__() + 2

    line1 = " " * ( width - len(str(val1))) + str(val1)
    line2 = operation + " " * ( width - len(str(val2)) - 1) + str(val2)
    line3 = "-" * width

    if result >= 0: line4 = " " * ( width - len(str(result))) + str(result)
    else: line4 = " " * ( width - len(str(result))) + str(result)

    return [line1, line2, line3, line4]
