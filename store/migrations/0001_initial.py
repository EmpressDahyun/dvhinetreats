# Generated by Django 3.2.9 on 2022-04-10 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Category Title')),
                ('slug', models.SlugField(max_length=55, verbose_name='Category Slug')),
                ('description', models.TextField(blank=True, verbose_name='Category Description')),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Category Image')),
                ('is_active', models.BooleanField(verbose_name='Is Active?')),
                ('is_featured', models.BooleanField(verbose_name='Is Featured?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='DeliveryInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_name', models.CharField(max_length=150, verbose_name='Juan Dela Cruz')),
                ('phone_number', models.CharField(default='+63', max_length=13, verbose_name='Phone Number')),
                ('telephone_number', models.CharField(blank=True, default='(062)', max_length=12, verbose_name='Telephone Number')),
                ('barangay', models.CharField(max_length=150, verbose_name='Barangay')),
                ('landmark', models.CharField(max_length=150, verbose_name='Landmark')),
                ('street_name', models.CharField(max_length=150, verbose_name='House/Unit/Flr #, Bldg Name, Blk or Lot #')),
                ('city', models.CharField(default='Zamboanga City', max_length=150, verbose_name='City')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery', verbose_name='Gallery Image')),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='Upload Date')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='ReservationProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Product Title')),
                ('slug', models.SlugField(max_length=160, verbose_name='Product Slug')),
            ],
            options={
                'verbose_name_plural': 'Reservation Products',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default='+63', max_length=13, verbose_name='Phone Number')),
                ('telephone_number', models.CharField(blank=True, default='(062)', max_length=12, verbose_name='Telephone Number')),
                ('pax', models.PositiveIntegerField(default=1, verbose_name='Number of Guest')),
                ('event_name', models.CharField(max_length=150, verbose_name='Event Name')),
                ('event_type', models.CharField(max_length=150, verbose_name='Event Type')),
                ('event_date', models.DateField(verbose_name='Event Date')),
                ('event_time', models.TimeField(unique_for_date='event_date', verbose_name='Event Time')),
                ('event_time_end', models.TimeField(unique_for_date='event_date', verbose_name='Event Time End')),
                ('remarks', models.TextField(blank=True, verbose_name='Remarks')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50)),
                ('reservation_product', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='store.reservationproducts', verbose_name='Reservation Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Product Title')),
                ('slug', models.SlugField(max_length=160, verbose_name='Product Slug')),
                ('sku', models.CharField(max_length=255, unique=True, verbose_name='Unique Product ID (SKU)')),
                ('short_description', models.TextField(verbose_name='Short Description')),
                ('detail_description', models.TextField(blank=True, null=True, verbose_name='Detail Description')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Product Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_active', models.BooleanField(verbose_name='Is Active?')),
                ('is_featured', models.BooleanField(verbose_name='Is Featured?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category', verbose_name='Product Categoy')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('ordered_date', models.DateTimeField(auto_now_add=True, verbose_name='Ordered Date')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.deliveryinformation', verbose_name='Delivery Address')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Customer Favorites',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
