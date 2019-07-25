
#------------------ django models init --------------------
import os,django,sys
scheduler_dir='/home/nrsc/radha/projects/rqscheduler/DPQRScheduler/scheduler/'
sys.path.insert(0,scheduler_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'scheduler.settings'
django.setup()
#-------------------------------------------------------
from jobs.models import Script,Jobs
from datetime import datetime
from loguru import logger
import time


def printandsleep(arguments):

    log_location="/home/radhakrishna/projects/py/rqscheduler/logs/test_print_n_sleep_2s/"
    required_args=['number','stime','job_id']
    time_now=datetime.now()
    #--------------UPDATING DATABASE------------------------
    curr_job=Jobs.objects.get(job_id=arguments['job_id'])
    curr_job.started_at=time_now
    curr_job.status='IN_PROCESS'
    curr_job.log_location=log_location
    curr_job.save()
    #---------------------------------------------------

    try:
        if all(arg not in arguments.keys() for arg in required_args):
            logger.error('Arguments passed are improper')
            #------------------ FINISH JOB SYNC DB ------------------
            time_now=datetime.now()
            curr_job.finished_at=time_now
            curr_job.status='FAILURE'
            curr_job.result_description='ARGUMENTS ARE IMPROPER'
            curr_job.save()
            #-----------------------------------------------------
            return [90,'Arguments improper']
        d=logger.add(log_location+str(arguments['job_id'])+".log")
        logger.info("Script :  Test , Print n , while sleeping 2s")

        for i in range(1,int(arguments['number'])):
            logger.info(i)

            time.sleep(int(arguments['stime']))
        logger.stop(d)
         #------------------ FINISH JOB SYNC DB ------------------
        time_now=datetime.now()
        curr_job.finished_at=time_now
        curr_job.status='SUCCESSFUL'
        curr_job.result_description='FINISHED PROCESSING'
        curr_job.save()
        #-----------------------------------------------------
        return [100,'Finished_succesfully']
    except Exception as e:
        logger.exception("What??!! :: = > Uncatched Exception")
        logger.stop(d)
         #------------------ FINISH JOB SYNC DB ------------------
        time_now=datetime.now()
        curr_job.finished_at=time_now
        curr_job.status='SUCCESSFUL'
        curr_job.result_description='EXCEPTION OCCURED , CHECK LOG FOR FURTHER ANALYSIS'+str(e)
        curr_job.save()
        #-----------------------------------------------------
        return [110,'Exception occured '+str(e)]





if __name__ == "__main__":
    arguments={
    "number":5,
    "stime":2,
    "jobid":"1231s6"
    }

    x=printandsleep(arguments)
    arguments={
    "number":5,
    "stime":2,
    "jobid":"1231s7"
    }
    x=printandsleep(arguments)
