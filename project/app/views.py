from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Count
from app.models import Hit

def home(request):
    context = RequestContext(request)
    template_name = 'home.html'
    data = {}
    data['all_ips_by_date'] = Hit.objects.extra({'day': 'date(visit_datetime)'}).distinct().order_by('-day', 'url__url', 'ip', 'hits').values('ip', 'day', 'url__url').annotate(hits=Count('url'))
    return render_to_response(template_name, data, context_instance=context)