from art import tprint
from task import Heloo

class NewHello(Heloo):
    def tprint(self):
        print("tprint func")

my_hello_obj = NewHello()

my_hello_obj.tprint()

my_hello_obj.greet()
tprint("PYTHON")