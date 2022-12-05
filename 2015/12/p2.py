import json


def n(obj):
    if type(obj) is dict:
        if 'red' in obj.values():
            return 0
        return sum(map(n, obj.values()))

    if type(obj) is list:
        return sum(map(n, obj))

    if type(obj) is int:
        return obj

    return 0


def main():
    with open('in.json', 'r') as f:
        data = json.loads(f.read())
        res = n(data)
        print(res)


if __name__ == '__main__':
    main()
