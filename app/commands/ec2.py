from app.ec2 import simple_command


def ec2_commands():
    commands = {
        'list-all-instances': simple_command
    }

    return commands
