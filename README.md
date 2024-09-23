# Exodus Wallet Transaction Data Analysis

This project analyzes cryptocurrency transaction data exported from the Exodus wallet. The goal is to explore and visualize the inflows and outflows of assets, the types of transactions, and other key metrics over time.

## Project Structure

- `main.ipynb`: The Jupyter Notebook containing all data analysis and visualization code.
- `exodus_0-all-txs-2024-09-20_21-17-11.csv`: CSV file containing the transaction history exported from the Exodus wallet (Not included for the analysis).
- `exodus_synthetic_data.py`: A Python script for generating synthetic cryptocurrency transaction data for analysis.
- `README.md`: This file, containing an overview of the project.

## Data Preparation

### Data Extraction
The transaction history is exported from the Exodus wallet as a CSV file. The data contains columns such as:

- `DATE`: Timestamp of the transaction.
- `TYPE`: Type of transaction (e.g., deposit, withdrawal).
- `FROMPORTFOLIO`: Source of the transaction (e.g., internal or external portfolio).
- `TOPORTFOLIO`: Destination of the transaction.
- `OUTAMOUNT`, `INAMOUNT`: The amount of cryptocurrency involved in the transaction.
- `OUTCURRENCY`, `INCURRENCY`: The type of cryptocurrency used in the transaction.
- Other fields such as transaction IDs, addresses, and fees.

### Data Cleaning & Preprocessing

The data cleaning steps involved:

- Converting missing values (`NaN`) to `0`, `"None"`, or `Null`, depending on the context.
- Converting the `DATE` column to a `datetime` format for easy time-based analysis.
- Dropping unnecessary columns such as `TOADDRESS` and `FROMADDRESS` if they were deemed irrelevant for the analysis.

## Synthetic Data Generation

The project includes a script to generate synthetic cryptocurrency transaction data for testing purposes.

### `exodus_synthetic_data.py`

This script creates a fake dataset containing random cryptocurrency transactions, including inflows, outflows, and wallet addresses. The script uses the `Faker` library to generate fake data such as:

- Random cryptocurrency names (e.g., Bitcoin, Ethereum).
- Random inflow and outflow amounts.
- Wallet addresses and transaction IDs.

You can modify the number of rows and adjust the parameters to fit your needs.

```python
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
```

### Usage

To generate synthetic data, simply run the `exodus_synthetic_data.py` script, which will create a CSV file named `synthetic_crypto_transactions.csv`.

```bash
python exodus_synthetic_data.py
```

## Data Analysis

### Types of Analysis Performed

1. **Transaction Types**: Analyzing different types of transactions (deposits, withdrawals) and the cryptocurrencies involved.
2. **Summarizing Inflows & Outflows**: Aggregating the inflows (deposits) and outflows (withdrawals) by various time frames (daily, weekly, monthly, and yearly).
3. **Distribution of Transaction Amounts**: Examining the distribution of amounts transacted for both deposits and withdrawals.
4. **Frequency of Transactions**: Investigating the frequency of transactions for different assets.

## Visualization

The project includes several visualizations to make the data easier to understand:

1. **Inflows and Outflows Over Time**: A time-series plot showing how much cryptocurrency was deposited and withdrawn over different time periods.
2. **Bar Charts for Asset Distribution**: Bar charts were created to visualize the volume of transactions per cryptocurrency.
3. **Pie Chart for Asset Allocation**: A pie chart was used to display the distribution of assets based on inflows.
![output_8](https://github.com/user-attachments/assets/4c193a99-1400-48df-8e12-6e26f72bb765)
![output_7](https://github.com/user-attachments/assets/7833d1e8-578a-4cb9-92dc-9b39f9609005)
![output_6](https://github.com/user-attachments/assets/da584009-724c-495f-addd-a03f10a8779b)
![output_5](https://github.com/user-attachments/assets/e25ea385-9e70-4369-9ed8-c2785db293ee)
![output_4](https://github.com/user-attachments/assets/d4dae86a-e86c-44c4-9b88-049f5c9ecf01)
![output_3](https://github.com/user-attachments/assets/0c265f9b-6252-419b-ae5e-6243ac226cd6)
![output_2](https://github.com/user-attachments/assets/732849db-6234-4288-b045-566f60a8526d)
![output_1](https://github.com/user-attachments/assets/79d74ac5-5b57-4c7f-aaab-0f42d9f4dcd4)
![output](https://github.com/user-attachments/assets/0849e10c-5bd1-47c5-b034-a5ee43f819fa)



### Libraries Used

- **pandas**: For data manipulation and cleaning.
- **matplotlib**: For basic plotting of the data.
- **seaborn**: For creating more advanced, aesthetic visualizations.

## Running the Project

To run the analysis and visualizations, ensure you have the required Python libraries installed:

```bash
pip install pandas matplotlib seaborn faker
```

Then, open the `main.ipynb` file in Jupyter Notebook or any compatible environment, and execute the cells. You can also run the synthetic data script to create a test dataset if needed.

## Future Work

- Improve transaction classification, such as categorizing based on the destination or source.
- Incorporate more advanced visualization techniques such as interactive charts using `plotly`.
- Explore further statistical analysis of fees, gains, and losses for the assets.

## Author

- @gappeah

## License

This project is licensed under the MIT License.
