from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView

# Create your views here.
class Metadata(LoginRequiredMixin, generic.TemplateView):
    template_name = 'metadata/metadata.html'


# view for the index page
class MetadataList(LoginRequiredMixin, generic.ListView):
    context_object_name = 'metadata_list'
    template_name = None  # defaults to '{appname}/{modelname}_list.html

    def get_queryset(self):
        return self.model.objects.all()


# view for the station entry page
class MetadataCreate(LoginRequiredMixin, CreateView):
    # the fields mentioned below become the entry rows in the generated form
    fields = '__all__'



class MetadataRead(LoginRequiredMixin, UpdateView):
    # FIXME: MetadataRead should use FormView, but this isn't displaying the data
    # Note: self.kwargs = {'pk': ...}
    pass
    # success_url = '/'
    # def form_valid(self, form):
    #model = Station
    #fields = '__all__'  # fields are specified by model form


# view for the station update page
class MetadataUpdate(LoginRequiredMixin, UpdateView):
    """
    E.g. self.kwargs = {'pk': '1111111'}

    """
    # form_class = UserForm
    # template_name = 'members/user_update.html'
    #model = Station
    # the fields mentioned below become the entry rows in the update form
    fields = '__all__'

    # success_url ="/"



# view for deleting a station entry
class MetadataDelete(LoginRequiredMixin, DeleteView):
    pass
    #model = Station
    # the delete button forwards to the url mentioned below.
    #success_url = reverse_lazy('metadata:station-index')
