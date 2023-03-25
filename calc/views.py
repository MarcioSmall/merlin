from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import VariableForm
from .models import Variable
from django.contrib import messages


class HomeView(CreateView):
    template_name = 'home.html'
    model = Variable
    form_class = VariableForm
    success_url = reverse_lazy('home')

    def form_valid(self, form, *args, **kwargs):
        form.save()
        messages.success(self.request, 'Mensagem enviada !!!')
        return super(HomeView, self).form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar mensagem !!!')
        return super(HomeView, self).form_invalid(form)


"""
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.all().first()
        return context
"""

