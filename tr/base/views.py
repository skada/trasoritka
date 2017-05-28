import json
import logging

from django.core.mail import EmailMultiAlternatives
from django.http import Http404, HttpResponse, JsonResponse
from django.template import Template, Context, loader


def contact_form_post(request):

    if request.method != 'post' and not request.is_ajax():
        raise Http404()

    if request.user.is_anonymous():
        raise Http404()

    data = dict(request.POST)

    plain_template = loader.get_template('mail/contact_mail.txt')
    plain_message = plain_template.render(Context(data))

    html_template = loader.get_template('mail/contact_mail.html')
    html_message = html_template.render(Context(data))

    msg = EmailMultiAlternatives(
        "[ALUMNI WEB] message",
        plain_message,
        'noreply@e-smile.cz',
        ['petr.stepan@mensa.cz', ],
        bcc=['jakub@e-smile.cz', 'lukas@e-smile.cz',]
    )
    msg.attach_alternative(html_message, "text/html")

    msg.send(fail_silently=False)

    return JsonResponse({
        'success': True
    })