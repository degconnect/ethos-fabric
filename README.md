# ethos-fabric
Fabric tasks to be used when mining rigs using EthosOS

## How to start using it

run pip install fabric

## How to use it
cd the ethos-fabric folder and run commands like:

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

## Running the same command to several rigs

fab show_wallet -H ethos@10.1.1.101,ethos@10.1.1.102

Please, don't put any space between hosts

## How to avoid entering your password anytime you need to run a command in your rig

Use ssh-copy-id ethos@10.1.1.101
