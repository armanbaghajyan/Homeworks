import string
import random
class Stack:
    def __init__(self):
        self.arr = []

    def push(self,value):
        self.arr.append(value)

    def pop(self):
        if not self.arr:
            raise "Empty stack"
        return self.arr.pop()

    def top(self):
        if not self.arr:
            raise "Empty stack"
        return self.arr[-1]

    def pri(self):
        print(self.arr)

    def is_empty(self):
        return not bool(self.arr)

def is_volid(string,perent):
    open_per = []
    close_per = []
    st = Stack()
    valid = False
    for per in perent:
        open_per.append(per[0])
        close_per.append(per[1])

    if string[0] in close_per:
        return False
    open_count = 0
    close_count = 0
    for letter in string:
        if letter in open_per:
            st.push(letter)
            open_count += 1
            valid = True
        elif letter in close_per:
            close_count += 1
            if not st.is_empty() and open_per[close_per.index(letter)] == st.top():
                st.pop()

    return close_count == open_count and valid and st.is_empty()

def test(test_count):
    char = list(string.ascii_lowercase) + [" ","(",")","[","]","{","}","<",">"]
    for _ in range(test_count):
        lenght_str = random.randint(5,20)
        lenght_pernt = random.randint(1, 4)
        test_string = "".join([random.choice(char) for _ in range(lenght_str)])
        test_pernt = [random.choice([("(", ")"), ("[", "]"), ("{", "}"), ("<", ">")]) for _ in range(lenght_pernt)]
        print("""String is.
{}""".format(test_string))
        print("""perentesis is.
{}""".format(test_pernt))
        try:
            assert is_volid(test_string,test_pernt)
        except:
            print("TEST NOT PASSED")
    print("TEST PASSED")

test(3)



