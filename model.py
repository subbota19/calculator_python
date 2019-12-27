class Expression:
    @classmethod
    def operation(cls, arg_1, arg_2, sign):
        dict_operation = {'+': arg_1 + arg_2, '-': arg_1 - arg_2, '*': arg_1 * arg_2, '/': arg_1 / arg_2,
                          '^': pow(arg_1, arg_2)}
        return dict_operation[sign]


class Assembly:
    def __init__(self, record_numbers):
        self.record_numbers = record_numbers

    @classmethod
    def is_integer(cls, element):
        try:
            return bool(int(element))
        except ValueError:
            pass

    def _assemble_pol_expression(self):
        stack_with_pl_record = []
        stack_with_operation = []
        using_operation = {'+': 0, '-': 0, '*': 1, '^': 2, '/': 1, '(': -1, ')': -1}

        for x in self.record_numbers:
            if Assembly.is_integer(x):
                stack_with_pl_record.append(int(x))
            else:
                if x == ')':
                    for i in stack_with_operation[::-1]:
                        if i == '(':
                            break
                    stack_with_pl_record.append(str(stack_with_operation.pop()))
                    stack_with_operation.pop()
                    continue
                if not stack_with_operation or x == '(':
                    pass
                elif using_operation[x] <= using_operation[str(stack_with_operation[-1])]:
                    if using_operation[x] == 1:
                        stack_with_pl_record.append(str(stack_with_operation.pop(-1)))
                    else:
                        stack_with_pl_record.append(str(stack_with_operation.pop(-1)))
                        if stack_with_operation and stack_with_operation[-1] != '(':
                            stack_with_pl_record.append(str(stack_with_operation.pop()))
                stack_with_operation.append(x)

        return stack_with_pl_record + stack_with_operation[::-1]

    def calculate_pol_expression(self):
        stack_with_pl_record = self._assemble_pol_expression()
        result_stack = []
        for x in stack_with_pl_record:
            try:
                result_stack.append(int(x))
            except ValueError:
                result_stack.append(Expression.operation(result_stack.pop(-2), result_stack.pop(-1), x))
        return str(result_stack[0])
