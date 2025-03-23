from datetime import datetime, timedelta
import time
import uuid
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

class OrdersManager:
    def __init__(self) -> None:
        self.__orders = self.__generate_fake_orders(quantity=1_000)
        self.__orders_processed = 0
        self.__last_printed_log = datetime.now()

    def __generate_fake_orders(self, quantity):
        self.__log(f"Generating fake orders")
        orders = [(uuid.uuid4(), x) for x in range(quantity)]
        self.__log(f"{len(orders)} generated...")
        return orders

    def __log(self, message):
        print(f"{datetime.now()} > {message}")

    def __fake_save_on_db(self, order):
        id, number = order
        time.sleep(random.uniform(0, 1))  # Simula procesamiento en BD
        self.__orders_processed += 1

        if datetime.now() > self.__last_printed_log:
            self.__last_printed_log = datetime.now() + timedelta(seconds=5)
            self.__log(
                message=f"Total orders executed: {self.__orders_processed}/{len(self.__orders)}"
            )

        return f"Order [{id}] {number} was successfully prosecuted."

    def process_orders(self, num_threads=10):
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = {executor.submit(self.__fake_save_on_db, order): order for order in self.__orders}
            for future in as_completed(futures):
                result = future.result()
                self.__log(result)


# --- Optimización en ejecución ---
orders_manager = OrdersManager()

start_time = time.time()

orders_manager.process_orders(num_threads=10)  # Ajustar el número de hilos según necesidad

delay = time.time() - start_time
print(f"{datetime.now()} > Tiempo de ejecución: {delay:.2f} segundos...")
