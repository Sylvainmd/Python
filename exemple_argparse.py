import argparse

parser = argparse.ArgumentParser(
                    prog = 'Mon programme',
                    description = 'Ecrit dans un fichier souhaité',
                    )

parser.add_argument('filename')           # positional argument
parser.add_argument('-m', '--message')      # option that takes a value
parser.add_argument('-e', '--end')
parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag

args = parser.parse_args()
print(args.filename, args.message, args.end, args.verbose)