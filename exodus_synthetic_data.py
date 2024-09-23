import pandas as pd
import numpy as np
from faker import Faker

# Instantiate Faker for generating fake data
fake = Faker()

# Parameters for the synthetic dataset
num_rows = 1000  # Change this number to match the size of your dataset

# Generate random dates within a year
date_range = pd.date_range(start='2023-01-01', end='2024-01-01', periods=num_rows)

# Generate random cryptocurrency names from a predefined list
crypto_names = ['Bitcoin', 'Ethereum', 'Litecoin', 'Dash', 'Zcash', 'BCH_USD', 'Bytecoin']
random_crypto = np.random.choice(crypto_names, num_rows)

# Random inflow and outflow amounts
in_amounts = np.random.uniform(low=0.01, high=5.0, size=num_rows)
out_amounts = np.random.uniform(low=0.01, high=5.0, size=num_rows)

# Generate random wallet addresses and transaction IDs using Faker
to_wallets = [fake.sha256() for _ in range(num_rows)]
from_wallets = [fake.sha256() for _ in range(num_rows)]
tx_ids = [fake.sha256() for _ in range(num_rows)]

# Create the synthetic dataset
synthetic_data = pd.DataFrame({
    'DATE': date_range,
    'ASSET': random_crypto,
    'INAMOUNT': in_amounts,
    'OUTAMOUNT': out_amounts,
    'TO': to_wallets,
    'FROM': from_wallets,
    'TXID': tx_ids
})

# Save to CSV
synthetic_data.to_csv('synthetic_crypto_transactions.csv', index=False)
