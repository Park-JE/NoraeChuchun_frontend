# Generated by Django 3.2.4 on 2021-07-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(help_text='Category ID', primary_key=True, serialize=False)),
                ('tag', models.CharField(help_text='Category tag', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='playlist',
            name='tracks',
            field=models.ManyToManyField(related_name='track', through='playlist.PlaylistTrack', to='playlist.Track'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='category',
            field=models.ManyToManyField(related_name='category', to='playlist.Category'),
        ),
    ]