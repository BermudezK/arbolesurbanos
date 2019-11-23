# Generated by Django 2.2.6 on 2019-11-21 22:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='postbase',
            name='img',
        ),
        migrations.AddField(
            model_name='postbase',
            name='titulo',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='denuncia',
            name='text',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='postbase',
            name='post_type',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='postinformativo',
            name='text',
            field=models.TextField(max_length=1000),
        ),
        migrations.AddField(
            model_name='denuncia',
            name='img',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.PostImg'),
            preserve_default=False,
        ),
    ]
