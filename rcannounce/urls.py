from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'rcannounce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r"^account/signup/$", myproject.views.SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
]



