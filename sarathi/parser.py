"""Parser module
Used to parse the arguments from the discord message.
"""
import argparse


class Parser(argparse.ArgumentParser):
    def exit(self, status=0, message=None):
        if status:
            raise argparse.ArgumentException(message)

    def error(self, *args, **kwargs):
        raise argparse.ArgumentParser("Error: {}, {}".format(args, kwargs))


sarathi_parser = Parser(
    prog="sarathi", description="This is some description text.",
    exit_on_error=False)

sarathi_subparsers = sarathi_parser.add_subparsers(
    required=True,
    dest="command",
    help="command help goes here")

til_parser = sarathi_subparsers.add_parser(
    "til", exit_on_error=False, help="TIL command")

til_subparsers = til_parser.add_subparsers(
    dest="subcommand", required=True, help="TIL sub-commands")

til_add_parser = til_subparsers.add_parser(
    "add",
    exit_on_error=False,
    help="add command")

til_add_parser.add_argument("-m", "--message", dest="message",
                            help="Text to be displayed when URL is provided")
til_add_parser.add_argument(
    "-c", "--category", action="append", type=str, help="Category or tag for the TIL.")
til_add_parser.add_argument(
    "-u", "--url", action="append", type=str, help="Links related to this TIL")

til_find_parser = til_subparsers.add_parser(
    "find", exit_on_error=False, help="add command")

til_find_parser.add_argument(
    "-c", "--category", help="Category in which to find this TIL")
til_find_parser.add_argument(
    "-d", "--domain", help="List help from this domain only")
til_find_parser.add_argument(
    "-l", "--limit", default=5, type=int, help="Limit of the TILs to print")
til_find_parser.add_argument(
    "--date", type=str, help="Fuzzy datetime filter; supports `[since|before|after] N [days|months|weeks|years]`")
