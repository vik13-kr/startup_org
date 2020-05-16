from django.shortcuts import (render, get_object_or_404, redirect) # using shortcuts 
from django.http.response import (HttpResponse, Http404)
from django.views.generic import View

from .models import Post
from .forms import PostForm

def post_list(request):
    return render(request,'blog/post_list.html',
            {'post_list':Post.objects.all()})

def post_detail(request, year, month, slug):
    post = get_object_or_404(Post, 
            pub_date__year = year, #lookup method 
            pub_date__month = month,
            slug = slug)
    return render(request, 'blog/blog_detail.html',
           {'post': post} )

class PostCreate(View):
        form_class = PostForm
        template_name = 'blog/post_form.html'

        def get(self, request):
                return render(request,
                        self.template_name,
                        {'form': self.form_class()})
                
        def post(self, request):
                bound_form = self.form_class(request.POST)
                if bound_form.is_valid():
                        new_post = bound_form.save()
                        return redirect(new_post)
                else:
                        return render(request,
                        self.template_name,
                        {'form':bound_form})             

class PostUpdate(View):
        form_class = PostForm
        model = Post
        template_name = 'blog/post_form_update.html'

        def get_object(self, year, month, slug   ):
                return get_object_or_404(
                        self.model,
                        pub_date__year = year,
                        pub_date__month = month,
                        slug = slug
                )
        
        def get(self,request, year, month, slug):
                post = self.get_object(year, month, slug)
                context = {
                        'form': self.form_class(instance= post), #passing an object whose value will be updated or changed.
                        'post': post,
                }
                return render(request, self.template_name, context)
        
        def post(self, request, year, month, slug):
                post = self.get_object(year, month, slug)
                bound_form = self.form_class(request.POST, instance = post)
                if bound_form.is_valid():
                        new_post = bound_form.save()
                        return redirect(new_post)
                else:
                        context = {
                                'form': bound_form,
                                'post': post,
                        }
                return render(request, template_name, context)