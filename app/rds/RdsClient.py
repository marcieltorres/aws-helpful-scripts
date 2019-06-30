from app.log import logger


class RdsClient(object):

    __slots__ = ['_boto_client']

    def __init__(self, **kwargs):
        self._boto_client = None
        if 'boto_client' in kwargs:
            self._boto_client = kwargs['boto_client']

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._boto_client = None

    def get_all_instances(self):
        try:
            instances = self._boto_client.describe_db_instances()
            if instances and 'DBInstances' in instances:
                return instances['DBInstances']
        except Exception as ex:
            logger.error(ex)

        return []
