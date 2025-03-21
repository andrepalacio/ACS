from abc import ABC, abstractmethod
import copy

# --- Ejercicio 2: Cálculo de Precio en Cuotas (Factory Method + Template Method) ---
class PaymentPlan(ABC):
    def calculate_total(self, precio):
        interes = self.get_interest()
        return precio * (1 + interes)

    def calculate_installments(self, precio, cuotas):
        total = self.calculate_total(precio)
        return total / cuotas

    @abstractmethod
    def get_interest(self):
        pass

class VisaPayment(PaymentPlan):
    def get_interest(self):
        return 0.05  # 5% de interés

class MastercardPayment(PaymentPlan):
    def get_interest(self):
        return 0.07  # 7% de interés

class PaymentPlanFactory:
    @staticmethod
    def create_payment_plan(marca):
        if marca == "Visa":
            return VisaPayment()
        elif marca == "Mastercard":
            return MastercardPayment()
        else:
            raise ValueError("Tarjeta no soportada")

# --- Pruebas ---
if __name__ == "__main__":
    factory = PaymentPlanFactory()
    visa_plan = factory.create_payment_plan("Visa")
    print("Total con Visa:", visa_plan.calculate_total(1000))
    print("Cuota con Visa:", visa_plan.calculate_installments(1000, 12))
    
    mc_plan = factory.create_payment_plan("Mastercard")
    print("Total con Mastercard:", mc_plan.calculate_total(1000))
    print("Cuota con Mastercard:", mc_plan.calculate_installments(1000, 12))