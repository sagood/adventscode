

def main():
    with open('in.txt') as f:
        lines = f.readlines()
        m = len(lines)
        n = len(lines[0]) - 1
        gamma = ['0'] * n
        epsilon = ['0'] * n

        for i in range(n):
            zero = 0
            one = 0
            for j in range(m):
                if lines[j][i] == '0':
                    zero += 1
                else:
                    one += 1
            if zero > one:
                gamma[i] = '0'
                epsilon[i] = '1'
            else:
                gamma[i] = '1'
                epsilon[i] = '0'

        g = int(''.join(gamma), base=2)
        e = int(''.join(epsilon), base=2)
        print(g * e)


if __name__ == '__main__':
    main()