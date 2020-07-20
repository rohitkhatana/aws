#!/usr/bin/env python
import boto3
import config

class AWS(object):

    def __init__(self):
        self.profile_name = config.profile_name
        self.region_name = config.region_name
        boto3.setup_default_session(profile_name=config.profile_name)

class LoadBalancer(AWS):

    def __init__(self):
        super(LoadBalancer, self).__init__()

    def by_dns_name(self):
        pass

    def all(self):
        pass

class ApplicationLoadBalancer(LoadBalancer):

    def __init__(self):
        super(ApplicationLoadBalancer, self).__init__()
        self.alb_client = boto3.client('elbv2', region_name=self.region_name)
        self.ec2_client = boto3.resource('ec2', region_name=self.region_name)

    def by_dns_name(self, dns):
        alb = filter(lambda x: x.get('DNSName') == dns, self.all())
        return alb[0] if len(alb) == 1 else {}

    def __get_instances_by_arn(self, arn):
        return self.__target_groups(arn).get('TargetHealthDescriptions', [])

    def get_instance_ids_by_arn(self, arn):
        return map(lambda x: x.get('Target', {}).get('Id'), self.__get_instances_by_arn(arn))

    def get_instances_by_arn(self, arn):
        return map(lambda x: self.ec2_client.Instance(x), self.get_instance_ids_by_arn(arn))

    def __target_groups(self, target_arn):
        return self.alb_client.describe_target_health(TargetGroupArn=target_arn)

    def all(self):
        return self.alb_client.describe_load_balancers().get('LoadBalancers')

if __name__ == '__main__':
    ac = ApplicationLoadBalancer()
    instance_ips = map(lambda x: x.public_ip_address, ac.get_instances_by_arn(config.arn))
    import json
    inventory = {config.group_name: instance_ips}
    print json.dumps(inventory)

