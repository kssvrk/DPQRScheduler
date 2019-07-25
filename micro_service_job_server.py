
#------------------ django models init --------------------
import os,django,sys
scheduler_dir='/home/nrsc/radha/projects/rqscheduler/DPQRScheduler/scheduler/'
sys.path.insert(0,scheduler_dir) 
os.environ['DJANGO_SETTINGS_MODULE'] = 'scheduler.settings'
django.setup()
#-------------------------------------------------------
from rq import Queue
from redis import Redis,ConnectionPool
import time
from jobs.models import Script,Jobs
from datetime import datetime
from loguru import logger

#------------------- JOBS-LIST ----------------
from scripts.TestScripts.BasicTests import printandsleep
#----------------------------------------------
log_path='/home/nrsc/radha/projects/rqscheduler/logs/job_server/'

logger.add(log_path+"file_{time}.log",rotation="500 MB")

loaded_scripts={
    "printandsleep":printandsleep
}

polling_time=10

def JobServerLoop():
    #------------ JOB SERVING MECHANISM ----------------------

    # 1) status=NOT_STARTED , Scheduled at <= now , order by priority.

    #---------------------------------------------------------

    #------------ REDIS JOB QUEUE ----------------------
    pool =ConnectionPool(host='localhost', port=6379)
    redis_conn=Redis(connection_pool=pool)
    q = Queue(connection=redis_conn)
    #--------------------------------------------------
    time_now=datetime.now()
    print('')
    jobs_torun=Jobs.objects.values('job_id', 'script_id','arguments').filter(status='NOT_STARTED').filter(schedule_at__lt=time_now).order_by('priority')
    results=list(jobs_torun)
    for rjob in results:
        logger.info("PUSHING JOB TO QUEUE "+str(rjob))
        arguments=rjob['arguments']
        arguments['job_id']=rjob['job_id']
        rscript=Script.objects.values('script_path').get(script_id=rjob['script_id'])
        method_to_call = loaded_scripts[rscript['script_path']]
        #PUSH TO QUEUE
        job = q.enqueue(method_to_call, arguments)




if __name__=="__main__":
    while(True):
        logger.info('...Fetching Pending Jobs...')
        JobServerLoop()
        time.sleep(polling_time)