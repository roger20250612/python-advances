"""Argument Parsing"""
import sys

###################################
# Demo 03 - getopt - Toi uu hoa
import getopt

def main():
    try:
        opts, _ = getopt.getopt(
            args=sys.argv[1:],
            shortopts="f:m:",
            longopts=["filename=", "message="]
        )
    except getopt.GetoptError as err:
        print(f"Error: {err}")
        sys.exit(1)

    options = {"-f": "", "-m": "", "--filename": "", "--message": ""}

    for opt, arg in opts:
        print(f"Processing opt={opt}; arg={arg}")
        if opt in ("-f", "--filename"):
            options["-f"] = arg
        elif opt in ("-m", "--message"):
            options["-m"] = arg
        else:
            raise Exception(f"Unsupported option: {opt}")

    filename = options["-f"]
    message = options["-m"]

    if not filename:
        print("Error: filename is required.")
        sys.exit(1)

    with open(filename, mode="a+", encoding="utf8") as f:
        f.write(f"{message}\n")

    print(f"Wrote message '{message}' to filename: {filename}")
    sys.exit(0)

if __name__ == "__main__":
    main()

# $ python tuto-04-argument-parsing.py -f tuto-04-argument-parsing-test.txt --message Bon-weekend\ Paris\ !
# Processing opt=-f; arg=tuto-04-argument-parsing-test.txt
# Processing opt=--message; arg=Bon-weekend Paris !
# Wrote message 'Bon-weekend Paris !' to filename: tuto-04-argument-parsing-test.txt

# $ python tuto-04-argument-parsing.py -f tuto-04-argument-parsing-test.txt -m Bon-weekend\ Paris\ !
# Processing opt=-f; arg=tuto-04-argument-parsing-test.txt
# Processing opt=-m; arg=Bon-weekend Paris !
# Wrote message 'Bon-weekend Paris !' to filename: tuto-04-argument-parsing-test.txt


###################################
# Demo 03 - getopt

import getopt
opts, args = getopt.getopt(args=sys.argv[1:],
                           shortopts="f:m:",
                           longopts=["filename", "message"])
filename = message = ""
for opt, arg in opts:
    print(f"Processing opt={opt}; arg={arg}")
    if opt == "-m":
        message = arg
    elif opt == "-f":
        filename = arg
    else:
        raise Exception(f"Not support opt: {opt}")
with open(file=filename, mode="a+", encoding="utf8") as f:
    f.write(f"{message}\n")
print(f"Wrote message '{message}' to filename: {filename}")
sys.exit(0)
# $ python tuto-04-argument-parsing.py -f tuto-04-argument-parsing-test.txt -m Bon-weekend\ Paris\ !
# Processing opt=-f; arg=tuto-04-argument-parsing-test.txt
# Processing opt=-m; arg=Bon-weekend Paris !
# Wrote message 'Bon-weekend Paris !' to filename: tuto-04-argument-parsing-test.txt

# $ python tuto-04-argument-parsing.py -f tuto-04-argument-parsing-test.txt -message Bon-weekend\ Paris\ !
# Processing opt=-f; arg=tuto-04-argument-parsing-test.txt
# Processing opt=-m; arg=essage
# Wrote message 'essage' to filename: tuto-04-argument-parsing-test.txt

# $ python tuto-04-argument-parsing.py -f tuto-04-argument-parsing-test.txt -k Bon-weekend\ Paris\ !
# Traceback (most recent call last):
#   File "/home/lavie/dev/work/hoc_them/python-advances/tuto-04-argument-parsing.py", line 8, in <module>
#     opts, args = getopt.getopt(args=sys.argv[1:],
#                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/usr/lib/python3.12/getopt.py", line 95, in getopt
#     opts, args = do_shorts(opts, args[0][1:], shortopts, args[1:])
#                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/usr/lib/python3.12/getopt.py", line 195, in do_shorts
#     if short_has_arg(opt, shortopts):
#        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/usr/lib/python3.12/getopt.py", line 211, in short_has_arg
#     raise GetoptError(_('option -%s not recognized') % opt, opt)
# getopt.GetoptError: option -k not recognized
###################################
# Demo 02 - sys.argv

filename = sys.argv[1]
message = sys.argv[2]
with open(file=filename, mode="a+", encoding="utf8") as f:
    f.write(message + "\n")
print(f"Wrote message '{message}' to filename: {filename}")
sys.exit(0)
# $ python tuto-04-argument-parsing.py tuto-04-argument-parsing-test.txt Bonjour\ Paris
# Wrote message 'Bonjour Paris' to filename: tuto-04-argument-parsing-test.txt

###################################
# Demo 01 - Arguments in Function
def my_function(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(kwargs.get("arg_one"))
    print(kwargs.get("arg_two"))

my_function("Hello", "World", arg_one="Paris", arg_two="Bonjour")
# $ python tuto-04-argument-parsing.py
# Hello
# World
# Paris
# Bonjour
