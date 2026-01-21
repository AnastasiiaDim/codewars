import operator

def arithmetic(a, b, op_name):
    ops = {
        "add": operator.add,
        "subtract": operator.sub,
        "multiply": operator.mul,
        "divide": operator.truediv,
    }
    return ops[op_name](a, b)