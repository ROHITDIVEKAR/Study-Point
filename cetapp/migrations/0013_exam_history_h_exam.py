# Generated by Django 4.2.1 on 2023-07-13 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cetapp', '0012_exam_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam_history',
            name='h_exam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='h_exam', to='cetapp.exam'),
            preserve_default=False,
        ),
    ]
