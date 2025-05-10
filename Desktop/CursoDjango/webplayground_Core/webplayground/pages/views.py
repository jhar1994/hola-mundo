
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import PageForm
from .models import Page


# Create your views here.
class PagesListView(ListView):
    context_object_name = 'pages'
    model = Page
    
class PageDetailListView(DetailView):
   model=Page
   template_name='pages/page_detail.html'
    
@method_decorator(staff_member_required,name='dispatch')
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    success_url=reverse_lazy('pages:pages')   
     
@method_decorator(staff_member_required,name='dispatch')   
class PageUpdateView(UpdateView):
    model = Page
    form_class =PageForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('pages:update',args=[self.object.id])+'?ok'
    
@method_decorator(staff_member_required,name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url=reverse_lazy('pages:pages')   
    template_name_suffix = '_confirm_delete'    