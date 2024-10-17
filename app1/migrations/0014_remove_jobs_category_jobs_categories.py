# Generated by Django 4.2.5 on 2024-10-02 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_messages_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='category',
        ),
        migrations.AddField(
            model_name='jobs',
            name='categories',
            field=models.CharField(choices=[('software development ', 'Software Development'), ('sata science', 'Data Science'), ('marketing', 'Marketing'), ('design', 'Design'), ('sales', 'Sales'), ('human resources', 'human resources'), ('finance', 'Finance'), ('education', 'Education'), ('healthcare', 'Healthcare'), ('customer Service', 'Customer Service'), ('administration', 'Administration'), ('engineering', 'Engineering'), ('construction', 'Construction'), ('retail', 'Retail'), ('transportation', 'Transportation'), ('hospitality', 'Hospitality'), ('legal', 'Legal'), ('media', 'Media'), ('real estate', 'Real Estate'), ('government', 'Government'), ('real estate', 'Real Estate'), ('other', 'Other')], default='marketing', max_length=30, null=True),
        ),
    ]
