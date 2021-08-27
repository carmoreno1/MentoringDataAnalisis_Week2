import itertools as it

class Exercises():
    def __init__(self):
        self.MIN_DRIVING_AGE = 18
        self.VALID_COLORS =['blue', 'yellow', 'red']
        self.text = ''

    def is_able_to_drive(self):
        try:
            name = input("Write your name: ")
            age = int(input("Write your age: "))
            print(f"{name} is allowed to drive") if age >= self.MIN_DRIVING_AGE else print(f"{name} is not allowed to drive")
        except ValueError as e:
            print(f"An error has happened {e}")

    def check_color(self):
        try:
            while self.text != 'quit':
                self.text = input("Write a color: ").lower()
                if self.text == 'quit':
                    print("bye")
                    break
                elif self.text in self.VALID_COLORS:
                    print(self.text)
                else:
                    print("Not a valid color")
        except Exception as e:
            print(f"An error has happened {e}")

    def zen_python(self):
        zen_text = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
        """
        try:
            zen_list = list(it.chain(zen_text))
            for index, item in enumerate(it.chain(zen_text)):
                if item.lower() in 'aeiou':
                    zen_list[index] = '*'

            print(''.join(zen_list))
        except Exception as e:
            print(f"An error has happened {e}")

if __name__ == '__main__':
    exercises = Exercises()
    # exercises.is_able_to_drive()
    # exercises.check_color()
    # exercises.zen_python()