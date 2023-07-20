from django.shortcuts import render

# Create your views here.

import os
from django.http import HttpResponse
from dotenv import load_dotenv
load_dotenv()
def members(request):
    x=os.getenv('KEY')
    return HttpResponse(x)