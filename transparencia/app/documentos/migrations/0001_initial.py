# Generated by Django 2.0 on 2017-12-15 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_archivo', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=500)),
                ('like', models.IntegerField(default='0', null=True)),
                ('dislike', models.IntegerField(default='0', null=True)),
                ('archivo', models.FileField(upload_to='Documentos/')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
    ]
