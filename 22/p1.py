
def main():
    with open('in.txt') as f:
        lines = list(map(str.strip, f.readlines()))
        on_cubes = set()
        for line in lines:
            turn_on = True
            if 'off' in line:
                turn_on = False
            parts = line.split(',')
            x_part = parts[0].split('x=')[1].split('..')
            x_start = int(x_part[0])
            x_end = int(x_part[1])
            y_part = parts[1].split('y=')[1].split('..')
            y_start = int(y_part[0])
            y_end = int(y_part[1])
            z_part = parts[2].split('z=')[1].split('..')
            z_start = int(z_part[0])
            z_end = int(z_part[1])

            if x_start < -50 or x_end > 51 or y_start < -50 or y_end > 51 or z_start < -50 or \
                    z_end > 51:
                continue

            for x in range(x_start, x_end + 1):
                for y in range(y_start, y_end + 1):
                    for z in range(z_start, z_end + 1):
                        cur = (x, y, z)
                        if turn_on:
                            if cur not in on_cubes:
                                on_cubes.add(cur)
                        else:
                            if cur in on_cubes:
                                on_cubes.remove(cur)

        print(len(on_cubes))


if __name__ == '__main__':
    main()
