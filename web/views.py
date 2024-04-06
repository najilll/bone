from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from . models import Banner,Services,ClientLogos,Blog,Testimonial

# Create your views here.
class IndexView(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baner'] = Banner.objects.filter(is_active=True)
        context['services'] = Services.objects.filter(is_active=True)
        context['logos'] = ClientLogos.objects.all()
        context['blog'] = Blog.objects.filter(is_active=True)
        context['testimonial'] = Testimonial.objects.filter(is_active=True)
        return context

def contact(request):
    return render(request,'web/contact.html')


class ServicesDetailView(DetailView):
    model = Services
    template_name = "web/service-details.html"
    

class BlogDetailView(DetailView):
    model = Blog
    template_name = "web/blog-details.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.filter(is_active=True)
        return context