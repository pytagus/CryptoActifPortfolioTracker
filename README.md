# Crypto Portfolio Tracker

## Description
This Crypto Portfolio Tracker is a desktop application built with Python's Tkinter library. It allows users to manage their cryptocurrency investments by tracking the quantity, value, and location of each cryptocurrency in their portfolio. The application provides real-time price updates by fetching data from the CryptoCompare API.

## Features

- **Add Cryptocurrencies**: Users can add a new cryptocurrency to their portfolio by entering the symbol and quantity.
- **Update Cryptocurrency Quantity**: Cryptocurrencies already in the portfolio can have their quantities updated directly from the application interface.
- **Delete Cryptocurrencies**: Users can remove a cryptocurrency from their portfolio.
- **Real-Time Price Updates**: The application fetches the latest prices for the cryptocurrencies in the portfolio, allowing users to see the current value of their investments.
- **Track Total Portfolio Value**: Displays the total value of the entire portfolio, updated in real time as prices change.
- **Location Tracking**: Users can specify and update the location where each cryptocurrency is stored (e.g., specific exchanges, wallets).
- **Data Persistence**: Portfolio data is saved locally, ensuring that users don't lose their data between application sessions.

## How to Use

### Adding a New Cryptocurrency
1. Enter the cryptocurrency symbol (e.g., BTC for Bitcoin) in the "Crypto Symbol" field.
2. Enter the quantity of the cryptocurrency you own in the "Quantity" field.
3. Click the "Add/Update Quantity" button to add the cryptocurrency to your portfolio.

### Updating Cryptocurrency Quantity
- To update the quantity of a cryptocurrency, simply enter the new total quantity in the "Quantity" field and click the "Add/Update Quantity" button.

### Deleting a Cryptocurrency
- Select the cryptocurrency you wish to delete from the list and click the "Delete Selected Crypto" button.

### Updating Prices
- Click the "Update Prices" button to fetch the latest prices for all cryptocurrencies in your portfolio.

### Adding/Updating the Location of a Cryptocurrency
1. Select the cryptocurrency for which you want to add or update the location.
2. Click the "Update Location" button.
3. In the popup window, enter the new location and click the "Update Location" button to save.

### Viewing Your Portfolio
- Your portfolio, including symbols, quantities, individual values, total values, and locations, is displayed in the main application window. This list updates in real time as you make changes.

## Installation
To run this application, you will need Python installed on your computer. Clone this repository, navigate to the project directory, and run:

```bash
python main.py


### Built With

- Python 3.x
- Tkinter
- Requests
pip install requests

## Contributing
Contributions to the Crypto Portfolio Tracker are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is open-source and available under the MIT License.
