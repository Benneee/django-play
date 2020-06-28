from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice
# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render( request, 'polls/index.html', context)
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
            Return the last five published questions.
            (not including those set to be published in the future)
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     # return HttpResponse("You're looking at question %s." % question_id)
#     context = {'question': question}
#     return render(request, 'polls/detail.html', context)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     # After somebody votes, we redirect to the results page for the question
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'polls/results.html', context)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Re-display the question voting form
        context = {'question': question}
        error_message = 'You did not select any choice'
        print(KeyError, error_message)
        return render(request, 'polls/detail.html', context, error_message)

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data
        # This prevents data from being posted twice if a user hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))
    # return HttpResponse("You're voting on questrion %s." % question_id)