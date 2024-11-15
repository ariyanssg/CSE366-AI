# Smartphone Trading Agent

A Python-based trading agent for smartphone inventory management that monitors prices and stock levels to make optimal purchasing decisions. The agent uses multiple controllers to monitor price changes and inventory levels, making automated decisions about when to restock based on configurable thresholds.

## Features

- **Price Monitoring**: Tracks price changes and identifies purchasing opportunities when prices drop below threshold
- **Inventory Management**: Monitors stock levels and triggers reorders when inventory becomes critical
- **Automated Decision Making**: Makes purchase decisions based on both price and inventory conditions
- **Visual Analytics**: Generates plots for price trends, stock levels, and order decisions
- **Interactive Configuration**: Allows users to set custom parameters and test different scenarios

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/smartphone-trading-agent.git
cd smartphone-trading-agent
```

2. Install required packages:
```bash
pip install numpy matplotlib
```

## Usage

Run the script using Python:
```bash
python trading_agent.py
```

### Configuration Parameters

When running the program, you'll be prompted to enter:
1. Average price of the smartphone
2. Critical stock level (default recommendation: 10)
3. Minimum order quantity
4. Specific order quantity for favorable prices
5. Choice to enter custom price series or use generated data

### Example Input

```python
Enter the average price of the smartphone: 600
Enter the critical stock level (e.g., 10): 10
Enter the minimum order quantity: 10
Enter the specific order quantity for favorable prices: 15
Do you want to enter custom price series? (yes/no): no
```

### Decision Rules

The agent makes decisions based on the following rules:

1. **Price-based Decision**:
   - If price drops below 80% of average price (20% discount)
   - AND stock is not critically low
   - THEN order specific quantity

2. **Stock-based Decision**:
   - If stock falls below critical level
   - THEN order minimum quantity

3. **No Action**:
   - If neither condition is met
   - THEN no order placed

### Example Scenario

As mentioned in the specifications:
- If smartphone price drops to 500 BDT (from average of 600 BDT)
- And current stock is 20 units
- The agent will order 15 more units

## Output

The program generates three plots:
1. **Price Trends**: Shows price history and average price threshold
2. **Stock Levels**: Displays inventory levels and critical stock threshold
3. **Order Decisions**: Visualizes ordering decisions over time

## Code Structure

- `SmartphoneTradingAgent`: Main agent class
  - `price_monitor()`: Monitors price changes
  - `inventory_monitor()`: Tracks inventory levels
  - `order_controller()`: Makes ordering decisions
  - `simulate()`: Runs the simulation
  - `plot_results()`: Generates visualizations

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

[Your Name]

## Acknowledgments

This project was developed as part of a lab task for inventory management simulation.
