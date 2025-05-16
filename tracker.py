from alpha_vantage.timeseries import TimeSeries

class StockPortfolio:
    def __init__(self, api_key):
        self.portfolio = {}
        self.initial_investment = 0
        self.api_key = api_key
        self.ts = TimeSeries(key=self.api_key, output_format='json')

    def add_stock(self, symbol, shares, purchase_price):
        symbol = symbol.upper()

        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
        else:
            self.portfolio[symbol] = {'shares': shares, 'purchase_price': purchase_price}

        self.initial_investment += shares * purchase_price
        print(f"Added {shares} shares of {symbol} at ${purchase_price} each.")

    def remove_stock(self, symbol):
        symbol = symbol.upper()
        if symbol in self.portfolio:
            shares_removed = self.portfolio[symbol]['shares']
            purchase_price = self.portfolio[symbol]['purchase_price']
            self.initial_investment -= shares_removed * purchase_price
            del self.portfolio[symbol]
            print(f"Removed {shares_removed} shares of {symbol}.")
        else:
            print(f"{symbol} not found in portfolio.")

    def get_current_price(self, symbol):
        """
        Fetches the current price of a stock using Alpha Vantage.
        """
        try:
            data, _ = self.ts.get_quote_endpoint(symbol=symbol)
            current_price = data['05. price']  # This is the latest price
            return float(current_price)
        except Exception as e:
            print(f"Error retrieving data for {symbol}: {e}")
            return None

    def get_portfolio_value(self):
        if not self.portfolio:
            print("\nPortfolio is empty. Add some stocks first.\n")
            return

        total_value = 0
        print("\n--- Portfolio Summary ---")
        for symbol, data in self.portfolio.items():
            current_price = self.get_current_price(symbol)
            if current_price is None:
                print(f"Could not retrieve price for {symbol}. Skipping.\n")
                continue

            market_value = current_price * data['shares']
            cost = data['purchase_price'] * data['shares']
            gain = market_value - cost
            total_value += market_value

            print(f"{symbol}: {data['shares']} shares")
            print(f"  Purchase Price: ${data['purchase_price']:.2f}")
            print(f"  Current Price:  ${current_price:.2f}")
            print(f"  Market Value:   ${market_value:.2f}")
            print(f"  Gain/Loss:      ${gain:.2f}\n")

        portfolio_performance = total_value - self.initial_investment
        performance_percentage = (portfolio_performance / self.initial_investment) * 100 if self.initial_investment != 0 else 0

        print(f"Total Portfolio Value: ${total_value:.2f}")
        print(f"Total Gain/Loss: ${portfolio_performance:.2f}")
        print(f"Performance: {performance_percentage:.2f}%\n")


def main():
    # Replace YOUR_API_KEY with your actual Alpha Vantage API key
    api_key = "YOUR_API_KEY"
    tracker = StockPortfolio(api_key)

    while True:
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ").strip()
            try:
                shares = float(input("Enter number of shares: "))
                price = float(input("Enter purchase price: "))
                tracker.add_stock(symbol, shares, price)
            except ValueError:
                print("Invalid input for shares or price. Please try again.")
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").strip()
            tracker.remove_stock(symbol)
        elif choice == '3':
            tracker.get_portfolio_value()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
