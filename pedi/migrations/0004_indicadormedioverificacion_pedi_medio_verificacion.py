# Generated by Django 3.2.16 on 2024-05-10 23:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0006_dependenciasinstitucionales_siglas'),
        ('pedi', '0003_actividad_meta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medio_verificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('activo', models.BooleanField(default=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('actividad_meta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedi.actividad_meta')),
                ('digitador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IndicadorMedioVerificacion_Pedi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('total', models.IntegerField()),
                ('anio1', models.IntegerField()),
                ('anio2', models.IntegerField()),
                ('anio3', models.IntegerField()),
                ('anio4', models.IntegerField()),
                ('anio5', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
                ('cumple', models.BooleanField(default=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('digitador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('entidadRespinsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.dependenciasinstitucionales')),
                ('medio_verificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedi.medio_verificacion')),
            ],
        ),
    ]
