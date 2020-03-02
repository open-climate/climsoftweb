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

        # hourly: yearChoice, monthChoice, dayChoice
        # daily: yearChoice, monthChoice, hourChoice
        # monthly: yearChoice


class KeyEntryUpdate(LoginRequiredMixin, UpdateView):
    """
    Due to the way in which key entry forms work, this view is used
    for Read, Update and Create (only Delete is separate).

    """
    pass
    # note: self.kwargs = {'pk': '1111111'}

    # form_class = UserForm
    # template_name = 'members/user_update.html'
    #model = Station
    # the fields mentioned below become the entry rows in the update form
    #fields = '__all__'
    # success_url ="/"

    # def get_object(self, queryset=None):
    #     """
    #     Override UpdateView's `get_object` method to create an empty
    #     record if the record doesn't exist
    #
    #     """
    #     # get the existing object or created a new one
    #     obj, created = Worker.objects.get_or_create(mac=self.kwargs['mac'])
    #
    #     return obj


# view for deleting a key entry form
class KeyEntryDelete(LoginRequiredMixin, DeleteView):
    pass
    #model = Station
    # the delete button forwards to the url mentioned below.
    #success_url = reverse_lazy('metadata:station-index')