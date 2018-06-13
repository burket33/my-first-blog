# Generated by Django 2.0.5 on 2018-06-05 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('underdog', '0010_matchup_home_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameresult',
            name='winner',
            field=models.CharField(choices=[('FAV_TEAM', 'Favorite'), ('UNDER_TEAM', 'Underdog')], default='FAV_TEAM', max_length=15),
        ),
    ]
