import os


from fabric.api import run, env, task, cd, sudo, execute, hide
from fabric.operations import get, put, reboot

"""
pip install fabric

how to run:
fab show_wallet -H ethos@10.1.1.101
fab minestart -H ethos@10.1.1.101
fab minestop -H ethos@10.1.1.101
fab allow -H ethos@10.1.1.101
fab disallow -H ethos@10.1.1.101
fab restart -H ethos@10.1.1.101
fab update -H ethos@10.1.1.101
fab hostname -H ethos@10.1.1.101
fab pool1pass -H ethos@10.1.1.101
fab show_miner -H ethos@10.1.1.101
fab stats -H ethos@10.1.1.101
fab degflasher -H ethos@10.1.1.101
"""


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


HOME_PATH = '/home/ethos/'


@task
def show_wallet():
    run('cat local.conf | grep wallet')


@task
def minestart():
    run('minestart')


@task
def minestop():
    run('minestop')


@task
def allow():
    run('allow')


@task
def disallow():
    run('disallow')


@task
def update():
    run('update')


@task
def restart():
    sudo('hard-reboot')


@task
def pool1pass():
    run('cat local.conf | grep poolpass1')


@task
def hostname():
    run('hostname')


@task
def show_miner():
    run('show miner')


@task
def stats():
    run('update | grep hash')


@task
def degflasher():
    """
    Information about how to flash your Cards in order to improve performance at http://flasher.degconnect.com.
    :return:
    """
    reboot(wait=45)
    run('degflasher')


def main():
    print("Please, read head of this file for help.")
    print("Information about how to flash your Cards in order to improve performance at http://flasher.degconnect.com.")


if __name__ == '__main__':
    main()
