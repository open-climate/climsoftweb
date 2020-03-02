from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView

# Create your views here.
class Metadata(LoginRequiredMixin, generic.TemplateView):
    template_name = 'metadata/metadata.html'


class MetadataList(LoginRequiredMixin, generic.ListView):
    context_object_name = 'metadata_list'
    template_name = None  # defaults to '{appname}/{modelname}_list.html
    order_by = None

    def get_queryset(self):
        return self.model.objects.all().order_by(self.order_by) if self.order_by else self.model.objects.all()


class MetadataCreate(LoginRequiredMixin, CreateView):
    # the fields mentioned below become the entry rows in the generated form
    fields = '__all__'


class MetadataRead(LoginRequiredMixin, UpdateView):
    # FIXME: MetadataRead should use FormView, but this isn't displaying the data
    pass


# view for the station update page
class MetadataUpdate(LoginRequiredMixin, UpdateView):
    fields = '__all__'


# view for deleting a station entry
class MetadataDelete(LoginRequiredMixin, DeleteView):
    pass
    #model = Station
    # the delete button forwards to the url mentioned below.
    #success_url = reverse_lazy('metadata:station-index')
