

def main():
    with open('in.txt') as f:
        line = f.readline()
        fishes = list(map(int, line.split(',')))
        for _ in range(80):
            new_fishes = []
            for i in range(len(fishes)):
                cur_time = fishes[i]
                if cur_time == 0:
                    cur_time = 6
                    new_fishes.append(8)
                else:
                    cur_time -= 1
                fishes[i] = cur_time
            if new_fishes:
                fishes += new_fishes
                new_fishes.clear()

        print(len(fishes))



if __name__ == '__main__':
    main()