# Generated by Django 2.2.8 on 2020-06-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190525_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(choices=[('Ahmedabad', 'Ahmedabad'), ('Bengaluru', 'Bengaluru'), ('Chennai', 'Chennai'), ('Chittorgarh', 'Chittorgarh'), ('Jodhpur', 'Jodhpur'), ('Raipur', 'Raipur'), ('Sirohi', 'Sirohi'), ('Pali', 'Pali'), ('Delhi', 'Delhi'), ('Hyderabad', 'Hyderabad'), ('Kanpur', 'Kanpur'), ('Kolkata', 'Kolkata'), ('Mumbai', 'Mumbai'), ('Ratnagiri', 'Ratnagiri'), ('Pune', 'Pune'), ('Surat', 'Surat'), ('Sultanpur', 'Sultanpur'), ('Lucknow', 'Lucknow'), ('Patna', 'Patna'), ('Indore', 'Indore'), ('Vadodara', 'Vadodara'), ('Bhopal', 'Bhopal'), ('Coimbatore', 'Coimbatore'), ('Agra', 'Agra'), ('Meerut', 'Meerut'), ('Madurai', 'Madurai'), ('Guwahati', 'Guwahati'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Tiruchchirappalli', 'Tiruchchirappalli'), ('Kota', 'Kota'), ('Jammu', 'Jammu'), ('Mangalore', 'Mangalore'), ('Ajmer', 'Ajmer'), ('Shillong', 'Shillong'), ('New Delhi', 'New Delhi')], max_length=50),
        ),
    ]
