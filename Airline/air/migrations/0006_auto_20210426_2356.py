

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0005_auto_20210426_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='pincode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
