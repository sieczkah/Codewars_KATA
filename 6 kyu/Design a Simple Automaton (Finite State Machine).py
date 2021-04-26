"""https://www.codewars.com/kata/5268acac0d3f019add000203"""

class Automaton(object):

    def __init__(self):
        self.states = {'q1': {'1': 'q2', '0': 'q1'},
                       'q2': {'1': 'q2', '0': 'q3'},
                       'q3': {'1': 'q2', '0': 'q2'}}
        self.current_state = 'q1'
                       

    def read_commands(self, commands):
        for command in commands:
            self.current_state = self.states[self.current_state][command]
        return self.current_state == 'q2'
        # Return True if we end in our accept state, False otherwise

my_automaton = Automaton()

# Do anything necessary to set up your automaton's states, q1, q2, and q3.
