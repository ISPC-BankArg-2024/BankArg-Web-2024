# Generated by Django 3.2 on 2023-05-22 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankarg_ispc', '0002_auto_20230519_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cantidad_cuotas',
            fields=[
                ('id_cantidad_cuotas', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_cuotas', models.IntegerField()),
            ],
            options={
                'verbose_name': 'cantidad_cuota',
                'verbose_name_plural': 'cantidad_cuotas',
                'db_table': 'cantidad_cuotas',
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id_cuenta', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('cbu', models.CharField(max_length=75)),
                ('alias', models.TextField(max_length=150)),
                ('password', models.TextField(max_length=250)),
                ('credito', models.BooleanField(default=True)),
                ('debito', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuentas',
                'db_table': 'Cuenta',
            },
        ),
        migrations.CreateModel(
            name='Tipo_cuota',
            fields=[
                ('id_tipo_cuota', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_cuota', models.TextField(max_length=20)),
            ],
            options={
                'verbose_name': 'tipo_cuota',
                'verbose_name_plural': 'tipos_cuotas',
                'db_table': 'tipo_cuota',
            },
        ),
        migrations.CreateModel(
            name='Tipo_empleado',
            fields=[
                ('id_tipo_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_empleado', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo_Empleado',
                'verbose_name_plural': 'Tipos_Empleados',
                'db_table': 'Tipo_Empleado',
            },
        ),
        migrations.CreateModel(
            name='Tipo_estado_cuenta',
            fields=[
                ('id_tipo_estado_cuenta', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_estado_cuenta', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo_estado_cuenta',
                'verbose_name_plural': 'Tipo_estados_cuentas',
                'db_table': 'Tipo_estado_cuenta',
            },
        ),
        migrations.CreateModel(
            name='Tipo_estado_cuota',
            fields=[
                ('id_tipo_estado_cuota', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_estado_cuota', models.TextField(max_length=20)),
            ],
            options={
                'verbose_name': 'tipo_estado_cuota',
                'verbose_name_plural': 'tipo_estados_cuotas',
                'db_table': 'tipo_estado_cuota',
            },
        ),
        migrations.CreateModel(
            name='Tipo_estado_empleado',
            fields=[
                ('id_tipo_estado_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_estado_empleado', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo_estado_empleado',
                'verbose_name_plural': 'Tipos_estado_empleados',
                'db_table': 'Tipo_estado_empleado',
            },
        ),
        migrations.CreateModel(
            name='Tipo_estado_prestamo',
            fields=[
                ('id_tipo_estado_prestamo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_estado_prestamo', models.TextField(max_length=20)),
            ],
            options={
                'verbose_name': 'Tipo_estado_prestamo',
                'verbose_name_plural': 'Tipo_estados_prestamos',
                'db_table': 'Tipo_estado_prestamo',
            },
        ),
        migrations.CreateModel(
            name='Tipo_estado_tarjeta',
            fields=[
                ('id_tipo_estado_tarjeta', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_estado_tarjeta', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo_estado_tarjeta',
                'verbose_name_plural': 'Tipos_estados_tarjetas',
                'db_table': 'Tipo_estado_tarjeta',
            },
        ),
        migrations.CreateModel(
            name='Tipo_interes',
            fields=[
                ('id_tipo_interes', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_interes', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'tipo_interes',
                'verbose_name_plural': 'tipos_intereses',
                'db_table': 'tipo_interes',
            },
        ),
        migrations.CreateModel(
            name='Tipo_moneda',
            fields=[
                ('id_tipo_moneda', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_moneda', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo_moneda',
                'verbose_name_plural': 'Tipos_monedas',
                'db_table': 'Tipo_moneda',
            },
        ),
        migrations.CreateModel(
            name='Tipo_prestamo',
            fields=[
                ('id_tipo_prestamo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_prestamo', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo_prestamo',
                'verbose_name_plural': 'Tipos_prestamos',
                'db_table': 'Tipo_prestamo',
            },
        ),
        migrations.CreateModel(
            name='Tipo_tarjeta',
            fields=[
                ('id_tipo_tarjeta', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_tarjeta', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo_tarjeta',
                'verbose_name_plural': 'Tipos_tarjetas',
                'db_table': 'Tipo_tarjeta',
            },
        ),
        migrations.CreateModel(
            name='Tipos_contactos',
            fields=[
                ('id_tipo_contacto', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_contacto', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo_contacto',
                'verbose_name_plural': 'Tipos_contactos',
                'db_table': 'Tipo_contacto',
            },
        ),
        migrations.CreateModel(
            name='Tipos_cuentas',
            fields=[
                ('id_tipo_cuenta', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_cuenta', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo_cuenta',
                'verbose_name_plural': 'Tipos_cuentas',
                'db_table': 'Tipos_cuentas',
            },
        ),
        migrations.CreateModel(
            name='Tipos_transferencias',
            fields=[
                ('id_tipo_transferencia', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_transferencia', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo_transferencia',
                'verbose_name_plural': 'Tipos_transferencias',
                'db_table': 'Tipos_transferencias',
            },
        ),
        migrations.AlterModelOptions(
            name='clientes',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelTable(
            name='clientes',
            table='Clientes',
        ),
        migrations.CreateModel(
            name='Transferencias',
            fields=[
                ('id_transferencia', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now=True)),
                ('monto', models.IntegerField()),
                ('cuenta_envio', models.TextField(max_length=50)),
                ('cuenta_recibo', models.TextField(max_length=50)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.clientes')),
                ('id_tipo_transferencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipos_transferencias')),
            ],
            options={
                'verbose_name': 'Tranferencia',
                'verbose_name_plural': 'Transferencias',
                'db_table': 'Transferencias',
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id_tarjeta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_vencimiento', models.DateField()),
                ('numero_tarjeta', models.TextField(max_length=150)),
                ('codigo_seguridad', models.TextField(max_length=150)),
                ('id_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.cuenta')),
                ('id_tipo_estado_tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_estado_tarjeta')),
                ('id_tipo_tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_tarjeta')),
            ],
            options={
                'verbose_name': 'Tarjeta',
                'verbose_name_plural': 'Tarjetas',
                'db_table': 'Tarjeta',
            },
        ),
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id_prestamo', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField()),
                ('interes_mes', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fec_start', models.DateField(auto_now=True)),
                ('fec_venc', models.DateField(auto_now=True)),
                ('id_cantidad_cuota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.cantidad_cuotas')),
                ('id_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.cuenta')),
                ('id_tipo_cuota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_cuota')),
                ('id_tipo_estado_cuota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_estado_cuota')),
                ('id_tipo_estado_prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_estado_prestamo')),
                ('id_tipo_interes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_interes')),
                ('id_tipo_moneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_moneda')),
                ('id_tipo_prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_prestamo')),
            ],
            options={
                'verbose_name': 'Prestamo',
                'verbose_name_plural': 'Prestamos',
                'db_table': 'Prestamos',
            },
        ),
        migrations.CreateModel(
            name='Plazo_fijo',
            fields=[
                ('id_plazo_fijo', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('interes', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.cuenta')),
                ('id_tipo_moneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_moneda')),
            ],
            options={
                'verbose_name': 'Plazo_fijo',
                'verbose_name_plural': 'Plazos_fijos',
                'db_table': 'Plazo_fijo',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='bankarg_ispc.persona')),
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_ingreso', models.DateTimeField()),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=15)),
                ('id_tipo_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_empleado')),
                ('id_tipo_estado_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_estado_empleado')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'Empleado',
            },
            bases=('bankarg_ispc.persona',),
        ),
        migrations.CreateModel(
            name='Cuotas',
            fields=[
                ('id_cuota', models.AutoField(primary_key=True, serialize=False)),
                ('nro_cuota', models.IntegerField()),
                ('fecha_vencimiento', models.DateField()),
                ('fecha_pago', models.DateTimeField(auto_now=True)),
                ('monto', models.IntegerField()),
                ('id_prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.prestamos')),
                ('id_tipo_cuota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_cuota')),
                ('id_tipo_estado_cuota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_estado_cuota')),
            ],
            options={
                'verbose_name': 'Cuotas',
                'verbose_name_plural': 'Cuotas',
                'db_table': 'Cuotas',
            },
        ),
        migrations.CreateModel(
            name='Cuenta_transferencia',
            fields=[
                ('id_cuenta_transferencia', models.AutoField(primary_key=True, serialize=False)),
                ('id_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.cuenta')),
                ('id_transferencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.transferencias')),
            ],
            options={
                'verbose_name': 'Cuenta_trasnferencia',
                'verbose_name_plural': 'Cuentas_trasnferencias',
                'db_table': 'Cuenta_transferencia',
            },
        ),
        migrations.CreateModel(
            name='Cuenta_TipoMoneda',
            fields=[
                ('cod_ctm', models.AutoField(primary_key=True, serialize=False)),
                ('id_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.cuenta')),
                ('id_tipo_moneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_moneda')),
            ],
            options={
                'verbose_name': 'Cuenta_TipoMoneda',
                'verbose_name_plural': 'Cuentas_TiposMonedas',
                'db_table': 'Cuenta_TipoMoneda',
            },
        ),
        migrations.CreateModel(
            name='Cuenta_TipoCuenta',
            fields=[
                ('cod_ctc', models.AutoField(primary_key=True, serialize=False)),
                ('id_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.cuenta')),
                ('id_tipo_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipos_cuentas')),
            ],
            options={
                'verbose_name': 'Cuenta_TipoCuenta',
                'verbose_name_plural': 'Cuentas_TiposCuentas',
                'db_table': 'Cuenta_TipoCuenta',
            },
        ),
        migrations.AddField(
            model_name='cuenta',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.clientes'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='id_tipo_cuenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipos_cuentas'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='id_tipo_estado_cuenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_estado_cuenta'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='id_tipo_moneda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipo_moneda'),
        ),
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id_contactos', models.AutoField(primary_key=True, serialize=False)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.clientes')),
                ('id_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.empleado')),
                ('id_tipo_contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.tipos_contactos')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'db_table': 'Contacto',
            },
        ),
        migrations.CreateModel(
            name='Cliente_Cuenta',
            fields=[
                ('cod_cc', models.AutoField(primary_key=True, serialize=False)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.clientes')),
                ('id_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankarg_ispc.cuenta')),
            ],
            options={
                'verbose_name': 'Cliente_Cuenta',
                'verbose_name_plural': 'Clientes_Cuentas',
                'db_table': 'Cliente_Cuenta',
            },
        ),
    ]
