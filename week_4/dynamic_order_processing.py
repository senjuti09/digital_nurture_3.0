from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, order_amount):
        pass

class RegularDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount * 0.95

class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount * 0.90

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount * 0.85

class Order:
    def __init__(self, customer_type, order_amount):
        self.customer_type = customer_type
        self.order_amount = order_amount
        self.discount_strategy = self.get_discount_strategy()

    def get_discount_strategy(self):
        if self.customer_type == "Regular":
            return RegularDiscount()
        elif self.customer_type == "Premium":
            return PremiumDiscount()
        elif self.customer_type == "VIP":
            return VIPDiscount()

    def final_price(self):
        return self.discount_strategy.apply_discount(self.order_amount)

customer_type = input("Enter Customer Type (Regular, Premium, VIP): ")
order_amount = float(input("Enter Order Amount: "))

order = Order(customer_type, order_amount)
print(f"Final Price for {customer_type} customer: {order.final_price()}")
