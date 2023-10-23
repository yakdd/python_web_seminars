import argparse
import homework_15


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Directory content', description='Directory content')
    parser.add_argument('content', type=str, nargs=1, help='Input abs-path to directory')
    args = parser.parse_args()
    parse_content = homework_15.inspect_folder(args.content[0])
    for i, item in enumerate(parse_content):
        print(f'{i + 1}. {item}')
