from django.shortcuts import (render, get_object_or_404, redirect) # using shortcuts 
from django.http.response import (HttpResponse, Http404) # for generating error 404 page 
from django.views.generic import View #for creating class based view(CBV)
#from django.template import Context, loader
from .models import Tag, Startup
from .forms import TagForm, StartupForm, NewsLinkForm
from .utils import ObjectCreateMixin

class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'organiser/tag_form.html'

class StartupCreate(ObjectCreateMixin, View):
    form_class = StartupForm
    template_name = 'organiser/startup_form.html'

class NewslinkCreate(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name = 'organiser/newslink_form.html'

def tag_list(request):
    return render(request,
                    'organiser/tag_list.html',
                    {'tag_list': Tag.objects.all()})

def tag_detail(request,slug):
    tag = get_object_or_404(Tag, slug__iexact = slug)
    return render(request,
                    'organiser/tag_detail.html',
                    {'tag': tag})

def startup_list(request):
    return render(request,
                'organiser/startup_list.html',
                {'startup_list': Startup.objects.all()})

def startup_detail(request,slug):
    startup = get_object_or_404(Startup, slug__iexact = slug)
    return render(request,
            'organiser/startup_detail.html',
            {'startup_detail': startup})

'''function based views for handling forms 
    def create_tag(request):
        if request.method == "POST":
            form = TagForm(request.POST)
            if form.is_valid():
                new_tag  = form.save()
                return redirect(new_tag)        
        else:
            form = TagForm()
        return render(request, 'organiser/tag_form.html', {'form': form})'''

''' class based views for handling forms
    class TagCreate(View):
        form_class = TagForm
        template_name = 'organiser/tag_form.html'

        def get(self,request):
            return render(request, self.template_name, {'form': self.form_class()})
        
        def post(self,request):
            bound_form = self.form_class(request.POST)
            if bound_form.is_valid():
                new_tag = bound_form.save()
                return redirect(new_tag)
            else :
                return render(request,
                        self.template_name,
                        {'form': bound_form})'''
