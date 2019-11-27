from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postbase',
            name='img',
        ),
        migrations.AddField(
            model_name='denuncia',
            name='email',
            field=models.EmailField(default='default@gmail.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postbase',
            name='titulo',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='denuncia',
            name='text',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='postbase',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='PostImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.PostBase')),
            ],
        ),
    ]
