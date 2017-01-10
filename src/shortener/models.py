from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
#from django.contrib.sites.models import site

from .utils import create_shortcode


SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 4)


class QprttURLManager(models.Manager):
	
	def all(self, *args, **kwargs):
		queryset = super(QprttURLManager, self).all(*args, **kwargs)
		return queryset.filter(active=True)

	def refresh_shortcodes(self, items=None):

		#only way to get all() wihtout filtering by active
		queryset = self.filter(id__gte=1)

		if items is not None and isinstance(items, int):
			queryset = queryset.order_by('id')[:items]

		for query in queryset:
			query.shortcode = create_shortcode(query)
			query.save()
			print(query.url, ' new shortcode -> ', query.shortcode)


class QprttURL(models.Model):
	url = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
	updated = models.DateTimeField(auto_now=True) #last time saved
	timestamp = models.DateTimeField(auto_now_add=True) #when was created
	active = models.BooleanField(default=True)

	objects = QprttURLManager()


	def save(self, *args, **kwargs):
		if not self.shortcode or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(QprttURL, self).save(*args, **kwargs)

	def get_short_url(self):
		path = reverse('short_url', kwargs={'shortcode': self.shortcode})
		return path

	def __str__(self):
		return str(self.url)

