from django.shortcuts import render
from .models import JobRequirement
from django.http import HttpResponse
from apps.utils.commons import *
from apps.login.models import *

# Create your views here.
def edit(request, jobInfo_id, id):
    user = User.objects.all()[0]
    request.session['user_id'] = user.id
    set = JobRequirement.objects.filter(pk=id)
    context = {
        'jobInfo_id': jobInfo_id if isNotNull(jobInfo_id, 'str') else '',
        'id': id if isNotNull(id, 'str') else '',
        'jobRequirement': set[0] if len(set) > 0 else None,
    }
    return render(request, 'edit.html', context)

@mirror(JobRequirement())
def save(request, entity):
    user = User.objects.filter(pk=request.session['user_id'])[0]
    entity.updateUser = user.id
    entity.createUser = entity.createUser if isNotNull(entity.createUser, 'str') else user.id
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