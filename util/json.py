from django.http import JsonResponse

def jsonRes(status,code,payload):
    return JsonResponse({
        "status":status,
        "code":code,
        "payload":payload,
    }
    )