# Generated by Django 2.2.7 on 2021-03-31 10:36

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
                ('pics_per_ladi', models.IntegerField(max_length=50)),
                ('coupli_or_board_size', models.CharField(max_length=100)),
                ('pics_per_coupli', models.CharField(max_length=100)),
                ('sponge_type', models.CharField(max_length=100)),
                ('sponge_shape', models.CharField(max_length=100)),
                ('layer1', models.CharField(max_length=100)),
                ('l1_qty', models.IntegerField(max_length=50)),
                ('layer2', models.CharField(max_length=100)),
                ('l2_qty', models.IntegerField(max_length=50)),
                ('layer3', models.CharField(max_length=100)),
                ('l3_qty', models.IntegerField(max_length=50)),
                ('layer4', models.CharField(max_length=100)),
                ('l4_qty', models.IntegerField(max_length=50)),
                ('layer5', models.CharField(max_length=100)),
                ('l5_qty', models.IntegerField(max_length=50)),
                ('layer6', models.CharField(max_length=100)),
                ('l6_qty', models.IntegerField(max_length=50)),
                ('finishing1', models.CharField(max_length=100)),
                ('f1_qty', models.IntegerField(max_length=50)),
                ('finishing2', models.CharField(max_length=100)),
                ('f2_qty', models.IntegerField(max_length=50)),
                ('finishing3', models.CharField(max_length=100)),
                ('f3_qty', models.IntegerField(max_length=50)),
                ('finishing4', models.CharField(max_length=100)),
                ('f4_qty', models.IntegerField(max_length=50)),
                ('finishing5', models.CharField(max_length=100)),
                ('f5_qty', models.IntegerField(max_length=50)),
                ('finishing6', models.CharField(max_length=100)),
                ('f6_qty', models.IntegerField(max_length=50)),
                ('decoration1', models.CharField(max_length=100)),
                ('d1_qty', models.IntegerField(max_length=50)),
                ('decoration2', models.CharField(max_length=100)),
                ('d2_qty', models.IntegerField(max_length=50)),
                ('decoration3', models.CharField(max_length=100)),
                ('d3_qty', models.IntegerField(max_length=50)),
                ('decoration4', models.CharField(max_length=100)),
                ('d4_qty', models.IntegerField(max_length=50)),
                ('decoration5', models.CharField(max_length=100)),
                ('d5_qty', models.IntegerField(max_length=50)),
                ('decoration6', models.CharField(max_length=100)),
                ('d6_qty', models.IntegerField(max_length=50)),
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
                ('pics_per_ladi', models.IntegerField(max_length=50)),
                ('coupli_or_board_size', models.CharField(max_length=100)),
                ('pics_per_coupli', models.CharField(max_length=100)),
                ('sponge_type', models.CharField(max_length=100)),
                ('sponge_shape', models.CharField(max_length=100)),
                ('layer1', models.CharField(max_length=100)),
                ('l1_qty', models.IntegerField(max_length=50)),
                ('layer2', models.CharField(max_length=100)),
                ('l2_qty', models.IntegerField(max_length=50)),
                ('layer3', models.CharField(max_length=100)),
                ('l3_qty', models.IntegerField(max_length=50)),
                ('layer4', models.CharField(max_length=100)),
                ('l4_qty', models.IntegerField(max_length=50)),
                ('layer5', models.CharField(max_length=100)),
                ('l5_qty', models.IntegerField(max_length=50)),
                ('layer6', models.CharField(max_length=100)),
                ('l6_qty', models.IntegerField(max_length=50)),
                ('finishing1', models.CharField(max_length=100)),
                ('f1_qty', models.IntegerField(max_length=50)),
                ('finishing2', models.CharField(max_length=100)),
                ('f2_qty', models.IntegerField(max_length=50)),
                ('finishing3', models.CharField(max_length=100)),
                ('f3_qty', models.IntegerField(max_length=50)),
                ('finishing4', models.CharField(max_length=100)),
                ('f4_qty', models.IntegerField(max_length=50)),
                ('finishing5', models.CharField(max_length=100)),
                ('f5_qty', models.IntegerField(max_length=50)),
                ('finishing6', models.CharField(max_length=100)),
                ('f6_qty', models.IntegerField(max_length=50)),
                ('decoration1', models.CharField(max_length=100)),
                ('d1_qty', models.IntegerField(max_length=50)),
                ('decoration2', models.CharField(max_length=100)),
                ('d2_qty', models.IntegerField(max_length=50)),
                ('decoration3', models.CharField(max_length=100)),
                ('d3_qty', models.IntegerField(max_length=50)),
                ('decoration4', models.CharField(max_length=100)),
                ('d4_qty', models.IntegerField(max_length=50)),
                ('decoration5', models.CharField(max_length=100)),
                ('d5_qty', models.IntegerField(max_length=50)),
                ('decoration6', models.CharField(max_length=100)),
                ('d6_qty', models.IntegerField(max_length=50)),
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
