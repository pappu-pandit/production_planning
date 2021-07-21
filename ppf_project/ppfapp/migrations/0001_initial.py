# Generated by Django 2.2.7 on 2021-07-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='closing_balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemcode', models.CharField(max_length=50)),
                ('itemname', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='item_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemcode', models.CharField(max_length=50)),
                ('itemname', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('station_no', models.CharField(max_length=50)),
                ('duration', models.IntegerField(default=None)),
                ('pics_per_ladi', models.IntegerField(max_length=50)),
                ('coupli_or_board_size', models.CharField(max_length=200)),
                ('pics_per_coupli', models.CharField(max_length=100)),
                ('sponge_type', models.CharField(max_length=100)),
                ('sponge_shape', models.CharField(max_length=100)),
                ('l1', models.CharField(max_length=100)),
                ('l1_qty', models.FloatField(max_length=50)),
                ('l2', models.CharField(max_length=100)),
                ('l2_qty', models.FloatField(max_length=50)),
                ('l3', models.CharField(max_length=100)),
                ('l3_qty', models.FloatField(max_length=50)),
                ('l4', models.CharField(max_length=100)),
                ('l4_qty', models.FloatField(max_length=50)),
                ('l5', models.CharField(max_length=100)),
                ('l5_qty', models.FloatField(max_length=50)),
                ('l6', models.CharField(max_length=100)),
                ('l6_qty', models.FloatField(max_length=50)),
                ('l7', models.CharField(default=None, max_length=100)),
                ('l7_qty', models.FloatField(default=None, max_length=50)),
                ('f1', models.CharField(max_length=100)),
                ('f1_qty', models.FloatField(max_length=50)),
                ('f2', models.CharField(max_length=100)),
                ('f2_qty', models.FloatField(max_length=50)),
                ('f3', models.CharField(max_length=100)),
                ('f3_qty', models.FloatField(max_length=50)),
                ('f4', models.CharField(max_length=100)),
                ('f4_qty', models.FloatField(max_length=50)),
                ('f5', models.CharField(max_length=100)),
                ('f5_qty', models.FloatField(max_length=50)),
                ('f6', models.CharField(max_length=100)),
                ('f6_qty', models.FloatField(max_length=50)),
                ('f7', models.CharField(default=None, max_length=100)),
                ('f7_qty', models.FloatField(default=None, max_length=50)),
                ('d1', models.CharField(max_length=100)),
                ('d1_qty', models.FloatField(max_length=50)),
                ('d2', models.CharField(max_length=100)),
                ('d2_qty', models.FloatField(max_length=50)),
                ('d3', models.CharField(max_length=100)),
                ('d3_qty', models.FloatField(max_length=50)),
                ('d4', models.CharField(max_length=100)),
                ('d4_qty', models.FloatField(max_length=50)),
                ('d5', models.CharField(max_length=100)),
                ('d5_qty', models.FloatField(max_length=50)),
                ('d6', models.CharField(max_length=100)),
                ('d6_qty', models.FloatField(max_length=50)),
                ('d7', models.CharField(default=None, max_length=100)),
                ('d7_qty', models.FloatField(default=None, max_length=50)),
                ('item_master_align_id', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='item_master_copy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemcode', models.CharField(max_length=50)),
                ('itemname', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('station_no', models.CharField(max_length=50)),
                ('duration', models.IntegerField(default=None)),
                ('pics_per_ladi', models.IntegerField(max_length=50)),
                ('coupli_or_board_size', models.CharField(max_length=200)),
                ('pics_per_coupli', models.CharField(max_length=100)),
                ('sponge_type', models.CharField(max_length=100)),
                ('sponge_shape', models.CharField(max_length=100)),
                ('l1', models.CharField(max_length=100)),
                ('l1_qty', models.FloatField(max_length=50)),
                ('l2', models.CharField(max_length=100)),
                ('l2_qty', models.FloatField(max_length=50)),
                ('l3', models.CharField(max_length=100)),
                ('l3_qty', models.FloatField(max_length=50)),
                ('l4', models.CharField(max_length=100)),
                ('l4_qty', models.FloatField(max_length=50)),
                ('l5', models.CharField(max_length=100)),
                ('l5_qty', models.FloatField(max_length=50)),
                ('l6', models.CharField(max_length=100)),
                ('l6_qty', models.FloatField(max_length=50)),
                ('l7', models.CharField(default=None, max_length=100)),
                ('l7_qty', models.FloatField(default=None, max_length=50)),
                ('f1', models.CharField(max_length=100)),
                ('f1_qty', models.FloatField(max_length=50)),
                ('f2', models.CharField(max_length=100)),
                ('f2_qty', models.FloatField(max_length=50)),
                ('f3', models.CharField(max_length=100)),
                ('f3_qty', models.FloatField(max_length=50)),
                ('f4', models.CharField(max_length=100)),
                ('f4_qty', models.FloatField(max_length=50)),
                ('f5', models.CharField(max_length=100)),
                ('f5_qty', models.FloatField(max_length=50)),
                ('f6', models.CharField(max_length=100)),
                ('f6_qty', models.FloatField(max_length=50)),
                ('f7', models.CharField(default=None, max_length=100)),
                ('f7_qty', models.FloatField(default=None, max_length=50)),
                ('d1', models.CharField(max_length=100)),
                ('d1_qty', models.FloatField(max_length=50)),
                ('d2', models.CharField(max_length=100)),
                ('d2_qty', models.FloatField(max_length=50)),
                ('d3', models.CharField(max_length=100)),
                ('d3_qty', models.FloatField(max_length=50)),
                ('d4', models.CharField(max_length=100)),
                ('d4_qty', models.FloatField(max_length=50)),
                ('d5', models.CharField(max_length=100)),
                ('d5_qty', models.FloatField(max_length=50)),
                ('d6', models.CharField(max_length=100)),
                ('d6_qty', models.FloatField(max_length=50)),
                ('d7', models.CharField(default=None, max_length=100)),
                ('d7_qty', models.FloatField(default=None, max_length=50)),
                ('item_master_align_id', models.IntegerField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='item_master_main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemcode', models.CharField(max_length=50)),
                ('itemname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='material_requisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mr_parameter', models.CharField(max_length=50)),
                ('mr_entity_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='mrp_bms_closing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyf', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='mrp_bms_opening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyf', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='mrp_linewise_bms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyf', models.CharField(max_length=100)),
                ('itemname', models.CharField(max_length=100)),
                ('station_no', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='mrp_linewise_sponge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponge_type', models.CharField(max_length=100)),
                ('sponge_shape', models.CharField(max_length=100)),
                ('itemname', models.CharField(max_length=100)),
                ('station_no', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='mrp_linewise_store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupli_board', models.CharField(max_length=100)),
                ('itemname', models.CharField(max_length=100)),
                ('station_no', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='mrp_sponge_closing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponge_type', models.CharField(max_length=100)),
                ('sponge_shape', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='mrp_sponge_opening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponge_type', models.CharField(max_length=100)),
                ('sponge_shape', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='mrp_store_closing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupli_board', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='mrp_store_opening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupli_board', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='opening_balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemcode', models.CharField(max_length=50)),
                ('itemname', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='production_completed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemcode', models.CharField(max_length=50)),
                ('itemname', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='production_damage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemcode', models.CharField(max_length=50)),
                ('itemname', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='production_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemcode', models.CharField(max_length=50)),
                ('itemname', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(max_length=100)),
                ('date', models.DateField()),
                ('datetime', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='production_planning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemcode', models.CharField(max_length=50)),
                ('itemname', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
