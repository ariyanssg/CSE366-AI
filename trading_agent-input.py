import matplotlib.pyplot as plt
import numpy as np

class SmartphoneTradingAgent:
    def __init__(self, average_price, critical_stock, min_order, specific_order):
        self.average_price = average_price
        self.critical_stock = critical_stock
        self.min_order = min_order
        self.specific_order = specific_order
        self.stock_level = 20  # Initial stock
        self.price_history = []
        self.stock_history = []
        self.order_history = []

    def price_monitor(self, current_price):
        return current_price < 0.8 * self.average_price

    def inventory_monitor(self):
        return self.stock_level < self.critical_stock

    def order_controller(self, current_price):
        if self.price_monitor(current_price) and not self.inventory_monitor():
            return self.specific_order
        elif self.inventory_monitor():
            return self.min_order
        return 0

    def simulate(self, price_series):
        for current_price in price_series:
            order_quantity = self.order_controller(current_price)
            self.stock_level += order_quantity
            self.stock_level -= np.random.randint(1, 5)  # Simulate sales
            
            # Record data for plotting
            self.price_history.append(current_price)
            self.stock_history.append(self.stock_level)
            self.order_history.append(order_quantity)

    def plot_results(self):
        plt.figure(figsize=(15, 5))

        # Plot price trends
        plt.subplot(1, 3, 1)
        plt.plot(self.price_history, label="Price", color="blue")
        plt.axhline(y=self.average_price, color="red", linestyle="--", label="Average Price")
        plt.legend()
        plt.title("Price Trends")
        plt.xlabel("Time")
        plt.ylabel("Price")

        # Plot stock levels
        plt.subplot(1, 3, 2)
        plt.plot(self.stock_history, label="Stock Level", color="green")
        plt.axhline(y=self.critical_stock, color="red", linestyle="--", label="Critical Stock")
        plt.legend()
        plt.title("Stock Levels")
        plt.xlabel("Time")
        plt.ylabel("Units in Stock")

        # Plot order decisions
        plt.subplot(1, 3, 3)
        plt.bar(range(len(self.order_history)), self.order_history, color="orange", label="Order Quantity")
        plt.legend()
        plt.title("Order Decisions")
        plt.xlabel("Time")
        plt.ylabel("Units Ordered")

        plt.tight_layout()
        plt.show()


def main():
    # Get user inputs
    average_price = float(input("Enter the average price of the smartphone: "))
    critical_stock = int(input("Enter the critical stock level (e.g., 10): "))
    min_order = int(input("Enter the minimum order quantity: "))
    specific_order = int(input("Enter the specific order quantity for favorable prices: "))
    
    # Generate price series or allow user to input prices
    option = input("Do you want to enter custom price series? (yes/no): ").strip().lower()
    if option == "yes":
        price_series = list(map(float, input("Enter the price series separated by spaces: ").split()))
    else:
        print("Generating random price series...")
        price_series = np.random.randint(average_price * 0.7, average_price * 1.2, 50)
        print(f"Generated price series: {price_series}")

    # Initialize and run the agent
    agent = SmartphoneTradingAgent(average_price, critical_stock, min_order, specific_order)
    agent.simulate(price_series)
    agent.plot_results()

if __name__ == "__main__":
    main()
