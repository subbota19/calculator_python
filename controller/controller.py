import sys
from calculator_python.model import *
from calculator_python.view import *


class Calculator:
    record = input.Input.get_data()
    error, bool_ = error.Error(record).check_record()
    if bool_:
        print(error)
        sys.exit()
    assembly = model.Assembly(list(record))
    view = view.View("Result:" + assembly.calculate_pol_expression())
    print(view)
