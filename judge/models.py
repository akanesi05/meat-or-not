from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    is_meat = models.BooleanField(default=False)

    def __str__(self):
        return self.name
