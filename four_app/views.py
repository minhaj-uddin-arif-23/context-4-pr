from django.shortcuts import render

# Create your views here.
def home(request):
    # dictionary form ah backend teka data nia aste hoy
    d = {'author':"arif","age":20,'List':['python','programming','language'] }
        #  ,'courss':[
    #     {
    #         'id':1,
    #         'name':"python",
    #         'fee':5000
    #     },
    #     {
    #         'id':1,
    #         'name':"python",
    #         'fee':4000
    #     },
    #     {
    #         'id':1,
    #         'name':"python",
    #         'fee':3000
    #     },
    # ]}
    return render(request,'home.html',{'data':d})