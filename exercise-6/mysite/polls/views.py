from typing import Any
from django.db.models import F
from django.db.models.query import QuerySet
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.http import HttpResponse,Http404
"""from django.template import loader"""

from .models import Question,Choice


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request,question_id):  
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        return render( 
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message":" You didn't select a choice",
            },
        )
    else:
        selected_choice.votes = F("votes")+1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))
    



# Create your views here.
"""def index1(request):
    return HttpResponse("Hello I am there with u always")
def index2(request):
    latest_question_list = Question.objects.order_by("-pub_date[:5]")
    output = " , ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list":latest_question_list,
    }
    return HttpResponse(template.render(context,request))
"""
"""def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list":latest_question_list}
    return render(request,"polls/index.html",context)
"""
"""def detail1(request,question_id):
    return HttpResponse("You are looking at qustion %s" %question_id)"""
"""def detail2(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,"polls/detail.html",{"question":question})"""
"""
def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{"question":question})
"""
"""def results1(request,question_id):
    response = "You are looking at qustion %s"
    return HttpResponse("response %question_id")"""
"""
def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/results.html",{"question":question})
"""
"""def vote1(request,question_id):
    return HttpResponse("You are voting at question %s" %question_id)"""
"""
def vote(request,question_id):  
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        return render( 
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message":" You didn't select a choice",
            },
        )
    else:
        selected_choice.votes = F("votes")+1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))
"""
