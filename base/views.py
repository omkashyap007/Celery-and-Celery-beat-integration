from django.shortcuts import render
from base.tasks import (
    updateCount , 
    getApiData , 
)
import json

def homePage(request , *args , **kwargs) :
    # updateCount.delay(json.dumps(1))
    getApiData.delay()
    return render(request , "base/homePage.html" , context = {})