

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0002_auto_20210419_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='send_feedback',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
