import sys


def sale(argv):
    program, *args = argv
    result = str()
    with open('bakery.csv', 'r', encoding='utf-8') as fail:
        line_list = fail.read().splitlines()
        if len(args) == 0:
            args.append(1)
            args.append(len(line_list))
        elif len(args) == 1:
            args.append(len(line_list))
        start = int(args[0])
        stop = int(args[1])
        if start == 0 or start > len(line_list) or stop < start or stop > len(line_list):
            return result
        for el in line_list[start - 1: stop]:
            result += f'{el}\n'
        return result.strip('\n')
print(sale(sys.argv))
