from rest_framework import serializers


from analytics.models import ClickEvent
from shortener.models import QprttURL

class AnalyticsSerializer(serializers.ModelSerializer):

	clicks_average = serializers.SerializerMethodField()
	chart_dates = serializers.SerializerMethodField()



	def get_clicks_average(self, obj):
		instance = self.context.get("instance")
		return ClickEvent.objects.clicks_average(instance)

	def get_chart_dates(self, obj):
		return ClickEvent.objects.chart_dates()

	class Meta:
		model = QprttURL
		fields = ('clicks_average', 'chart_dates')


