from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Chưa được kiểm duyệt"),
    (1,"Đã được kiểm duyệt")
)

# Create your models here.
class DangBan(models.Model):
    product_name = models.CharField(max_length=250)
    cover = models.ImageField(upload_to='images/')
    description = models.TextField()
    product_price = models.CharField(max_length=10,null=True)
    link_Facebook = models.URLField(null = True)
    created_on = models.DateTimeField(auto_now_add=True,null = True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.product_name

class DangMua(models.Model):
    product_name = models.CharField(max_length=250)
    cover = models.ImageField(upload_to='images/')
    description = models.TextField()
    link_Facebook = models.URLField(null = True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.product_name