# Generated by Django 4.0.5 on 2022-06-24 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_doctor_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='headdoctor',
            name='hospital',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='head_doctor', to='hospital.hospital'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='doctors', to='hospital.hospital'),
        ),
    ]
