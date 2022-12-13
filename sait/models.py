from django.db import models

#Создание основной модели
class Uni(models.Model):
    CATEGORY = (
        ("MEDICINE", "MEDICINE"),
        ("ENGINNER", "ENGINEER"),
        ("MOUNTAIN", "MOUNTAIN"),
        ("GOS", "GOS"),
        ("TECHNOLOGIES", "TECHNOLOGIES"),
        ("LANGUAGE", "LANGUAGE"),
    )

    number = models.CharField(max_length=3, null=True)
    tittle = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="", null=True)
    title_ref = models.TextField(null=True)
    ref = models.URLField(null=True)
    category = models.CharField(choices=CATEGORY, null=True, max_length=50)

    def __str__(self):
        return self.tittle
