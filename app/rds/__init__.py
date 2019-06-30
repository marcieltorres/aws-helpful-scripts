import boto3

from app.rds.RdsClient import RdsClient
from app.output import output_rds_instances

__RDS_CLIENT_CONFIG = {
    'boto_client': boto3.client('rds')
}


def list_all_instances():
    instances = []
    with RdsClient(**__RDS_CLIENT_CONFIG) as rds_client:
        instances = rds_client.get_all_instances()

    output_rds_instances(instances)
