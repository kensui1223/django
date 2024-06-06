from django.shortcuts import render
from django.shortcuts import render, redirect
from gakuseikanri.Forms import GakuseikanriForm
from gakuseikanri.models import Gakuseikanri

def gsk(request):
    if request.method == "POST":
        form = GakuseikanriForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = GakuseikanriForm()
    return render(request,'index.html',{'form':form})
def show(request):
    gakuseikanris = Gakuseikanri.objects.all()
    return render(request,"show.html",{'gakuseikanris':gakuseikanris})
def edit(request, id):
    gakuseikanri = Gakuseikanri.objects.get(id=id)
    return render(request,"edit.html",{'gakuseikanri':gakuseikanri})
def update(request, id):
    gakuseikanri = Gakuseikanri.objects.get(id=id)
    form =GakuseikanriForm(request.POST, instance = gakuseikanri)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html',{'gakuseikanri':gakuseikanri})
def destroy(request, id):
    gakuseikanri = Gakuseikanri.objects.get(id=id)
    gakuseikanri.delete()
    return redirect("/show")