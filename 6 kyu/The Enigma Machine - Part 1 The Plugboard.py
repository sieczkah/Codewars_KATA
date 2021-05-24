"""https://www.codewars.com/kata/5523b97ac8f5025c45000900"""


class Plugboard(object):
    def __init__(self, wires=''):
        if self.validate(wires):
            self.wires = {wires[i]: wires[i + 1] for i in range(0, len(wires), 2)}
            self.wires.update({value: key for key, value in self.wires.items()})
        else:
            raise Exception("Too many wires defined")
                
    def process(self, c):
        return self.wires.get(c, c)
    
    @staticmethod
    def validate(wires):
        req = [len(wires) <= 20, len(set(wires)) == len(wires)]
        return all(req)
