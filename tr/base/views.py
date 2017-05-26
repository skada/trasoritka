import json
from django.http import Http404, HttpResponse, JsonResponse


def contact_form_post(request):

    if request.method != 'post' and not request.is_ajax():
        raise Http404()

    if request.user.is_anonymous():
        raise Http404()

    data = request.POST

    return JsonResponse({
        'success': True
    })