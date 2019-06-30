from app.commands.rds import rds_commands
from app.commands.ec2 import ec2_commands


def available_commands():
    return {
        'rds': rds_commands(),
        'ec2': ec2_commands()
    }
