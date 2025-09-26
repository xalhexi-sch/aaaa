from collections import deque

class Restaurant:
    def __init__(self):
        # Initialize the orders queue as an empty deque
        self.orders = deque()

    def add_order(self, order_id):
        """
        Adds a new order_id to the end of the queue.
        """
        # Add the order_id to the right side of the deque
        self.orders.append(order_id)

    def prepare_order(self):
        """
        Removes the oldest order from the front of the queue and returns it.
        If the queue is empty, returns "No orders to prepare".
        """
        # Check if the queue has orders
        if self.orders:
            # Remove the order from the front and return it
            return self.orders.popleft()
        else:
            # Return message if no orders are left
            return "No orders to prepare"

# --- Main execution part of the script (DO NOT MODIFY) ---
restaurant = Restaurant()

while True:
    try:
        command = input().strip()

        if command == "exit":
            break

        parts = command.split()

        action = parts[0]

        if action == "order" and len(parts) > 1:
            order_id = parts[1]
            restaurant.add_order(order_id)

        elif action == "prepare":
            result = restaurant.prepare_order()
            print(result)

    except Exception as e:
        print(f"Error: {e}")
