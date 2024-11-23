from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    pseudonym = models.CharField(max_length=64, null=True, blank=True)
    age = models.IntegerField()
    retired = models.BooleanField()

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        if self.pseudonym:
            return f"{self.get_full_name()} ({self.pseudonym})"
        return self.get_full_name()
