# Generated by Django 2.1 on 2018-08-22 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=40)),
                ('token', models.CharField(db_index=True, help_text='SHA-512 encrypted version of Steemconnect access token', max_length=160)),
            ],
            options={
                'ordering': ('username',),
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(db_index=True)),
                ('author', models.CharField(db_index=True, max_length=40)),
                ('title', models.CharField(db_index=True, max_length=128)),
                ('permlink', models.CharField(db_index=True, max_length=160)),
                ('active', models.DateTimeField(blank=True, help_text='The last time this content was “touched” by voting or reply', null=True)),
                ('tag1', models.CharField(max_length=40)),
                ('tag2', models.CharField(blank=True, max_length=40, null=True)),
                ('tag3', models.CharField(blank=True, max_length=40, null=True)),
                ('tag4', models.CharField(blank=True, max_length=40, null=True)),
                ('tag5', models.CharField(blank=True, max_length=40, null=True)),
                ('flagged', models.BooleanField(default=False, help_text='Indicates if this item has been flagged by moderators')),
                ('net_votes', models.PositiveIntegerField(default=0, help_text='Net positive votes')),
                ('author_payout_value', models.FloatField(default=0, help_text='Tracks the total payout (in SBD) this content has received over time')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(help_text='The main SteemQA application tag', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='FavouriteTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(db_index=True)),
                ('author', models.CharField(db_index=True, max_length=40)),
                ('title', models.CharField(db_index=True, max_length=128)),
                ('permlink', models.CharField(db_index=True, max_length=160)),
                ('active', models.DateTimeField(blank=True, help_text='The last time this content was “touched” by voting or reply', null=True)),
                ('tag1', models.CharField(max_length=40)),
                ('tag2', models.CharField(blank=True, max_length=40, null=True)),
                ('tag3', models.CharField(blank=True, max_length=40, null=True)),
                ('tag4', models.CharField(blank=True, max_length=40, null=True)),
                ('tag5', models.CharField(blank=True, max_length=40, null=True)),
                ('flagged', models.BooleanField(default=False, help_text='Indicates if this item has been flagged by moderators')),
                ('net_votes', models.PositiveIntegerField(default=0, help_text='Net positive votes')),
                ('author_payout_value', models.FloatField(default=0, help_text='Tracks the total payout (in SBD) this content has received over time')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Scraper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodes', models.TextField(default='api.steemit.com,steemd.minnowsupportproject.org,steemd.privex.io,steemd.steemgigs.org,steemd.steemit.com,rpc.curiesteem.com,rpc.steemliberator.com,rpc.steemviz.com', help_text='The steem nodes to use (in order of priority)')),
                ('oldest_author', models.TextField(blank=True, null=True)),
                ('oldest_permlink', models.TextField(blank=True, null=True)),
                ('new_posts_wait_time', models.PositiveIntegerField(default=60, help_text='The amount of time (in seconds) to wait before fetching new posts')),
                ('post_batch_size', models.PositiveIntegerField(default=50, help_text='The number of posts to get from the Steemd node per operation')),
            ],
        ),
        migrations.CreateModel(
            name='SteemUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(db_index=True, max_length=40)),
            ],
            options={
                'ordering': ('username',),
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(db_index=True, max_length=40, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_topic', to='steem.Topic')),
            ],
            options={
                'ordering': ('topic',),
            },
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='steem.Topic'),
        ),
        migrations.AddField(
            model_name='favouritetopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='steem.Topic'),
        ),
        migrations.AddField(
            model_name='favouritetopic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='steem.SteemUser'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='steem.Question'),
        ),
    ]