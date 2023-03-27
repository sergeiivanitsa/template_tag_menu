from django.views import generic


class IndexView(generic.TemplateView):
    """Класс представления главной страницы"""
    template_name = 'menutree/index.html'
