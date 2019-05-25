# aws
This repo contains python scripts for interacting with aws

This *get_ips_by_alb_target_group_arn.py* script is written to generate **dynamic inventory for ansible**. 

### For fetching the IPs attached to a target group of ALB
1. First change the config file:
  ```python
  profile_name = 'profile_name'
  region_name = 'region_name'
  arn = 'arn'
  group_name = 'app1-group'
  ```
2. Install the PIP packages (recommend use virtualenv before installing the packages)

  `pip install -r requirements.txt`

3. Run the scripts

  `python get_ips_by_alb_target_group_arn.py`

4. Passing dynamic inventory to ansible playbook

  `ansible-playbook main.yml -i get_ips_by_alb_target_group_arn.py`
  
### For Flushing the cdn
1. First change the config file:
  ```python
  profile_name = 'profile_name'
  region_name = 'region_name'
  arn = 'arn'
  group_name = 'app1-group'
  disribution_id = ''
  ```
2. Install the PIP packages (recommend use virtualenv before installing the packages)

  `pip install -r requirements.txt`

3. Run the scripts

  `python cloudfront.py flush`

