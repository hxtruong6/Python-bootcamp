#one.py
print("Top level in One.py")


def func():
    print("Function in One.py")


if __name__ == "__main__" :
    print("One.py run directly!")
else:
    print("One.py was imported!")
