from add import add
from division import div
from programm_vichitaet import main as sub
from umnoenie import mul

def main():
    print("Hello, World!")
    cmd = input()
    {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }[cmd]()

if __name__ == '__main__':
    main()
