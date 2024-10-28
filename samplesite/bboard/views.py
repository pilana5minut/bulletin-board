from django.shortcuts import render
# Create your views here.
#######################################################################

from django.template import loader
from django.http import HttpResponse
from .models import Bb


######## variant-1 ####################################################
# def index(request):
#     s = 'Объявления\r\n\r\n\r\n'
#     for bb in Bb.objects.order_by('-published'):
#         s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
#     return HttpResponse(s, content_type='text/plain; charset=utf-8')


######## variant-2 ####################################################
# def index(request):
#     template = loader.get_template('bboard/index.html')
#     bbs = Bb.objects.order_by('-published')
#     context = {'bbs': bbs}
#     return HttpResponse(template.render(context, request))


######## variant-3 ####################################################
def index(request):

    bbs = Bb.objects.order_by('-published')
    return render(request, 'bboard/index.html', {'bbs': bbs})
