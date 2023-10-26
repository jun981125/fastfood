import json

from django.http import HttpResponse
from django.shortcuts import render

from pro19app.models import Producttab


# Create your views here.
def main(request):
	return render(request,'main.html')

def admin(request):
	pass

def insert(request):
	pass


def list(request):
	category = request.GET['category']
	data = Producttab.objects.filter(category=category)
	data_result=[]
	for p in data:
		dictdata = {

			'pname':p.pname,
			'description':p.description,
			'price':p.price,
			'stock':p.stock,
		}

		data_result.append(dictdata)

	return HttpResponse(json.dumps(data_result),content_type='application/json')


def payment(request):
	print(request.GET['datas'])
	#datas =json.loads(request.GET['datas'])
#	data_result=[]
#	print(datas)
	#for p in datas:
	#	print(p.stock)
	return HttpResponse('aa')
	#data_result.append(dictdata)
	#return HttpResponse(json.dumps(datas),content_type='application/json')