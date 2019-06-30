import logging

import argparse
from dynaconf import settings

from app.commands import available_commands


def main():
    commands = available_commands()
    parser = argparse.ArgumentParser(description=settings('application_description'))
    parser.add_argument('--rds',
                        help='Desired action',
                        nargs='+',
                        choices=commands['rds'].keys(),
                        required=False)
    parser.add_argument('--ec2',
                        help='Desired action',
                        nargs='+',
                        choices=commands['ec2'].keys(),
                        required=False)

    args = parser.parse_args()

    if args.rds:
        command = commands['rds'][args.rds[0]]
        command()
    elif args.ec2:
        command = commands['ec2'][args.ec2[0]]
        command()
    else:
        logging.error("args not found")


if __name__ == "__main__":
    main()
