import sys
from loguru import logger
import time

def printandsleep(arguments):
    log_location="/home/radhakrishna/projects/py/rqscheduler/logs/test_print_n_sleep_2s/"
    required_args=['number','stime','jobid']
    try:
        if all(arg not in arguments.keys() for arg in required_args):
            logger.error('Arguments passed are improper')
            return [90,'Arguments improper']
            #exit()
        #logger.enable()
        #logger.start(sys.stderr)
        #logger.start(sys.stdout)
        d=logger.add(log_location+str(arguments['jobid'])+".log")
        logger.info("Script :  Test , Print n , while sleeping 2s")
        #logger.add(sys.stderr, format="{time} {level} {message}")
        #logger.add(sys.stdout, format="{time} {level} {message}")
        #logger.opt(exception=True).info("Error stacktrace added to the log message")
        for i in range(1,int(arguments['number'])):
            logger.info(i)

            time.sleep(int(arguments['stime']))
            #logger.disable()
        #logger.disable()
        logger.stop(d)
        return [100,'Finished_succesfully']
    except Exception as e:
        logger.exception("What??!! :: = > Uncatched Exception")
        #logger.close()
        #logger.stop(x)
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
