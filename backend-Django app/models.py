from django.db import models

class AppointmentSlot(models.Model):
    title = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title or 'Slot'} on {self.date} from {self.start_time} to {self.end_time}"
