# Generated by Django 5.0.3 on 2024-07-20 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_jobs_vacancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone1', models.CharField(max_length=100)),
                ('phone2', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('employed', models.BooleanField()),
                ('skills', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('certifications', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='resume')),
                ('about', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='jobs',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
