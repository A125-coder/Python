if __name__ == "__main__":
    summ
    minus
    division
    mult


def summ(params):
    res = 0
    for i in params:
        res += i
    return res


def minus(params):
    res = 0
    params[0] = -params[0]
    for i in params:
        res -= i
    return res


def mult(params):
    res = 1
    for i in params:
        res *= i
    return res


def division(params):
    res = params[0]

    for i in params[1:]:
        if i == 0:
            print('Division by zero!')
            break
        elif i > 0:
            res = res / i
        return res
