from add_setup import add_setup
from read_setup import readsetup

def main():
    while True:
        use = input("What do you want to do? [A] = 'Add' / [M] = 'Modify' / [R] = 'Read' / [Q] = 'Quit' ").strip().upper()
        if use == "A":
            add_setup()
        elif use == "M":
            try:
                modify_setup()
            except ValueError:
                print("Function doesn't exist yet")
                break
        elif use == "R":
            try:
                readsetup()
            except ValueError:
                print("Function doesn't exist yet")
                break
        else:
            break


if __name__ == "__main__":
    main()