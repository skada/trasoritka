import json
from django.http import Http404, HttpResponse


def contact_form_post(request):

    if request.method != 'post' and not request.is_ajax():
        raise Http404()

    data = request.POST
    print(data)

    return HttpResponse({
        'content_type': "tre"
    }, content_type='application/json')