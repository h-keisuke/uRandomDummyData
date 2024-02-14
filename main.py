import sys
import generate_dummy_data

def main(args):
    if len(args) > 1 and args[1].isdigit():
        loopNum = int(args[1])
    else:
        loopNum = 10

    for _ in range(loopNum):
        generated = generate_dummy_data.generate()
        print(generated)

##
if __name__ == '__main__':
    main(sys.argv)
