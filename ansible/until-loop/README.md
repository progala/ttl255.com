# Ansible - _until_ loop

## Playbooks

Playbooks illustrating use cases for Ansible `until` loop.

- `until_web_app.yml` - Polling REST API endpoint
- `until_eos_net.yml` - Checking status of the BGP adjacency
- `until_docker.yml` - Polling health status of Docker container

## Setup

- Python 3.8.5
- Ansible 2.9.10 running in Python virtual environment
- Python libraries listed in `requirements.txt`
- Docker engine
- Docker container named "veos:4.18.10M" built with vrnetlab and "vEOS-lab-4.18.10M.vmdk" image

Blog post URL: https://ttl255.com/ansible-until-loop/