from brownie import OurToken, accounts, network, config
from scripts.deployToken import deploy_token


def test_contract_deploy():
    # Arrange
    tokenContract = deploy_token()
    account = accounts[0]
    # Act
    # Assert
    assert tokenContract.totalSupply() == 1_000 * 10 ^ 18
    assert tokenContract.balanceOf(account) == 1_000 * 10 ^ 18
