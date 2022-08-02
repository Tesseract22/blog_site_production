from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone
# Create your models here.


class Article(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # ���±��⡣models.CharField Ϊ�ַ����ֶΣ����ڱ���϶̵��ַ������������
    title = models.CharField(max_length=100)

    # �������ġ���������ı�ʹ�� TextField
    body = models.TextField()

    # ���´���ʱ�䡣���� default=timezone.now ָ�����ڴ�������ʱ��Ĭ��д�뵱ǰ��ʱ��
    created = models.DateTimeField(default=timezone.now)

    # ���¸���ʱ�䡣���� auto_now=True ָ��ÿ�����ݸ���ʱ�Զ�д�뵱ǰʱ��
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.title