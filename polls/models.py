from django.db import models


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    geo = models.CharField(max_length=100, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    approver = models.CharField(max_length=255, blank=True, null=True)
    approver_date = models.DateField(blank=True, null=True)
    filters = models.TextField(blank=True, null=True)
    parent_project_id = models.IntegerField(blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'
