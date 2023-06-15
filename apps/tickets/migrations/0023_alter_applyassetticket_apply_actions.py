# Generated by Django 3.2.14 on 2022-11-18 03:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tickets', '0022_alter_applyassetticket_apply_actions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyassetticket',
            name='apply_actions',
            field=models.IntegerField(default=1, verbose_name='Actions'),
        ),
        migrations.AlterField(
            model_name='approvalrule',
            name='strategy',
            field=models.CharField(
                choices=[
                    ('org_admin', 'Org admin'), ('custom_user', 'Custom user'),
                    ('super_admin', 'Super admin'), ('super_org_admin', 'Super admin and org admin')
                ], default='super_admin', max_length=64,
                verbose_name='Approve strategy'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='state',
            field=models.CharField(
                choices=[
                    ('pending', 'Open'), ('closed', 'Cancel'),
                    ('reopen', 'Reopen'), ('approved', 'Approved'),
                    ('rejected', 'Rejected')
                ], default='pending', max_length=16, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='type',
            field=models.CharField(
                choices=[
                    ('general', 'General'), ('apply_asset', 'Apply for asset'),
                    ('login_confirm', 'Login confirm'), ('command_confirm', 'Command confirm'),
                    ('login_asset_confirm', 'Login asset confirm')
                ],
                default='general', max_length=64, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='ticketassignee',
            name='state',
            field=models.CharField(
                choices=[
                    ('pending', 'Open'), ('closed', 'Cancel'),
                    ('reopen', 'Reopen'), ('approved', 'Approved'),
                    ('rejected', 'Rejected')
                ], default='pending', max_length=64),
        ),
        migrations.AlterField(
            model_name='ticketflow',
            name='type',
            field=models.CharField(
                choices=[
                    ('general', 'General'), ('apply_asset', 'Apply for asset'),
                    ('login_confirm', 'Login confirm'), ('command_confirm', 'Command confirm'),
                    ('login_asset_confirm', 'Login asset confirm')
                ],
                default='general', max_length=64, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='ticketstep',
            name='state',
            field=models.CharField(
                choices=[
                    ('pending', 'Pending'), ('closed', 'Closed'),
                    ('reopen', 'Reopen'), ('approved', 'Approved'),
                    ('rejected', 'Rejected')
                ], default='pending', max_length=64, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='ticketstep',
            name='status',
            field=models.CharField(
                choices=[('active', 'Active'), ('closed', 'Closed'), ('pending', 'Pending')],
                default='pending', max_length=16),
        ),
    ]
