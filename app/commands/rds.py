from app.rds import simple_command


def rds_commands():
    commands = {
        'list-all-instances': simple_command()
    }

    return commands
