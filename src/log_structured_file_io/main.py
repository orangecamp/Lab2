# 文件名: src/log_structured_file_io/main.py
import argparse
import json
import os


def main():
    arg_parser = argparse.ArgumentParser(description='Log structured file I/O')
    subparsers = arg_parser.add_subparsers(dest='command')

        # Set command
    arg_parser_set = subparsers.add_parser('set', help='Set a key-value pair')
    arg_parser_set.add_argument('key', type=str, help='Key')
    arg_parser_set.add_argument('value', type=str, help='Value')

        # Get command
    arg_parser_get = subparsers.add_parser('get', help='Get the value of a key')
    arg_parser_get.add_argument('key', type=str, help='Key')

        # Del command
    arg_parser_del = subparsers.add_parser('del', help='Delete a key-value pair')
    arg_parser_del.add_argument('key', type=str, help='Key')

    args = arg_parser.parse_args()
    filename = './data/store.kv'
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write('{}')

    with open('./data/store.kv', 'r') as f:
        data = json.load(f)
    if args.command == 'set':
        data[args.key] = args.value
    elif args.command == 'get':
        value = data.get(args.key)
        if value is None:
            print('Key not found')
        else:
            print(value)
    elif args.command == 'del':
        if args.key in data:
            del data[args.key]
        else:
            print('Key not found')
    with open('./data/store.kv', "w") as f:
        json.dump(data, f)


if __name__ == '__main__':
    main()