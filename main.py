import FacebookWebBot as Fb
from FacebookWebBot import FacebookBot
import warnings
import argparse
import sys


def setup_cli():
    parser = argparse.ArgumentParser(
        description="Automate facebook messaging and commenting."
    )
    subparsers = parser.add_subparsers(description="Commands help")

    message_parser = subparsers.add_parser(
        name="message", help="Send a message to user"
    )
    message_parser.add_argument(
        "--url", "-u", type=str, help="The user profile url to message.", required=True
    )
    message_parser.add_argument(
        "--text", "-t", type=str, help="The message text to send.", required=True
    )
    message_parser.add_argument(
        "--repeat",
        "-r",
        type=int,
        help="The number of time to repeat the same command. If not provided the command will run only one time",
        default=None,
    )

    comment_parser = subparsers.add_parser(name="comment", help="Comment on a post")
    comment_parser.add_argument(
        "--url", "-u", type=str, help="The post url to comment on.", required=True
    )
    comment_parser.add_argument(
        "--text", "-t", type=str, help="The comment text to post.", required=True
    )
    comment_parser.add_argument(
        "--repeat",
        "-r",
        type=int,
        help="The number of time to repeat the same command. If not provided the command will run only one time",
        default=None,
    )

    return parser


def message(bot: FacebookBot, url: str, text: str):
    print(
        f"""
        Sending message: {text}
        to: {url}
    """
    )
    bot.messageToUrl(url, text)
    print("\tMessage is sent successfully")


def comment(bot: FacebookBot, url: str, text: str):
    print(
        f"""
        Posting comment: {text}
        on post: {url}
    """
    )
    bot.commentInPost(url, text)
    print("\tComment is posted successfully")


#
# bot.logout()
# exit(0)

if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    cli = setup_cli()
    args = cli.parse_args()

    bot = Fb.FacebookBot()
    bot.login("55612056", "thanos")

    if len(sys.argv) < 2:
        cli.print_help()
    else:
        command = sys.argv[1]
        times = 1 if args.repeat is None else args.repeat
        for _ in range(times):
            if command == "message":
                message(bot, url=args.url, text=args.text)
            if command == "comment":
                comment(bot, url=args.url, text=args.text)

    bot.logout()
