# Generated by Django 4.2.1 on 2023-06-21 21:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trak", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="wastecode",
            name="rcra_state",
            field=models.CharField(
                blank=True,
                choices=[
                    ("AK", "Alaska"),
                    ("AL", "Alabama"),
                    ("AP", "Armed Forces Pacific"),
                    ("AR", "Arkansas"),
                    ("AZ", "Arizona"),
                    ("CA", "California"),
                    ("CO", "Colorado"),
                    ("CT", "Connecticut"),
                    ("DC", "District of Columbia"),
                    ("DE", "Delaware"),
                    ("FL", "Florida"),
                    ("GA", "Georgia"),
                    ("GU", "Guam"),
                    ("HI", "Hawaii"),
                    ("IA", "Iowa"),
                    ("ID", "Idaho"),
                    ("IL", "Illinois"),
                    ("IN", "Indiana"),
                    ("KS", "Kansas"),
                    ("KY", "Kentucky"),
                    ("LA", "Louisiana"),
                    ("MA", "Massachusetts"),
                    ("MD", "Maryland"),
                    ("ME", "Maine"),
                    ("MI", "Michigan"),
                    ("MN", "Minnesota"),
                    ("MO", "Missouri"),
                    ("MS", "Mississippi"),
                    ("MT", "Montana"),
                    ("NC", "North Carolina"),
                    ("ND", "North Dakota"),
                    ("NE", "Nebraska"),
                    ("NH", "New Hampshire"),
                    ("NJ", "New Jersey"),
                    ("NM", "New Mexico"),
                    ("NV", "Nevada"),
                    ("NY", "New York"),
                    ("OH", "Ohio"),
                    ("OK", "Oklahoma"),
                    ("OR", "Oregon"),
                    ("PA", "Pennsylvania"),
                    ("PR", "Puerto Rico"),
                    ("RI", "Rhode Island"),
                    ("SC", "South Carolina"),
                    ("SD", "South Dakota"),
                    ("TN", "Tennessee"),
                    ("TX", "Texas"),
                    ("UT", "Utah"),
                    ("VA", "Virginia"),
                    ("VI", "Virgin Islands"),
                    ("VT", "Vermont"),
                    ("WA", "Washington"),
                    ("WI", "Wisconsin"),
                    ("WV", "West Virginia"),
                    ("WY", "Wyoming"),
                ],
                max_length=3,
                null=True,
            ),
        ),
    ]
