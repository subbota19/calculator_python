import re


# error handler
class Error:
    def __init__(self, record):
        self.record = record

    def check_record(self):
        if re.findall(r'[A-Za-z!@#$%&]', self.record):
            return 'unknown arguments in expression', True
        if len(re.findall(r'[(]', self.record)) != len(re.findall(r'[)]', self.record)):
            return 'expression contain extra bracket', True
        if len(re.findall(r'[-+*/^]', self.record)) != len([x for x in re.split(r'[^\d]', self.record) if x]) - 1:
            return 'expression contain extra numbers or operations', True
        return None, False
