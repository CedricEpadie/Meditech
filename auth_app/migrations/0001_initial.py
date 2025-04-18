# Generated by Django 5.1.7 on 2025-04-12 07:09

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActeMariage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_personne', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ActeNaissance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_enfant', models.CharField(max_length=50)),
                ('lieux_naissance', models.CharField(max_length=50)),
                ('sexe', models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], max_length=50)),
                ('nom_pere', models.CharField(max_length=50)),
                ('lieu_naissance_pere', models.CharField(max_length=50)),
                ('lieu_habitat_pere', models.CharField(max_length=50)),
                ('profession_pere', models.CharField(max_length=50)),
                ('nom_mere', models.CharField(max_length=50)),
                ('lieu_naissance_mere', models.CharField(max_length=50)),
                ('lieu_habitat_mere', models.CharField(max_length=50)),
                ('date_dressage', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Allergie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergene', models.CharField(max_length=50)),
                ('symptomes', models.TextField()),
                ('gravite', models.CharField(max_length=50)),
                ('traitement', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Antecedent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('date_diagnostic', models.DateField()),
                ('traitement', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Commissariat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('lieu', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUrgence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_contact', models.CharField(max_length=50)),
                ('lien', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hopital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('lieu', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.CharField(max_length=250, unique=True)),
                ('groupe_sanguin', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=2)),
                ('rhesus', models.CharField(choices=[('+', 'Positif'), ('-', 'Négatif')], max_length=1)),
                ('face_encoding', models.BinaryField(blank=True, null=True)),
                ('type', models.CharField(choices=[('Patient', 'Patient'), ('Medecin', 'Medecin'), ('Policier', 'Policier')], max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('acte_mariage', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth_app.actemariage')),
                ('acte_naissance', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth_app.actenaissance')),
                ('allergies', models.ManyToManyField(blank=True, to='auth_app.allergie')),
                ('antecedents', models.ManyToManyField(blank=True, to='auth_app.antecedent')),
                ('contacts_urgence', models.ManyToManyField(blank=True, to='auth_app.contacturgence')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialite', models.CharField(blank=True, max_length=50, null=True)),
                ('hopitaux', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.hopital')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Policier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commissariat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.commissariat')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
