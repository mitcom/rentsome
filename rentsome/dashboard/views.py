from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView, ListView, DetailView

from products.models import Article, Rental


def index(request):
    template = loader.get_template('products/detail.html')
    context = {
        'atricles': Article.objects.all(),
    }
    return HttpResponse(template.render(context, request))


class ArticleList(ListView):
    model = Article

article_list = ArticleList.as_view()


class ArticleCreate(CreateView):
    model = Article
    fields = ['name']

    def get_success_url(self):
        return reverse('article', args=[self.object.id])

article_create = ArticleCreate.as_view()


class ArticleDetail(DetailView):
    model = Article

article_detail = ArticleDetail.as_view()


class RentalList(ListView):
    model = Rental

rental_list = RentalList.as_view()


class RentalCreate(CreateView):
    model = Rental
    fields = ['article', 'begin', 'end']

    def get_success_url(self):
        return reverse('rental', args=[self.object.id])

rental_create = RentalCreate.as_view()


class RentalDetail(DetailView):
    model = Rental

rental_detail = RentalDetail.as_view()
