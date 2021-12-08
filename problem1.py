# Question: Evaluate postfix expression using a stack

import operator

class Evaluate:

    def __init__ (self, orgininal_exp):
        self.stack = []
        self.original_exp = orgininal_exp
        self.ops_dic = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv,
    }

    def splitExpression(self, exp):
        exp = self.original_exp
        return exp.split()

    def addToStack(self, value):
        self.stack.append(value)

    def doOperation(self, operator):
        val_1 = int(self.stack.pop())
        val_2 = int(self.stack.pop())
        return self.ops_dic[operator](val_2, val_1)

    def solve(self):
        for i in range(len(self.splitExpression(self.original_exp))):
            splitExp = self.splitExpression(self.original_exp)
            if splitExp[i].isdigit():
                self.addToStack(int(splitExp[i]))
            else:
                self.addToStack(self.doOperation(splitExp[i]))
        return self.stack

# Solution Example 1

obj1 = Evaluate("22 3 1 * + 9 -")
print(obj1.solve())

# Solution Example 2

obj2 = Evaluate("2 8 * 3 - 4 + 3 2")
print(obj2.solve())

# Solution Example 3

obj3 = Evaluate("4 8 2 / 1 * 9 3 +")
print(obj3.solve())
        





