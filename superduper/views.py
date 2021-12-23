from  django.conf.urls import url

from django.shortcuts import render,HttpResponse

from django.views.decorators.http import require_GET, require_POST

from django.shortcuts import requests

import json

# Create your views here.


def index(request):
    data = requests.get('https://api.github.com/search/repositories?q=python&sort=stars?page=2')
    content = data.text
    return HttpResponse(content)


def get_data(query,sort,page_num):
    query_params={"q":query, "sort" :sort,"page" :page_num}
    url='https://api.github.com/search/repositories?q=python&sort=stars?page=2'
    print(url)
    r=requests.get(url,params=query_params)
    return r.json()
print(get_data('python','stars',2))













