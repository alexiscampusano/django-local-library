# Generated by Django 4.1 on 2022-08-17 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_bookinstance_borrower"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookinstance",
            options={
                "ordering": ["due_back"],
                "permissions": (("can_mark_returned", "Set book as returned"),),
            },
        ),
    ]
