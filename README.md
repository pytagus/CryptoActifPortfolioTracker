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
1. **Enter the Cryptocurrency Symbol**: In the "Crypto Symbol" entry field at the top, type the symbol for the cryptocurrency you wish to add (e.g., BTC for Bitcoin).
2. **Enter the Quantity**: In the "Quantity" entry field, type the amount of the cryptocurrency you own.
3. **Add to Portfolio**: Click the "Add/Update Quantity" button. This action adds the cryptocurrency to your portfolio or updates the quantity if it already exists in the portfolio.

### Updating Cryptocurrency Quantity
1. **Select a Cryptocurrency**: In the portfolio list displayed in the Treeview, double-click on the row corresponding to the cryptocurrency whose quantity you want to update. This action will open a new window.
2. **Enter the New Quantity**: In the popup window, enter the new total quantity for the selected cryptocurrency in the "New Quantity" entry field.
3. **Submit the Update**: Click the "Update Quantity" button in the popup window to save your changes.

### Deleting a Cryptocurrency
1. **Select the Cryptocurrency**: Click on the cryptocurrency entry you wish to delete from the list in the Treeview.
2. **Delete the Entry**: With the cryptocurrency selected, click the "Delete Selected Crypto" button. This will remove the cryptocurrency from your portfolio.

### Updating Prices
- **Fetch the Latest Prices**: Click the "Update Prices" button at any time to fetch the latest market prices for all the cryptocurrencies in your portfolio. This will update the "Value ($)" and "Total ($)" columns in the Treeview with the latest data.

### Adding/Updating the Location of a Cryptocurrency
1. **Select a Cryptocurrency**: Click once on the cryptocurrency in the Treeview for which you want to update the location. Ensure it is highlighted.
2. **Open the Location Update Window**: Click the "Update Location" button. This will open a new popup window.
3. **Enter the Location**: In the popup window, type the location where the cryptocurrency is stored (e.g., a specific exchange or wallet) into the "New Location" entry field.
4. **Submit the Update**: Click the "Update Location" button within the popup window to save the new location information to your portfolio.

### Viewing Your Portfolio
- **Automatic Updates**: The main application window displays your entire portfolio, including cryptocurrency symbols, quantities, values, total values, and storage locations. This list updates automatically as you make changes to your portfolio, such as adding new cryptocurrencies, updating quantities or locations, and fetching the latest prices.


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
