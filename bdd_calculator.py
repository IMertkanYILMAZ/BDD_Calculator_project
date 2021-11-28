

class bdd_calc1:
    def __init__(self):
        self.result = 0
        self.numb1 = None
        self.numb2 = None
        self.equ1 = None
        self.type1 = None

    def ask_for_type(self):
        if self.type1 in ["Sum", "Sub", "Mult", "Div"]:
            return True
        elif self.type1 == "scientific":
            return True
        else:
            return "Wrong Input"

    def input_check(self):
        if isinstance(self.numb1, (float,int)) and isinstance(self.numb2, (float, int)):
            return True

    def calc_sum(self):
        if self.input_check():
            self.result = (self.numb1 + self.numb2)
            return float(self.result)
        else:
            return "Wrong Input"

    def calc_subt(self):
        if self.input_check():
            self.result = (self.numb1 - self.numb2)
            return self.result
        else:
            return "Wrong Input"

    def calc_mult(self):
        if self.input_check():
            self.result = (self.numb1 * self.numb2)
            return self.result
        else:
            return "Wrong Input"

    def calc_div(self):
        self.input_check()
        if self.numb2 == 0:
            return "ZeroDivisionError"
        else:
            if self.input_check():
                self.result = (self.numb1 / self.numb2)
                return self.result
            else:
                return "Wrong Input"

    def scientific_calculator(self):
        try:
            return eval(self.equ1)
        except:
            return "Wrong Input"