import argparse
import get_data
import data_viz
import sys


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--out_file",
                        required=True,
                        help="file output",
                        type=str)

    parser.add_argument("--plot_type",
                        required=True,
                        help="type of data plot",
                        type=str,
                        choices=["histogram", "boxplot", "combo"])

    parser.add_argument("--col_number",
                        required=False,
                        help="data column to analyze",
                        default=0,
                        type=int)

    parser.add_argument("--in_type",
                        required=False,
                        help="way data is input to program",
                        type=str,
                        default="stdin",
                        choices=["stdin", "file"])

    args = parser.parse_args()

    if args.in_type == "stdin":
        try:
            data = get_data.read_stdin_col(args.col_number)
        except IndexError:
            print("column " + str(args.col_number) + " is not in STDIN!",
                  file=sys.stderr)
            sys.exit(1)

    if args.in_type == "file":
        print("Cannot do this yet", file=sys.stderr)
        sys.exit(1)

    if args.plot_type == "histogram":
        try:
            data_viz.histogram(data, out_file_name=args.out_file)
        except IndexError:
            print("Empty list", file=sys.stderr)
            sys.exit(1)
        except PermissionError:
            print("No permissions for output file", file=sys.stderr)
            sys.exit(1)
        except ValueError:
            print("Bad extension", file=sys.stderr)
            sys.exit(1)

    if args.plot_type == "boxplot":
        try:
            data_viz.boxplot(data, out_file_name=args.out_file)
        except IndexError:
            print("Empty list", file=sys.stderr)
            sys.exit(1)
        except PermissionError:
            print("No permissions for output file", file=sys.stderr)
            sys.exit(1)
        except ValueError:
            print("Bad extension", file=sys.stderr)
            sys.exit(1)

    if args.plot_type == "combo":
        try:
            data_viz.combo(data, out_file_name=args.out_file)
        except IndexError:
            print("Empty list", file=sys.stderr)
            sys.exit(1)
        except PermissionError:
            print("No permissions for output file", file=sys.stderr)
            sys.exit(1)
        except ValueError:
            print("Bad extension", file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    main()
