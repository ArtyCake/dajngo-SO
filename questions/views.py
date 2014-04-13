from django.shortcuts import render, get_object_or_404
from questions.models import Questions,Comments
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView


class QuestionsList(ListView):
    context_object_name = 'question_list'
    queryset = Questions.objects.order_by('-create_date')
    paginate_by = 10

class QuestionDetailView(DetailView):
    model = Questions
    context_object_name = 'question'

class QuestionCreate(CreateView):
    model = Questions
    fields = ['title','content']
    success_url = '/questions/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.create_date = timezone.now()
        form.save()
        return super(QuestionCreate, self).form_valid(form)

