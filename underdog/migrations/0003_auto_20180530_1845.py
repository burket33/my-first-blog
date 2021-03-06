# Generated by Django 2.0.5 on 2018-05-30 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('underdog', '0002_matchupmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchupmodel',
            name='underdog',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='under', to='underdog.NFLTeam'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='matchupmodel',
            name='favorite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fav', to='underdog.NFLTeam'),
        ),
    ]
