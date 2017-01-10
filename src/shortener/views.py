from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.views import View

from analytics.models import ClickEvent

from .models import QprttURL
from .forms import SubmitUrlForm



# Create your views here.

class HomeView(View):

	def get(self, request, *args, **kwargs):
		form = SubmitUrlForm()
		context = {'form': form}		
		return render(request, 'shortener/home.html', context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {'form': form}
		template = 'shortener/home.html'

		if form.is_valid():
			url = form.cleaned_data.get('url')
			if 'http://' not in url:
				url = 'http://' + url
			obj, created = QprttURL.objects.get_or_create(url=url)
			context = {
				'url': obj.url,
				'short_url': request.META['HTTP_HOST'] + '/' + obj.shortcode,
				'created': created,
				'id': obj.id
			}
			if created:
				template = 'shortener/new_url.html'
			else:
				template = 'shortener/old_url.html'


		return render(request, template, context)



class RedirectView(View):

	def get(self, request, shortcode=None, *args, **kwargs):		
		obj = get_object_or_404(QprttURL, shortcode=shortcode)
		ClickEvent.objects.create_event(obj)
		return HttpResponseRedirect(obj.url)