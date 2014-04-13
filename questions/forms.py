from django.forms import ModelForm
from questions.models import Comments

class CommentsForm(ModelForm):
  class Meta:
    model=Comments
    fields = ['content']
