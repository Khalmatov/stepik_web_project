from django import forms
from django.contrib.auth.models import User
from .models import Question, Answer
from django.shortcuts import get_object_or_404


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, user=None, *args, **kwargs):
        if not user:
            self._user = User.objects.get(id=1)
        else:
            self._user = user
        super(AskForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(AskForm, self).clean()
        title = self.cleaned_data['title']
        text = self.cleaned_data['text']
        if (not title) or (not text):
            raise forms.ValidationError(u'message incorrect!')
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()

    def __init__(self, user=None, *args, **kwargs):
        if not user:
            self._user = User.objects.get(id=1)
        else:
            self._user = user
        super(AnswerForm, self).__init__(*args, **kwargs)

    def clean(self):
        text = self.cleaned_data['text']
        if "spam" in text:
            raise forms.ValidationError(u'message incorrect!')
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        self.cleaned_data['question'] = get_object_or_404(Question, pk=self.cleaned_data['question'])
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
