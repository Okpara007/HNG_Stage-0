from django.http import JsonResponse
from datetime import datetime

def get_info(request):
    data = {
        "email": "chinemeremokpara93@gmail.com",  
        "current_datetime": datetime.utcnow().isoformat() + "Z", 
        "github_url": "https://github.com/Okpara007/HNG_Stage-0"  
    }
    return JsonResponse(data)
