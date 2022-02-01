from brownie import OurToken, accounts, network, config
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def deploy_token():
    account = get_account()
    ourToken = OurToken.deploy(
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(f"Token Contract deployed! The total supply is: {ourToken.totalSupply()}")
    return ourToken


def main():
    deploy_token()
