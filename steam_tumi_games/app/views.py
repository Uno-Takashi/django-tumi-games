"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from allauth.socialaccount.models import SocialAccount
from django.views.generic import *
from django.contrib.auth.models import User

common_datas={"site_name":"積みゲーで遊ぼう"}

class HomeView(TemplateView):
    template_name = "app/index_logout.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        if self.request.user.is_authenticated:
            self.template_name = "app/index_login.html"

            for account in SocialAccount.objects.filter(user=self.request.user):
                provider_account = account.get_provider_account()
            
            print(provider_account)

        context["title"] = "Home"
        context["year"]=datetime.now().year
        context["common_datas"]=common_datas
        return context




def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
