from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=64)
    video_url = models.URLField()

    class Meta:
        db_table = 'lesson'

    def __str__(self):
        return self.name


class Product(models.Model):
    author = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    start_time = models.DateTimeField()
    max_users_in_group = models.IntegerField()
    min_users_in_group = models.IntegerField()
    included_lessons = models.ManyToManyField(Lesson)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=64)
    is_opened = models.BooleanField(default=True)
    to_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'group'

    def __str__(self):
        return self.name


class User(models.Model):
    login = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    purchased_products = models.ManyToManyField(Product, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.login
