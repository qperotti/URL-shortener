from datetime import date, timedelta


from django.db import models

from shortener.models import QprttURL

# Create your models here.

class ClickEventManager(models.Manager):

	def create_event(self, instance):
		if isinstance(instance, QprttURL):
			obj, created = self.get_or_create(qprtt_url=instance, timestamp=date.today())
			obj.count +=1
			obj.save()
			return obj.count
		return None

	def clicks_average(self, instance):
		if isinstance(instance, QprttURL):

			data = list()
			for i in range(0,14):
				d = date.today() - timedelta(i)
				obj = self.filter(qprtt_url=instance, timestamp=d).first()
				if not obj:
					data.insert(0,0)
				else:
					data.insert(0,obj.count)
			return data

		return None

	def chart_dates(self):
		
		dates = list()
		for i in range(0,14):
			d = date.today() - timedelta(i)
			dates.insert(0,d)
		
		return dates




class ClickEvent(models.Model):
	qprtt_url = models.ForeignKey(QprttURL)
	count = models.IntegerField(default=0)
	timestamp = models.DateField(auto_now_add=True) #when was created

	objects = ClickEventManager()
	

	def __str__(self):
		return self.qprtt_url.url + " -> " + str(self.count)



