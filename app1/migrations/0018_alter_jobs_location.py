# Generated by Django 4.2.9 on 2024-10-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_alter_jobs_categories_alter_jobs_job_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='location',
            field=models.CharField(choices=[('all', 'ALL'), ('trivandrum', 'Trivandrum'), ('kochi', 'Kochi'), ('kollam', 'Kollam'), ('kottayam', 'Kottayam'), ('thrissur', 'Thrissur'), ('palakkad', 'Palakkad'), ('malappuram', 'Malappuram'), ('calicut', 'Calicut'), ('kannur', 'Kannur'), ('wayanad', 'Wayanad'), ('alappuzha', 'Alappuzha'), ('idukki', 'Idukki'), ('kasaragod', 'Kasaragod'), ('pathanamthitta', 'Pathanamthitta')], default='calicut', max_length=30, null=True),
        ),
    ]
