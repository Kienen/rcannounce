from django.conf.urls import patterns, include, url
from django.contrib import admin
from participant import views as participant_views

urlpatterns = [
    # Examples:
    url(r'^$', participant_views.home_page, name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r"^account/signup/$", myproject.views.SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
]



