# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base_Snake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alive', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EnemySnake',
            fields=[
                ('base_snake_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='objects.Base_Snake')),
            ],
            options={
            },
            bases=('objects.base_snake',),
        ),
        migrations.CreateModel(
            name='PlayerSnake',
            fields=[
                ('base_snake_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='objects.Base_Snake')),
            ],
            options={
            },
            bases=('objects.base_snake',),
        ),
        migrations.CreateModel(
            name='SnakeFood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
