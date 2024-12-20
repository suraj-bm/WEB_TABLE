from django.db import models

class Timetable(models.Model):
    # Choices for days of the week
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    
    # The 'day' field is the simple text representation of the day
    day = models.CharField(max_length=20, null=True, blank=True, help_text="Day of the week for the session.")

    # Time slots as a JSON field (Optional, could be used to hold complex data)
    time_slots = models.JSONField(default=dict, blank=True, null=True)
    
    # Define individual time slot fields
    time_08_00_09_00 = models.CharField(max_length=100, blank=True, null=True)
    time_09_00_10_00 = models.CharField(max_length=100, blank=True, null=True)
    time_10_00_11_00 = models.CharField(max_length=100, blank=True, null=True)
    time_11_00_12_00 = models.CharField(max_length=100, blank=True, null=True)
    time_12_00_13_00 = models.CharField(max_length=100, blank=True, null=True)
    time_13_00_14_00 = models.CharField(max_length=100, blank=True, null=True)
    time_14_00_15_00 = models.CharField(max_length=100, blank=True, null=True)
    time_15_00_16_00 = models.CharField(max_length=100, blank=True, null=True)

    # Time period
    start_time = models.TimeField(help_text="Start time of the session.")
    end_time = models.TimeField(help_text="End time of the session.")

    # Day of the week (a choice field to restrict input)
    day_of_week = models.CharField(
        max_length=9,
        choices=DAY_CHOICES,
        default='Monday',  # Default value
        help_text="Day of the week for the session."
    )

    # Course information
    course_code = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Optional course code."
    )
    course_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Optional course name. If not provided, will be considered 'Free'."
    )
    room = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Optional room number or location."
    )
    instructor = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Optional instructor name."
    )
    
    # Optional for handling breaks or empty slots
    is_break = models.BooleanField(
        default=False,
        help_text="Mark as a break or empty slot."
    )

    def __str__(self):
        return f"{self.day_of_week} {self.start_time} - {self.end_time}"

    def save(self, *args, **kwargs):
        # Set 'day' field to match 'day_of_week' if not provided
        if not self.day:
            self.day = self.day_of_week
        super().save(*args, **kwargs)
