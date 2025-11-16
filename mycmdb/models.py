from django.db import models

class Host(models.Model):
    hostname = models.CharField(max_length=255, verbose_name="Host Name", unique=True, blank = False)
    ip = models.GenericIPAddressField(verbose_name="IP Address", blank = False)
    cpu = models.CharField(max_length=128, null=True, blank=True)
    mem = models.CharField(max_length=128, null=True, blank=True)
    disk = models.CharField(max_length=128, null=True, blank=True)
    desc = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.hostname

    class Meta:
        db_table = "Host"
        ordering = ["hostname"]
        verbose_name = "Equipment"
        verbose_name_plural = "Equipment List"
