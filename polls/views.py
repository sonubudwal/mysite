from django.template import RequestContext, loader
from  .models import Questions
from django.http import Http404
from django.shortcuts import get_object_or_404, render
# Create your views hefr

from django.http import HttpResponse

def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))

def detail(request,question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse("You're voting on question %s."%question_id)