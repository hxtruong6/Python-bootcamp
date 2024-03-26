#two.py
import one

print("Top level in Two.py")

one.func()

if __name__ == "__main__":
    print("Two.py run directly!")
else:
    print("Two.py was imported!")
