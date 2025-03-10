

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('flight_name', models.CharField(max_length=100, null=True)),
                ('airline_number', models.CharField(max_length=100, null=True)),
                ('from_city', models.CharField(choices=[('Bhopal', 'Bhopal'), ('Delhi', 'Delhi'), ('Bengaluru', 'Bengaluru'), ('Pune', 'Pune'), ('Mumbai', 'Mumbai'), ('Patna', 'Patna')], max_length=100, null=True)),
                ('from_city_arrival', models.CharField(max_length=100, null=True)),
                ('from_city_departure', models.CharField(max_length=100, null=True)),
                ('to_city_arrival', models.CharField(max_length=100, null=True)),
                ('to_city_departure', models.CharField(max_length=100, null=True)),
                ('to_city', models.CharField(choices=[('Bhopal', 'Bhopal'), ('Delhi', 'Delhi'), ('Bengaluru', 'Bengaluru'), ('Pune', 'Pune'), ('Mumbai', 'Mumbai'), ('Patna', 'Patna')], max_length=100, null=True)),
                ('days', models.TextField(null=True)),
                ('fare_economy', models.CharField(max_length=100, null=True)),
                ('number_of_seat_e', models.CharField(max_length=100, null=True)),
                ('number_of_seat_b', models.CharField(max_length=100, null=True)),
                ('fare_business', models.CharField(max_length=100, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('booking_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_price', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('airline', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='air.airline')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField(null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking_Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id_pass', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.CharField(blank=True, max_length=100, null=True)),
                ('total_price', models.CharField(blank=True, max_length=100, null=True)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='air.booking')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
