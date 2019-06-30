from app.rds import list_all_instances


def rds_commands():
    commands = {
        'list-all-instances': list_all_instances
    }

    return commands
