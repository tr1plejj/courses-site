from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    users = models.ManyToManyField(User)
    is_opened = models.BooleanField(default=True)
    to_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'group'

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    purchased_products = models.ManyToManyField(Product, blank=True)
    groups = models.ManyToManyField(Group, blank=True)

    class Meta:
        db_table = 'user'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)
