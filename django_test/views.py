from django.http import JsonResponse

def get_data(request):
    # Sample data (replace with your own)
    data = {
        'message': 'This is a simple API GET endpoint.',
        'status': 'success'
    }
    
    return JsonResponse(data)
