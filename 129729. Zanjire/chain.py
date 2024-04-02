class Chain:
    def __init__(self, param):
        self.ans = param
        self.type = str(type(param))
        if 'float' in self.type:
            self.type = str(type(0))
        if not ("str" in self.type or "int" in self.type):
            raise Exception("invalid operation")

    def __call__(self, param):
        tt = str(type(param))
        if 'float' in tt:
            tt = str(type(0))
        if (tt == self.type):
            if 'int' in self.type:
                self.ans += param
            else:
                self.ans += " " + param
        else:
            raise Exception("invalid operation")
        return self

    def __eq__(self, __o):
        return self.ans == __o

    def __repr__(self):
        if ('int' in self.type and int(self.ans) == self.ans):
            return str(int(self.ans))
        if ('str' in self.type):
            return f"'{self.ans}'"
        return str(self.ans)


c = Chain('Ali')('Safinal')('is')('the')('best.')
print(c)
