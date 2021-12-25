

def main():
    with open('in.txt') as f:
        lines = f.readlines()
        m = len(lines)
        n = len(lines[0]) - 1
        oxygen = set()
        co2 = set()

        for line in lines:
            oxygen.add(line.strip())
            co2.add(line.strip())

        index = 0
        while len(oxygen) > 1:
            zero = 0
            one = 0
            o = list(oxygen)
            for i in range(0, len(o)):
                if o[i][index] == '0':
                    zero += 1
                else:
                    one += 1

            if zero > one:
                for item in o:
                    if item[index] == '1':
                        oxygen.remove(item)
            else:
                for item in o:
                    if item[index] == '0':
                        oxygen.remove(item)
            index += 1

        index = 0
        while len(co2) > 1:
            zero = 0
            one = 0
            c = list(co2)
            for j in range(0, len(c)):
                if c[j][index] == '0':
                    zero += 1
                else:
                    one += 1
            if zero > one:
                for item in c:
                    if item[index] == '0':
                        co2.remove(item)
            else:
                for item in c:
                    if item[index] == '1':
                        co2.remove(item)
            index += 1

        n1 = int(oxygen.pop(), base=2)
        n2 = int(co2.pop(), base=2)
        print(n1 * n2)


if __name__ == '__main__':
    main()