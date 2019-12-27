from calculator import *


class Calculator:
    assembly = model.Assembly(input.Input.get_data())
    view = view.View("Result:" + assembly.calculate_pol_expression())
    print(view)
