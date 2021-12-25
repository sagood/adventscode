import collections


def main():
    with open('in.txt') as f:
        lines = list(map(str.strip, f.readlines()))
        cubes = collections.Counter()
        for line in lines:
            turn_on = 1
            if 'off' in line:
                turn_on = -1
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

            update = collections.Counter()
            for (x0, x1, y0, y1, z0, z1), on_off in cubes.items():
                x0_intersect = max(x_start, x0)
                x1_intersect = min(x_end, x1)
                y0_intersect = max(y_start, y0)
                y1_intersect = min(y_end, y1)
                z0_intersect = max(z_start, z0)
                z1_intersect = min(z_end, z1)

                if x0_intersect <= x1_intersect and y0_intersect <= y1_intersect and z0_intersect\
                        <= z1_intersect:
                    update[(x0_intersect, x1_intersect, y0_intersect, y1_intersect, z0_intersect,
                            z1_intersect)] -= on_off

            if turn_on > 0:
                update[(x_start, x_end, y_start, y_end, z_start, z_end)] += turn_on

            cubes.update(update)

        print(sum((x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * on_off
                  for (x0, x1, y0, y1, z0, z1), on_off in cubes.items()))


if __name__ == '__main__':
    main()
