# Generated by Django 4.2.4 on 2023-08-30 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-fecha',),
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descripcion', models.TextField()),
                ('stock', models.IntegerField(default=0)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='app.pedido')),
            ],
            options={
                'ordering': ('-nombre',),
            },
        ),
    ]
