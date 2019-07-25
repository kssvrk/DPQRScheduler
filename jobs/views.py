from django.shortcuts import render
from django.http import JsonResponse
from .models import Jobs

# Create your views here.
def process_log(request):
    if request.method == 'GET':
        job_id=request.GET['job_id']
        last_line=request.GET['last_line']
        curr_job=Jobs.objects.values('log_location').get(job_id=job_id)
        if(curr_job['log_location']):
            log_path=curr_job['log_location']+"/"+str(job_id)+".log"
            fp = open(log_path)
            log_message={"log_lines":[],"job_id":job_id}
            for i, line in enumerate(fp):
                if(i>=int(last_line)):
                    log_message['log_lines'].append(line)
            log_message['last_line']=i+1
            fp.close()
        else:
            log_message={"error":"JOB DOES NOT EXIST"}
        return render(request, 'jobs/result.html', log_message)
    else:
        job_id=request.POST['job_id']
        last_line=request.POST['last_line']
        curr_job=Jobs.objects.values('log_location').get(job_id=job_id)
        if(curr_job['log_location']):
            log_path=curr_job['log_location']+"/"+str(job_id)+".log"
            fp = open(log_path)
            log_message={"log_lines":[],"job_id":job_id}
            for i, line in enumerate(fp):
                if(i>=int(last_line)):
                    log_message['log_lines'].append(line)
            log_message['last_line']=i+1
            fp.close()
        else:
            log_message={"error":"JOB DOES NOT EXIST"}
        return JsonResponse(log_message)
