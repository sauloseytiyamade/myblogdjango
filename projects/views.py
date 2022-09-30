from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from .models import projects
import requests

class projects_list(ListView):
    def get(self, request):
        sites_sitemas = projects.objects.all()
        github_json = requests.get('https://api.github.com/users/sauloseytiyamade/repos').json()
        github_all_repos = []
        for project in github_json:
            github_repos = {
                'project_name': project['name'],
                'project_description': project['description'],
                'project_url': project['html_url']
            }
            github_all_repos.append(github_repos)

        for values in sites_sitemas:
            values.tags = values.tags.split(',')

        return render(request, 'projects/projects_list.html', {'sites_sistemas': sites_sitemas, 'github_all_repos': github_all_repos, 'is_active': 'projects'})