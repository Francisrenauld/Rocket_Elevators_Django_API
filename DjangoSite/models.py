from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Employees(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(db_column='First_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=255, blank=True, null=True) 
 # Field name made lowercase.
    title_or_function = models.CharField(db_column='Title_Or_Function', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    #user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    keypoints = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'

