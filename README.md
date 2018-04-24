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

## Degflasher

If you want to use degflasher for improving your hashing power in rigs with RX 570, RX 580, RX 470 or RX 480, please, install it by typing pip install https://github.com/degconnect/deg_flasher/archive/master.zip.

There is more information at http://flasher.degconnect.com

---

You can support this project donating to degconnect:

BTC : 18TAw57LUveA5CoqMfkWheNGXiDpqRcwmn

ETH: 0x23efacc1634d8b12a9e5acee330b1f28b1a3068c

LTC: Lcw9cWpW72E18m2LJRe8YG2Pk6AC2K5FN4

ZEC: t1QZVBhVviLwr1D9qpk9U6pSmLrEFNcU1Wq
