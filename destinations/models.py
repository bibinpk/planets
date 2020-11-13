from django.db import models


# Create your models here.

class countries(models.Model):
    name = models.CharField(max_length=15, verbose_name="Country name", unique=True)
    small_pic = models.ImageField(upload_to='c_pics', verbose_name="Thumpnail")
    large_pic = models.ImageField(upload_to='c_pics', verbose_name="Picture")
    description = models.CharField(max_length=30, verbose_name="Description")

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Countries'
        verbose_name_plural = 'Countries'


class destinations(models.Model):
    name = models.CharField(max_length=35, verbose_name="Destination name", unique=True)
    country = models.ForeignKey(to='countries', on_delete=models.CASCADE)
    small_pic = models.ImageField(upload_to='d_pics', verbose_name="Thumpnail")
    large_pic = models.ImageField(upload_to='d_pics', verbose_name="Picture")
    s_desc = models.CharField(max_length=30, verbose_name="small Description")
    l_desc = models.TextField(verbose_name="Large Description")

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'


class popular_places(models.Model):
    dest_id = models.ForeignKey(to='destinations', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.dest_id)

    class Meta:
        verbose_name = 'Popular places'
        verbose_name_plural = 'Popular places'


class popular_countries(models.Model):
    cou_id = models.ForeignKey(to='countries', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.cou_id)

    class Meta:
        verbose_name = 'Popular Countries'
        verbose_name_plural = 'Popular Countries'


class slider(models.Model):
    slide_id = models.ForeignKey(to='countries', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.slide_id)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'
