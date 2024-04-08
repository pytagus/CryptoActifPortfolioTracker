# Crypto Portfolio Tracker

A desktop application for tracking cryptocurrency investments.

## About The Project

**Crypto Portfolio Tracker** is a Python-based desktop application designed to offer cryptocurrency enthusiasts and investors a simplified way to keep track of their digital assets. Utilizing the **Tkinter** library for the GUI and integrating real-time price updates from **CryptoCompare API**, this tool allows users to monitor the value of their cryptocurrency portfolio in a user-friendly environment.

### Features

#### Real-time Price Updates
- **Description:** Automatically fetches the latest cryptocurrency prices from the CryptoCompare API.
- **How to Use:** Simply click the "Update Prices" button to refresh the prices of all cryptocurrencies in your portfolio. The application will display a message confirming the successful update.

#### Portfolio Management
- **Description:** Allows users to add, update, and delete cryptocurrencies from their portfolio.
- **How to Use:** 
  1. To add a cryptocurrency, enter the symbol (e.g., BTC for Bitcoin) and the quantity you own in the respective entry fields, then click the "Add/Update Quantity" button. The application will update your portfolio with the new entry.
  2. To update the quantity of an existing cryptocurrency, double-click on the desired asset in the portfolio list. A pop-up window will appear where you can enter the new quantity and click "Update Quantity" to confirm.
  3. To delete a cryptocurrency from your portfolio, select the asset in the portfolio list and click the "Delete Selected Crypto" button.

#### Dynamic Portfolio Value
- **Description:** Calculates and displays the total value of your portfolio based on current market prices.
- **How to Use:** The application automatically updates the total portfolio value whenever prices are updated or portfolio modifications are made. The total value is prominently displayed at the bottom of the interface.

#### Sortable Portfolio Display
- **Description:** Organizes the portfolio in descending order based on asset value, facilitating easy identification of the most valuable investments.
- **How to Use:** The portfolio list is sorted automatically every time prices are updated or portfolio modifications occur. The assets are listed with the most valuable at the top, making it simple to prioritize your investments.

#### Responsive UI
- **Description:** Built with Tkinter, ensuring a smooth and native application experience across different platforms.
- **How to Use:** The application features a user-friendly interface with intuitive controls and responsive design, allowing seamless navigation and interaction.

#### Data Persistence
- **Description:** Saves your portfolio data locally in a JSON file for easy access and modification, ensuring that your portfolio is preserved between sessions.
- **How to Use:** Your portfolio data is automatically saved to a file named "portfolio_data.json" in the same directory as the application. This file is loaded every time you launch the application, ensuring that your portfolio remains intact.


### Built With

- Python 3.x
- Tkinter
- Requests

## Getting Started

To get started with the Crypto Portfolio Tracker, follow these simple steps:

1. Clone the repository:
```bash
git clone https://github.com/your_username_/CryptoPortfolioTracker.git
