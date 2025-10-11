class iostring():
    def __init__(self):
        self.str1=""
    def get_string(self):
        self.str1=input("enter ur string: ")
    def print_string(self):
        print("result is: ",self.str1.upper())
string1=iostring()
string1.get_string()
string1.print_string()