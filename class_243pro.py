from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/688c45a4890e4d1db51acad3d517f138'

web3 = Web3(Web3.HTTPProvider(infura_url))

latest_block = web3.eth.getBlock('latest')

print("/nLatest block of eth blockchain:", latest_block)

block_transaction_count = web3.eth.block_transaction_count(20187935)

print("/n Number of transaction happened in the block: ", block_transaction_count)

Transaction_fee = web3.eth.fee_history(block_conut = 396, newest_block = 'latest', reward_percentile = None)

print("/nNumber of transaction happened in the block:", Transaction_fee)


