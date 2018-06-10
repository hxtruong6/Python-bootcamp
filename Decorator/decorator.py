def func_decorator(origin_func):
    def new_func():
        print("Some code before.")
        origin_func()
        print("Some code after.")

    return new_func()

@func_decorator
def function_need_decorator():
    print("Hello. I am a decorator!")
