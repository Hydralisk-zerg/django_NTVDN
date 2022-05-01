# Generated by Django 4.0.4 on 2022-04-29 09:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lesson_5', '0002_alter_client_discount_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bouquet',
            name='frech_period',
            field=models.DurationField(default=datetime.timedelta(days=5), help_text='Use this field wen you need to have information about bouquet fresh time', null=True),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='price',
            field=models.FloatField(default=1.0, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='diname',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='discount_size',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='invoice',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='client',
            name='second_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='client',
            name='user_uuid',
            field=models.UUIDField(auto_created=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='flower',
            name='Wikipedia',
            field=models.URLField(default='https://www.wikipedia.org/', null=True, unique_for_date='delivered_at'),
        ),
        migrations.AlterField(
            model_name='flower',
            name='could_use_in_bouquet',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='flower',
            name='count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='flower',
            name='delivered_at',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]
