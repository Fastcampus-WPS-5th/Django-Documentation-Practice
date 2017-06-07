# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 05:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0011_student_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cars',
            field=models.ManyToManyField(related_name='introduction_to_models_students', related_query_name='introduction_to_models_student', to='introduction_to_models.Car'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='cars',
            field=models.ManyToManyField(related_name='introduction_to_models_teachers', related_query_name='introduction_to_models_teacher', to='introduction_to_models.Car'),
        ),
        migrations.AlterField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', related_query_name='manufacturer_car', to='introduction_to_models.Manufacturer'),
        ),
    ]