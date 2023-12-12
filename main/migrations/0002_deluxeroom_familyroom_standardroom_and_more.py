# Generated by Django 4.2.7 on 2023-11-23 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeluxeRoom',
            fields=[
                ('room_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.room')),
            ],
            bases=('main.room',),
        ),
        migrations.CreateModel(
            name='FamilyRoom',
            fields=[
                ('room_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.room')),
            ],
            bases=('main.room',),
        ),
        migrations.CreateModel(
            name='StandardRoom',
            fields=[
                ('room_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.room')),
            ],
            bases=('main.room',),
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='amenities',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='rooms',
        ),
        migrations.RemoveField(
            model_name='hotelamenity',
            name='amenity',
        ),
        migrations.RemoveField(
            model_name='hotelamenity',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='roomoccupancy',
            name='room',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_type',
        ),
        migrations.RemoveField(
            model_name='room',
            name='total_rooms',
        ),
        migrations.AddField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(to='main.amenity'),
        ),
        migrations.AddField(
            model_name='room',
            name='occupied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='room_number',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='EntranceFee',
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
        migrations.DeleteModel(
            name='HotelAmenity',
        ),
        migrations.DeleteModel(
            name='RoomOccupancy',
        ),
    ]