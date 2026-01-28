from django.db import models

class Metric(models.Model)
    CPU=model.FloatField();
    Memory=model.FloatField();
    Disk=model.FloatField();
    Timestamp=model.DateTiemField();
    def __str__(self):
        return f" CPU: {self.CPU} at {self.Timestamp}"

