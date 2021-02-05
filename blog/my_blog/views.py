from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,TemplateView,DetailView
from my_blog.models import BlogCategory,BlogPost
# Create your views here.

#class CategoryList(ListView):
 #   model = BlogCategory
  #  context_object_name = "category_list"
   # template_name = "my_blog/Home.html"

class MultimodelView(TemplateView):
    template_name = "my_blog/Home.html"
    def get_context_data(self, **kwargs):
        """
        docstring
        """
        context = super(MultimodelView,self).get_context_data(**kwargs)
        context["CateModel"] = BlogCategory.objects.all()
        context["PostModel"] = BlogPost.objects.all()
        return context
class BlogView(DetailView):
    """
    docstring
    """
    model = BlogPost
    template_name = "my_blog/Post.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["Post"] = BlogPost.objects.filter(slug = self.kwargs["slug"])
        context["CateModel"] = BlogCategory.objects.all()
        return context
class CategoryView(TemplateView):
    
    template_name = "my_blog/Category.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["Post"] = BlogPost.objects.filter()
        context["Cat"] = BlogCategory.objects.filter(slug = self.kwargs["slug"])
        
        return context
    