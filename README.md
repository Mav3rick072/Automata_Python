#Automatas Finitos Deterministas con Salida
class MooreAutomaton:
    def __init__(self):
        self.state = 'q0'  # Estado inicial
        self.output = []   # Salida generada

    def transition(self, char):
        if self.state == 'q0':
            if char == '1':
                self.state = 'q1'
                self.output.append('0')  # No cambia la salida aún
            else:
                self.output.append(char)
        elif self.state == 'q1':
            if char == '1':
                self.state = 'q2'
                self.output[-1] = '0'  # Cambia el último '0' agregado
                self.output.append('0')
            else:
                self.state = 'q0'
                self.output.append(char)
        elif self.state == 'q2':
            self.state = 'q0'
            if char == '1':
                self.state = 'q1'
                self.output.append('0')
            else:
                self.output.append(char)

    def process_input(self, input_string):
        for char in input_string:
            self.transition(char)
        return ''.join(self.output)
