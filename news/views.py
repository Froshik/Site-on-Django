from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news' : news})

class NewDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewUpdateView(UpdateView):
    model = Articles
    template_name = 'news/edit_news.html'
    form_class = ArticlesForm
    success_url = '/news/'

class NewDeleteView(DeleteView):
    model = Articles
    template_name = 'news/delete_news.html'
    success_url = '/news/'


def add_news(request):
    msg = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('news_home')
        else:
            msg = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'msg': msg
    }

    return render(request, 'news/add_news.html', data)

