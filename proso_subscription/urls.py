from django.conf.urls import patterns, url
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView


urlpatterns = patterns(
    'proso_subscription.views',
    url(r'^(|home)$', ensure_csrf_cookie(TemplateView.as_view(template_name="subscription_home.html")), name='subscription_home'),
    url(r'^mysubscriptions/$', 'my_subscriptions', name='subscription_my_subscriptions'),
    url(r'^plans/$', 'plans', name='subscription_plans'),
    url(r'^myreferrals/$', 'my_referrals', name='subscription_my_referrals'),
    url(r'^subscribe/(?P<description_id>\d+)$', 'subscribe', name='subscription_subscribe'),
)
