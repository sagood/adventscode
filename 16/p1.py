class Packet:
    def __init__(self, data):
        if isinstance(data, str):
            h_size = len(data) * 4
            bin_input = (bin(int(data, 16))[2:]).zfill(h_size)
            self.bin_input = iter(bin_input)
        else:
            self.bin_input = iter(data)

        self.sub_packets = []
        self.packet_len = 0
        self.version = self.read_num(3)
        self.type_id = self.read_num(3)

        if self.type_id == 4:
            res = ""
            while True:
                num = self.get_bits(5)
                res += num[1:]
                if num[0] == "0":
                    break
            self.value = int(res, base=2)
        else:
            if self.get_bits(1) == "0":
                length = self.read_num(15)
                while length > 0:
                    self.sub_packets.append(Packet(self.bin_input))
                    self.packet_len += self.sub_packets[-1].packet_len
                    length -= self.sub_packets[-1].packet_len
            else:
                count = self.read_num(11)
                for _ in range(count):
                    self.sub_packets.append(Packet(self.bin_input))
                    self.packet_len += self.sub_packets[-1].packet_len

    def version_sum(self):
        return self.version + sum(item.version_sum() for item in self.sub_packets)

    def read_num(self, n):
        return int(self.get_bits(n), base=2)

    def get_bits(self, n):
        self.packet_len += n
        return "".join(next(self.bin_input) for _ in range(n))


def main():
    with open('in.txt') as f:
        lines = list(map(str.strip, f.readlines()))
        line = lines[0]

        p = Packet(line)
        print(p.version_sum())


if __name__ == '__main__':
    main()
