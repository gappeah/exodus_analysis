# Exodus Wallet Transaction Data Analysis

This project analyses cryptocurrency transaction data exported from the Exodus wallet. The goal is to explore and visualise the inflows and outflows of assets, the types of transactions, and other key metrics over time.

## Project Structure

- `main.ipynb`: The Jupyter Notebook containing all data analysis and visualisation code.
- `exodus_0-all-txs-2024-09-20_21-17-11.csv`: CSV file containing the transaction history exported from the Exodus wallet.
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

## Data Analysis

### Types of Analysis Performed

1. **Transaction Types**: Analysing different types of transactions (deposits, withdrawals) and the cryptocurrencies involved.
2. **Summarising Inflows & Outflows**: Aggregating the inflows (deposits) and outflows (withdrawals) by various time frames (daily, weekly, monthly, and yearly).
3. **Distribution of Transaction Amounts**: Examining the distribution of amounts transacted for both deposits and withdrawals.
4. **Frequency of Transactions**: Investigating the frequency of transactions for different assets.

### Data Exploration

The following steps were carried out:

1. **Explore Transaction Types**: Identified unique transaction types and grouped them by the type of cryptocurrency involved.
2. **Summarise Inflows and Outflows**: Aggregated transaction amounts based on various time intervals, including daily, monthly, and yearly.
3. **Transaction Amount Distribution**: Generated histograms to visualise the distribution of transaction amounts.
4. **Transaction Frequency by Asset**: Summarised the number of transactions for each cryptocurrency.

## Visualisation

The project includes several visualisations to make the data easier to understand:

1. **Inflows and Outflows Over Time**: A time-series plot showing how much cryptocurrency was deposited and withdrawn over different time periods.
2. **Bar Charts for Asset Distribution**: Bar charts were created to visualise the volume of transactions per cryptocurrency.
3. **Pie Chart for Asset Allocation**: A pie chart was used to display the distribution of assets based on inflows.

### Libraries Used

- **pandas**: For data manipulation and cleaning.
- **matplotlib**: For basic plotting of the data.
- **seaborn**: For creating more advanced, aesthetic visualisations.

## Running the Project

To run the analysis and visualisations, ensure you have the required Python libraries installed:

```bash
pip install pandas matplotlib seaborn
