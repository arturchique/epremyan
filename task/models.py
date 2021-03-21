from django.core.mail import send_mail
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from simple_history.models import HistoricalRecords

User = get_user_model()


class Record(models.Model):
    user_login = models.CharField(max_length=20, help_text="Логин пользователя, добавившего фотографию")
    upload_datetime = models.DateTimeField(auto_now=True, help_text="Время добавления фотографии")
    image = models.ImageField(upload_to='media')
    history = HistoricalRecords()

    def get_absolute_url(self):
        """ Возвращает URL для доступа к странице книги"""
        return reverse('image-detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super(Record, self).save(*args, **kwargs)
        email_address = User.objects.get(username=self.user_login).email
        send_mail("Тестовое задание",
                  f"Ваша запись сохранена.\nДанные:\n{self.user_login};\n{self.upload_datetime};\n{self.image};",
                  "aepremyan3993@gmail.com", [email_address], fail_silently=False, auth_user="aepremyan3993@gmail.com",
                  auth_password="12torrentino")
