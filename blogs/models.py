from contextlib import nullcontext

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
# Create your models here.
from django.utils.text import slugify


class blogsCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها '


class ProductInformation(models.Model):
    color=models.CharField(max_length=200,verbose_name='رنگ')
    Size=models.CharField(max_length=200,verbose_name='سایز')
    def __str__(self):
        return f'{self.color}--------{self.Size}'
    class Meta:
        verbose_name='اطلاعات تکمیلی'
        verbose_name_plural='لیست اطلاعات تکمیلی'

class ProductTag(models.Model):
    tag=models.CharField(max_length=200,verbose_name='عنوان تگ')
    def __str__(self):
        return f'{self.tag}'
    class Meta:
        verbose_name='تگ محصول'
        verbose_name_plural='نگ محصولات'

class Product(models.Model):
    category = models.ForeignKey(blogsCategory, on_delete=models.CASCADE, null=True, verbose_name='دسته یندی')
    Product_informtion=models.OneToOneField(ProductInformation,on_delete=models.CASCADE,null=True,blank=True,verbose_name='اطلاعات تکمیلی',)
    Product_tag=models.ManyToManyField(ProductTag,verbose_name='تگ محصولات')
    title = models.CharField(max_length=50, verbose_name='نام محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    description = models.CharField(max_length=300, verbose_name='توضیحات محصول')
    is_active = models.BooleanField(verbose_name='موجود/ناموجود بودن محصول')
    ratings = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)],
                                  verbose_name='امتیاز محصول')
    slug = models.SlugField(max_length=400,unique=True,default='', null=False, db_index=True, verbose_name='عنوان در url')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return f'{self.title}---{self.description}----{self.price}'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_absolute_url(self):
        return reverse('Product_detail', args={self.title})


class karbaran(models.Model):
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=20)
    age = models.IntegerField()
    # emailk=models.EmailField()
    is_active = models.BooleanField()
