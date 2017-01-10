
from rest_framework.views import APIView
from rest_framework.response import Response

from analytics.models import ClickEvent
from shortener.models import QprttURL

from analytics.api.serializers import AnalyticsSerializer

class ClickEventAPIView(APIView):

	def get(self, request, id, format=None):

		qprtt_url = QprttURL.objects.filter(id=int(id)).first()
		serializer = AnalyticsSerializer(qprtt_url, context={'instance': qprtt_url})
		return Response(serializer.data)