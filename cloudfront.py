import time,sys
import boto3
import config


def flush_the_cdn(distribution_id):
    client = boto3.client('cloudfront')
    client.create_invalidation(
        DistributionId=distribution_id,
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': ['/*']
            },
            'CallerReference': 'automatic-{}'.format(int(time.time()))
        }
    )

if __name__ == '__main__':
    commands = sys.argv[1:]
    if len(commands) > 0 and commands[0] == 'flush':
        print flush_the_cdn(config.distribution_id)
    else:
        print 'support command: flush, ex: python cloudfront.py flush'
