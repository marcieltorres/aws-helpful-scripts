from app.log import logger


def output_rds_instances(instances):
    items = [instance['DBInstanceIdentifier'] for instance in instances]
    logger.info(_default_output(items))


def _default_output(values):
    output = {
        'length': len(values) if values else 0,
        'items': values if values else []
    }

    return output
