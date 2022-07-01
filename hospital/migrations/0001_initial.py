# Generated by Django 4.0.5 on 2022-06-24 12:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(choices=[('Хирург', 'Хирург'), ('Терапевт', 'Терапевт')], max_length=20)),
                ('full_name', models.CharField(max_length=100)),
                ('inn_code', models.IntegerField(unique=True, verbose_name='ИНН')),
                ('age', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('telephone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HeadDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('inn_code', models.IntegerField(unique=True, verbose_name='ИНН')),
                ('age', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('telephone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('classification_code', models.IntegerField(unique=True, verbose_name='ОКПО')),
                ('region', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Ош', 'Ош'), ('Баткен', 'Баткен'), ('Жалал-Абад', 'Жалал-Абад'), ('Нарын', 'Нарын'), ('Ошская обл.', 'Ошская обл.'), ('Талас', 'Талас'), ('Чуйская обл.', 'Чуйская обл.'), ('Ысык-Кол', 'Ысык-Кол')], default='Кыргызстан', max_length=30)),
                ('ownership_type', models.BooleanField(default=False)),
                ('max_people', models.DecimalField(decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('inn_code', models.IntegerField(unique=True, verbose_name='ИНН')),
                ('age', models.IntegerField()),
                ('telephone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('inn_code', models.IntegerField(unique=True, verbose_name='ИНН')),
                ('age', models.IntegerField()),
                ('telephone', models.CharField(max_length=30)),
                ('diagnose', models.TextField(blank=True)),
                ('is_queue', models.BooleanField(blank=True, null=True, verbose_name='В очереди?')),
                ('attending_doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='patients', to='hospital.doctor')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='nurse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hospital.nurse'),
        ),
    ]