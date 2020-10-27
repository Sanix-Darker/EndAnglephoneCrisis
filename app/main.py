from app.utils import *


def main():
    """

    The basic main method to send all over the time

    """

    try:
        while True:
            proceed()
    except KeyboardInterrupt:
        print("[x] Bot stoped")



if __name__ == "__main__":
    main()
