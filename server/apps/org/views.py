import logging

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.serializers import HaztrakSiteSerializer
from apps.org.services import get_org_sites

logger = logging.getLogger(__name__)


class HaztrakOrgSitesListView(APIView):
    """Retrieve a list of sites for a given Org"""

    @method_decorator(cache_page(60 * 15))
    def get(self, request, *args, **kwargs):
        haztrak_sites = get_org_sites(self.kwargs["org_id"])
        serializer = HaztrakSiteSerializer(haztrak_sites, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
