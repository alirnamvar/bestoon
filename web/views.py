from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from json import JSONEncoder
from datetime import datetime

from web.models import *



# Create your views here.
@csrf_exempt
def submit_expense(request):
    """user submits an expense"""

    # TODO: validate date, user, amount that token might be failed
    this_token = request.POST.get("token")
    this_user = Token.objects.get(token=this_token).user

    if 'date' not in request.POST:
        date = datetime.now()

    Expense.objects.create(user=this_user, amount=request.POST.get("amount"),
        text=request.POST.get("text"), date=date)

    return JsonResponse({"status": "ok"}, encoder=JSONEncoder)


@csrf_exempt
def submit_income(request):
    """user submits an income"""

    # TODO: validate date, user, amount that token might be failed
    this_token = request.POST.get("token")
    this_user = Token.objects.get(token=this_token).user

    if 'date' not in request.POST:
        date = datetime.now()

    Income.objects.create(user=this_user, amount=request.POST.get("amount"),
        text=request.POST.get("text"), date=date)

    return JsonResponse({"status": "ok"}, encoder=JSONEncoder)