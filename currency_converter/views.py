import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CurrencyConvertView(APIView):
    API_URL = 'https://api.freecurrencyapi.com/v1/latest'
    API_KEY = 'fca_live_76nkLFHLak8vSJGvmLogJe6gWR940TkMCfd3Cww7'

    def get(self, request):
        try:
            current_currency = request.GET.get('current_currency', '').upper()
            value = request.GET.get('value', 0)
            convert_to_currency = request.GET.get('convert_to_currency', '').upper()

            # GET request to the external service
            params = {
                'apikey': self.API_KEY,
                'base_currency': current_currency,
                'currencies': convert_to_currency,
            }
            response = requests.get(self.API_URL, params=params)
            response.raise_for_status()  # Check for any request errors

            # Parse the JSON response
            data = response.json()
            conversion_rate = data['data'].get(convert_to_currency)

            response_data = {
                'currency': convert_to_currency,
                'value': float(value) * conversion_rate,
                'conversion_rate': conversion_rate,
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response({'error': f'Error making external request: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

