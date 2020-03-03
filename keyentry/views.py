from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView

from .models import FormHourly, FormDaily2, FormMonthly


MODEL = {
    'FormHourly': FormHourly,
    'FormDaily2': FormDaily2,
    'FormMonthly': FormMonthly,
}


# Create your views here.
class ContentsView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'keyentry/keyentry_contents.html'


class KeyEntryView(LoginRequiredMixin, View):
    """ Custom view providing customised POST method """
    extra_context = {}

    def get(self, request, *args, **kwargs):
        return render(request, 'keyentry/keyentry_form.html', self.extra_context)

    def post(self, request, *args, **kwargs):
        model_name = request.POST.get('model')
        model = MODEL.get(model_name)
        params = {k.replace('Choice', ''): v for k, v in request.POST.items() if 'Choice' in k}
        if model is not None:
            obj, created = model.objects.get_or_create(**params)
            return HttpResponse(obj.pk, content_type='text/plain')
        else:
            return HttpResponse('', content_type='text/plain')


class KeyEntryUpdate(LoginRequiredMixin, UpdateView):
    """
    Due to the way in which key entry forms work, this view is used
    for Read, Update and Create (only Delete is separate).

    """
    def form_valid(self, form):
        """If the form is valid, save the associated model. Also add user's id and username"""
        self.object = form.save()
        self.object.user_id = self.request.user.id
        self.object.signature = self.request.user.username
        return super().form_valid(form)


class KeyEntryDelete(LoginRequiredMixin, DeleteView):
    pass
