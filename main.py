# a script to print hello world

def say_hello():
    print("Hello World")

def say_goodbye():
    print("Goodbye World")

    # sleep for 1 minute to simulate buggy code
    import time
    time.sleep(60)

if __name__ == "__main__":
    say_hello()