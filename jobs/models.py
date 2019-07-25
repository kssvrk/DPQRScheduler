from django.db import models
from django.contrib.postgres.fields import JSONField
from datetime import datetime
# Create your models here.
class Script(models.Model):
    script_id=models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #script_name= models.CharField(max_length=30, unique=True)
    script_path=models.CharField(max_length=1000,unique=True)

    def __str__(self):
        return (str(self.script_id)+":"+str(self.script_path))

class Jobs(models.Model):
    #--- status enumeration---
    INPROCESS='IN_PROCESS'
    NOTSTARTED='NOT_STARTED'
    SUCCESSFUL='SUCCESSFUL'
    FAILURE='FAILURE'
    TAKENQ='TAKENQ'

    status_choices=(
    (INPROCESS,'Processing'),
    (NOTSTARTED,'Not_yet_started'),
    (SUCCESSFUL,'Finished_succesfully'),
    (FAILURE,'Failed'),
    (TAKENQ,'Taken_by_Q')
    )
    #-------------------

    job_id=models.AutoField(primary_key=True)
    script=models.ForeignKey(Script,related_name='script',on_delete=models.SET(0))
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)
    arguments= JSONField()
    status=models.CharField(
                            max_length=30,
                            choices=status_choices,
                            default=NOTSTARTED
        )
    started_at=models.DateTimeField(null=True)
    priority=models.IntegerField()
    schedule_at=models.DateTimeField(default=datetime.now,blank=True)
    job_description=models.CharField(max_length=1000)
    result_description=models.CharField(max_length=1000,null=True)
    job_name=models.CharField(max_length=30)
    log_location=models.CharField(max_length=1000,null=True)

    def __str__(self):
        return (str(self.job_name)+":"+str(self.job_id)+":"+str(self.schedule_at))
