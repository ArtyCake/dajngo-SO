# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from questions.models import Questions,Comments
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from questions.forms import CommentsForm
from django.utils import simplejson, formats
from django.core.mail import send_mail

class QuestionsList(ListView):
    context_object_name = 'question_list'
    queryset = Questions.objects.order_by('-create_date')
    paginate_by = 10

# class QuestionDetailView(DetailView):
#     model = Questions
#     context_object_name = 'question'

class QuestionDetailView(ListView,FormMixin):
    form_class = CommentsForm
    def get(self, request, *args, **kwargs):
        self.question = Questions.objects.get(pk=self.kwargs['pk'])
        self.object_list = self.get_queryset()
        self.form = self.get_form(self.get_form_class())
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_queryset(self):
        return Comments.objects.all().filter(question = self.question).order_by('create_date')

    def get_context_data(self,**kwargs):
        context = {
            'object_list':self.object_list,
            'form':self.form,
            'question':self.question,
            'args':kwargs
        }
        return context

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            self.form = self.get_form(self.get_form_class())
            if self.form.is_valid():
                self.form.instance.user = self.request.user
                self.form.instance.create_date = timezone.now()
                self.form.instance.question = Questions.objects.get(pk = request.POST['pk'])
                new_comment = self.form.save()
                data = {
                    'content':new_comment.content,
                    'user':new_comment.user.username,
                    'create_date':new_comment.create_date.strftime("%Y-%m-%d %H:%M")
                }
                message = u"На ваш вопрос '{question}' ответил пользователь {username} ".format(question = new_comment.question.title,username=self.request.user.username)
                send_mail(u"На ваш вопрос ответили", message, u"info@google.com",[new_comment.question.user.email], fail_silently=False)
                return HttpResponse(simplejson.dumps(data), mimetype="application/json")
            else:
                json = simplejson.dumps(self.form.errors, ensure_ascii=False)
                return HttpResponse(json, mimetype="application/json")

class QuestionCreate(CreateView):
    model = Questions
    fields = ['title','content']
    success_url = '/questions/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.create_date = timezone.now()
        form.save()
        return super(QuestionCreate, self).form_valid(form)

