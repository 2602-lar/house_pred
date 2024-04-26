from django.shortcuts import render, redirect
from .forms import PropertyForm
from .models import Property
import pickle
import django_tables2 as tables
from .table import Mytable

# Create your views here.
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            data = list(form.cleaned_data.values())
            print(data)
            f_status = data.pop(-2)
            if f_status == 'furnished':
                data.extend([1,0,0])
            elif f_status == 'unfurnished':
                data.extend([0,1,0])
            else:
                data.extend([0,0,1])
            regressor = pickle.load(open("random_forest.pkl",'rb'))
            result = regressor.predict([data[:-1]])
            form.cleaned_data['predictedprice'] = result[0]
            form.save()
            result_pred = result[0] * 0.012 
            if data[0] <= 50 :
                result = "Area too small for a house !" 
            elif data[1] < 1:
                result = "Invalid details. A house must have at least 1 bedroom !"
            elif data[2] < 1:
                result = "Invalid details. A house must have at least 1 bathroom !"
            elif data[3] < 0:
                result = "Invalid details. Negetive stories ! "
            elif data[9] < 0:
                result = "Invalid details. Negetive parking spaces ! "
            else: 
                result = "Predict House Price : "+" $ " + str(int(result_pred))
            form = PropertyForm()
            return render(request, 'add_property.html', {'form': form,"result2":result})
    else:
        form = PropertyForm()
        return render(request, 'add_property.html', {'form': form})
    
def property_list(request):
    properties = Property.objects.all().order_by('-predictedprice')
    table = Mytable(properties)
    return render(request, 'property_list.html', {'table': table})