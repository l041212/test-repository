from django.shortcuts import render
from .models import JobRequirement
from django.http import HttpResponse
from apps.utils.commons import *

# Create your views here.
def edit(request, jobInfo_id, id):
    context = {
        'jobInfo_id': jobInfo_id if isNotNull(jobInfo_id, 'str') else '',
        'id': id if isNotNull(id, 'str') else '',
    }
    return render(request, 'edit.html', context)

@mirror(JobRequirement())
def save(request, entity):
    JobRequirement.save(entity)
    education = request.POST.get('education')
    experience = request.POST.get('experience')
    passTime = request.POST.get('passTime')
    certificate = request.POST.get('certificate')
    major = request.POST.get('major')
    skill = request.POST.get('skill')
    jobrequirement = JobRequirement()
    jobrequirement.education = education
    jobrequirement.experience = experience
    jobrequirement.passTime = passTime
    jobrequirement.certificate = certificate
    jobrequirement.major = major
    jobrequirement.skill = skill
    #@jobrequirement.save()
    return HttpResponse("ok")