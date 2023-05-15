# Generated by Django 3.0.7 on 2021-03-27 03:12

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
            name='SeekerSocialDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(max_length=1005, null=True)),
                ('instagram', models.URLField(max_length=1000, null=True)),
                ('linkden', models.URLField(max_length=1000, null=True)),
                ('others', models.URLField(max_length=1000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SeekerAdditionalDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=105, null=True)),
                ('qualification', models.CharField(max_length=100, null=True)),
                ('skills', models.CharField(max_length=100, null=True)),
                ('preferred_job_category', models.CharField(max_length=100, null=True)),
                ('available_for', models.CharField(max_length=100, null=True)),
                ('preferred_location', models.CharField(max_length=100, null=True)),
                ('work_experience', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seeker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=10, null=True)),
                ('image', models.ImageField(blank=True, default='user.jpg', null=True, upload_to='seeker/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('company_type', models.CharField(max_length=100, null=True)),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='seeker/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]