# Generated by Django 5.1.7 on 2025-04-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_alter_allergie_gravite_alter_allergie_traitement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergie',
            name='gravite',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='allergie',
            name='symptomes',
            field=models.TextField(),
        ),
    ]
