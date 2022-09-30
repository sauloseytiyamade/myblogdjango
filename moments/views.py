from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.list import ListView
from moments.models import moment

class moments_list(ListView):
    def get(self, request):
        all_moments = moment.objects.all().order_by('-create_at')
        return render(request, 'moments/moment_list.html', {'moments': all_moments, 'base_url': request.META['HTTP_HOST'], 'is_active': 'home'})
