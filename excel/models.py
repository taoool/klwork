from django.db import models
import datetime
# Create your models here.
class History(models.Model):
    """导入记录"""
    file_name = models.FileField(upload_to='avatars/', verbose_name=u"文件名字", null=True)
    create_time = models.DateTimeField(verbose_name="导入时间", default=datetime.datetime.now())