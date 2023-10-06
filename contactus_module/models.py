from django.db import models

# Create your models here.

class contactUs(models.Model):
    title=models.CharField(max_length=300,verbose_name='عنوان')
    email=models.EmailField(max_length=300,verbose_name='email')
    fullname=models.CharField(max_length=300,verbose_name='نام نام خانوادگی')
    message=models.TextField(verbose_name='متن پیام')
    created_date=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    response=models.TextField(verbose_name='متن پیام')
    is_read_by_admin=models.BooleanField(default=False,verbose_name='خوانده شده توسط ادمین')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='تماس باما'
        verbose_name_plural='لیست تماس باما '