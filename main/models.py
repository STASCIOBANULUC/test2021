from django.db import models


class Transaction(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    surname = models.CharField(max_length=200, verbose_name="Фамилия")
    uuid = models.IntegerField(verbose_name="uuid")
    plate_number = models.CharField(max_length=200, null=True, blank=True)
    group = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    direction = models.CharField(max_length=200, null=True, blank=True)
    status = models.IntegerField()
    type_passage = models.CharField(max_length=200)
    photo = models.ImageField(null=True, blank=True)
    sync = models.BooleanField()

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


