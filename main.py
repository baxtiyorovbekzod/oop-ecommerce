from models import Product, Customer, Order, Shop


shop = Shop("TechStore")


laptop = Product("Laptop", 1200, 5)
mouse = Product("Mouse", 25, 30)
shop.add_product(laptop)
shop.add_product(mouse)


user = Customer("Ali", 2000)
shop.add_customer(user)


order = Order(user)
order.add_item(laptop, 1)
order.add_item(mouse, 2)


print("Total:", order.calculate_total())


order.complete_order()
