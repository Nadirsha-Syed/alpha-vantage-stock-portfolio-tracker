# Alpha Vantage Stock Portfolio Tracker 📈

A simple command-line application in Python to manage and track your stock portfolio using real-time data from the Alpha Vantage API.

## 🚀 Features

- Add stocks with number of shares and purchase price
- Remove stocks from your portfolio
- Fetch real-time stock prices using Alpha Vantage
- Calculate market value, gain/loss, and performance percentage
- Display a detailed portfolio summary

## 📦 Requirements

- Python 3.6+
- [Alpha Vantage API Key](https://www.alphavantage.co/support/#api-key)
- Required Python package:
  - `alpha_vantage`

Install the required package using pip:

```bash
pip install alpha_vantage
```

## 🛠 Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/alpha-vantage-stock-portfolio-tracker.git
cd alpha-vantage-stock-portfolio-tracker
```

2. Open `tracker.py` and replace:

```python
api_key = "YOUR_API_KEY"
```

with your actual Alpha Vantage API key.

## ▶️ Usage

Run the application:

```bash
python tracker.py
```

Follow the on-screen menu:

```
1. Add Stock
2. Remove Stock
3. View Portfolio
4. Exit
```

### Example

```
Enter stock symbol (e.g., AAPL): AAPL
Enter number of shares: 100
Enter purchase price: 10
```

### Sample Output

```
--- Portfolio Summary ---
AAPL: 100.0 shares
  Purchase Price: $10.00
  Current Price:  $211.45
  Market Value:   $21145.00
  Gain/Loss:      $20145.00

Total Portfolio Value: $21145.00
Total Gain/Loss: $20145.00
Performance: 2014.50%
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👤 Author

[Your Name](https://github.com/your-username)
