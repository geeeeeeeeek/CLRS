__author__ = 'Tong'

priority = {"+": 0, "-": 0, "*": 1, "/": 1, "mod": 1, "(": -99, ")": -999}
n_operands = {"+": 2, "-": 2, "*": 2, "/": 2, "mod": 2}


def get_next(infix):
    # Avoid accidental space
    infix = infix.strip()
    # Find the most adjacent operator
    index = float("inf")
    operator = ""
    for op in priority:
        try:
            if index > infix.index(op):
                index = int(infix.index(op))
                operator = op
        except ValueError:
            continue
    # If operator appears in the first position, return the operator.
    # Or, deal with operands first.
    if index == 0:
        infix = infix[len(operator):]
        return operator, "operator", infix
    elif index == float("inf"):
        return infix, "operand", ""
    else:
        operand = infix[:index]
        infix = infix[index:]
        return operand, "operand", infix


def infix_to_postfix(infix):
    postfix = []
    operator_stack = []
    while infix != "":
        nxt, typ, infix = get_next(infix)
        if typ == "operand":
            operand = nxt
            postfix.append(operand)
        elif typ == "operator":
            operator = nxt
            if operator == ")":
                # Pop elements after "("
                ptr = len(operator_stack) - 1
                while ptr >= 0:
                    if operator_stack[ptr] != "(":
                        postfix.append(operator_stack.pop())
                        ptr -= 1
                    else:
                        operator_stack.pop()
                        break
            elif operator == "(":
                operator_stack.append(operator)
            # If current operator has lower priority:
            elif operator_stack == [] or priority.get(operator_stack[len(operator_stack) - 1]) < priority.get(operator):
                operator_stack.append(operator)
            else:
                postfix.append(operator_stack.pop())
                operator_stack.append(operator)
    while operator_stack:
        postfix.append(operator_stack.pop())
    for each in operator_stack:
        postfix.append(each)
    return postfix


def postfix_calc(postfix):
    while len(postfix) != 1:
        # Find the most adjacent operator
        index = float("inf")
        operator = ""
        for op in n_operands:
            try:
                if index > postfix.index(op):
                    index = int(postfix.index(op))
                    operator = op
            except ValueError:
                continue
        # Here in the case given, only binary operators are required to deal with.
        if n_operands.get(operator) == 2:
            # Update the postfix removing dealt operands and operator and put in result.
            operand1 = postfix[index - 2]
            operand2 = postfix[index - 1]
            postfix = postfix[:index - 2] + postfix[index + 1:]
            postfix.insert(index - 2, eval(operand1 + operator.replace("mod", "%") + operand2).__str__())
    return postfix


# ##################################################### #
# #                      Test sets                    # #
# ##################################################### #
def run_tests():
    exprs = ["3+4+20-8", "9*8+7", "3-18mod7", "100-30/6", "9*8+7*5", "120/(5+3)", "100+30/(34mod3)", "9*8+(7+6)*5",
             "9*8+(7+6*(3+4*5))", "9.6*6+3", "9.5*8+37*5-(7+3*4+5)*4", "9.8*5+((3+1)*4+(2+3)*1.2)*3"]
    for expr in exprs:
        is_correct = (float(postfix_calc(infix_to_postfix(expr))[0]) == eval(expr.replace("mod", "%")))
        print("Test case " + exprs.index(expr).__str__() + ": " + is_correct.__str__())


def run_single_test(expr):
    print(">> " + expr + " = " + postfix_calc(infix_to_postfix("3-18mod7"))[0])


run_tests()
run_single_test("9.8*5+((3+1)*4+(2+3)*1.2)*3")