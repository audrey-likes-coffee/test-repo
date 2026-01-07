import sys

def hello(name="World"):
    return f"Hello, {name}!"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"
    print(hello(name))