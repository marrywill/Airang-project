# Generated by Django 2.2.15 on 2020-09-17 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200910_1645'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='substory',
            name='back_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='MySubstory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_id', models.IntegerField(blank=True, null=True)),
                ('is_end', models.BooleanField()),
                ('substory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Substory')),
            ],
        ),
        migrations.CreateModel(
            name='MyStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('story_name', models.CharField(max_length=30)),
                ('mystory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='substories', to='stories.MySubstory')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mystories', to='stories.Story')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mystories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mycharacters', to='stories.Character')),
                ('family', models.ManyToManyField(related_name='mycharacters', to='accounts.Family')),
                ('mystory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mycharacters', to='stories.MyStory')),
            ],
        ),
    ]