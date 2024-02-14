import sys
import generate_dummy_data


def main(args):
    if len(args) > 1 and args[1].isdigit():
        loop_num = int(args[1])
    else:
        loop_num = 10

    for _ in range(loop_num):
        generated = generate_dummy_data.generate()
        print(generated)


##
if __name__ == '__main__':
    main(sys.argv)
