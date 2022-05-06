from django.http.response import HttpResponseRedirect
from django.views.generic import (
    TemplateView, CreateView
)
from django.contrib.auth import login
from django.urls import reverse_lazy

from antenna.forms import SignUpForm

class IndexView(TemplateView):
    template_name = 'antenna/pages/index.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'antenna/signup.html'
    success_url = reverse_lazy('antenna:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())