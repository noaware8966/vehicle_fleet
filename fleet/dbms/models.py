from django.db import models


class Client(models.Model):
    full_name = models.CharField("Полное имя", max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class PickupPoint(models.Model):
    address = models.CharField("Адрес пункта", max_length=255)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Пункт"
        verbose_name_plural = "Пункты"


class Car(models.Model):
    license_plate = models.CharField("Номерной знак", max_length=20, unique=True)
    brand = models.CharField("Марка", max_length=255)

    def __str__(self):
        return f"{self.brand} ({self.license_plate})"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


class Order(models.Model):
    number_order = models.CharField("Номер заказа", max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    departure_point = models.ForeignKey(PickupPoint, on_delete=models.CASCADE, related_name="departures",
                                        verbose_name="Пункт отправления")
    pickup_point = models.ForeignKey(PickupPoint, on_delete=models.CASCADE, related_name="pickups",
                                     verbose_name="Пункт выдачи")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль")
    delivery_date = models.DateField("Дата доставки")

    payment_date = models.DateField("Дата оплаты", null=True, blank=True)
    amount = models.DecimalField("Сумма оплаты", max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.number_order

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

