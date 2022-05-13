"""
Program to test and view de results of logic operations
"""

def andOperator(ValA, ValB)
    andOp = ValA and ValB
    return andOp

def orOperator(ValA, ValB)
    orOp = ValA or ValB
    return orOp

def main():
    bool = (True, False)
    operator = ("and", "or")
    for k in operator:
        for i in bool:
            for j in bool:
                if k == "and":
                    print(f"{j} and {i} is {andOperator(j,i)}")
                else:
                    print(f"{j} or {i} is {orOperator(j,i)}")

if __name__ == '__main__':
    main()
