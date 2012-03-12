from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

from decimal import Decimal

def index(request):
    nums = [1.618, 2.71828, 3.14159]
    nums.append(4)
    t = loader.get_template('index.html')
    c = RequestContext(request, {'numbers' : nums})
    return HttpResponse(t.render(c))

def decimals(request):
    denom = request.POST['denominator']
    base = request.POST['base']

    myDec = Decimal(denom, base)

    c = RequestContext(request, { 'denominator' : myDec.denominator, 'base' : myDec.base, 'decimal_data' : myDec.data })

    return render_to_response("decimals.html", c)
