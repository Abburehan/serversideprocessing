from django.shortcuts import render
def triarea(request):
    context={}
    context['area'] = "0"
    context['l'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        l = request.POST.get('length','0')
        h = request.POST.get('height','0')
        print('request=',request)
        print('Length=',l)
        print('height=',h)
        area = int(l) * int(h)
        context['area'] = area
        context['l'] = l
        context['h'] = h
        print('Area=',area)
    return render(request,'myapp/math.html',context)
