from facade import OnlineShoppingFacade

facade = OnlineShoppingFacade()

print(facade.place_order(user_id=1, product_id=2, amount=100))  # True