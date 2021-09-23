from actions import actions
from output import start, clean


def main():
    clean()
    start()
    clean()
    actions()

if __name__ == "__main__":
    main()