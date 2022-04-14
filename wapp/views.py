import unicodedata

from django.http.response import *
from django.shortcuts import *
from LangIdenApp.Comparison_function import *
import os
from django.views.decorators.csrf import csrf_exempt
import unidecode

@csrf_exempt
def index(request):
	if(str(request.method).lower() == 'get'):
		return render(request, 'index.html')
	else:
		user_input = request.POST.get('user_input')
		print('VIEW_LOG', user_input,len(user_input))

		input = unidecode.unidecode(user_input)
		#print(user_input, len(user_input))

		result = compare(input)
		#print(result)
		return render(request, 'index.html', {
			'result': result[0],
			'user_value': user_input

		})

	

def __str__(self):
	return self.result.encode('utf8')
