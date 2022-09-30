from django.shortcuts import render
from .models import about
from django.views.generic.list import ListView
import datetime

class about_list(ListView):
    def age(self):
        current_date = datetime.date.today()
        format_date = int(current_date.strftime('%Y'))
        year_age = 1989
        my_age = format_date - year_age
        return my_age

    def get(self, request):
        graduates = about.objects.filter(category__icontains='pos') | about.objects.filter(category__icontains='gra')
        certifications = about.objects.filter(category__icontains='cer')
        voluntaries = about.objects.filter(category__icontains='vol')
        curses = about.objects.filter(category__icontains='cur')
        my_age = self.age()
        return render(request, 'about/about_list.html', {'graduates': graduates, 'certifications': certifications, 'voluntaries': voluntaries, 'curses': curses, 'my_age': my_age, 'is_active': 'about'})