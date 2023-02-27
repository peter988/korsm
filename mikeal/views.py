import random

from django.shortcuts import render

# Create your views here.
from mikeal.models import men , women , kids , handbags , shoes1

arr = []
var = 0

arr1 = []
var1 = 0

arr2 = []
var2 = 0

arr3 = []
var3 = 0

arr4 = []
var4 = 0

def add(request):
    if request.method == 'POST':
        discreption = request.POST.get('dis')
        price = request.POST.get('pr')
        image = request.POST.get('img')
        image1 = request.POST.get('img1')
        categeory = request.POST.get('cat')
        if categeory == 0:
            men.objects.Create(discreption,price,image,image1,categeory)
            var += 1
            arr.append(var)
        if categeory == 1:
            women.objects.Create(discreption,price,image,image1,categeory)
            var1 += 1
            arr1.append(var1)

        if categeory == 2:
            kids.objects.create(discreption,price,image,image1,categeory)
            var2 +=1
            arr2.append(var2)
        if categeory == 3:
            handbags.objects.create(discreption,price,image,image1,categeory)
            var3 +=1
            arr3.append(var3)
        if categeory == 4:
            shoes.objects.create(discreption,price,image,image1,categeory)
            var4 +=1
            arr4.append(var4)
    return render(request,'add.html')



def menfun(request):
    db = men.objects
    rn = []
    for i in range(100):
        h = random.choice(arr)
        rn.append(h)

    desc = [ db.get(id = rn[j]  ).desc for j in range(100) ]
    price = [ db.get(id =rn[j]).price for j in range(100) ] 
    image = [ db.get(id = rn[j]).image for j in range(100)]
    image1 = [ db.get(id =rn[j]).imag1 for j in range(100)]

    products = zip(desc,price,image,image1)

    con = {
        'products': products
    }
    return render(request,'men.html',con)



















def womfun(request):
    db = women.objects
    renum = []
    print(arr1)
    for i in range(8):
        h =  random.choice(arr1)
        renum.append(h)
    con = {
        'disc': [db.get(id = renum[j]).disc for j in range(8)],
        'price': [db.get(id=renum[j]).price for j in range(8)],
        'image': [db.get(id=renum[j]).image for j in range(8)],
        'image1': [db.get(id=renum[j]).image1 for j in range(8)]
    }
    return render(request,'kors2.html',con)

def kidsfun(request):
    db = kids.objects
    renum = []
    print(arr2)
    for i in range(8):
        h =  random.choice(arr2)
        renum.append(h)
    disc = [db.get(id=renum[j]).disc for j in range(4)]
    price = [db.get(id=renum[j]).price for j in range(4)]
    image = [db.get(id=renum[j]).image for j in range(4)]
    image1 = [db.get(id=renum[j]).image1 for j in range(4)]

    products = zip(disc,price,image,image1)

    disc1 = [db.get(id=renum[j]).disc for j in range(4)]
    price1 = [db.get(id=renum[j]).price for j in range(4)]
    image2 = [db.get(id=renum[j]).image for j in range(4)]
    image3 = [db.get(id=renum[j]).image1 for j in range(4)]

    products1 = zip(disc1,price1,image2,image3)

    con = {
        'products':products,
        'products1':products1
    }

    return render(request,'kids.html',con)

def handbagsfun(request):
    db = handbags.objects
    renum = []
    for i in range(8):
        h =  random.choice(arr3)
        renum.append(h)
    disc = [db.get(id=renum[j]).disc for j in range(4)]
    price = [db.get(id=renum[j]).price for j in range(4)]
    image = [db.get(id=renum[j]).image for j in range(4)]
    image1 = [db.get(id=renum[j]).image1 for j in range(4)]

    products = zip(disc, price, image, image1)

    disc1 = [db.get(id=renum[j]).disc for j in range(4)]
    price1 = [db.get(id=renum[j]).price for j in range(4)]
    image2 = [db.get(id=renum[j]).image for j in range(4)]
    image3 = [db.get(id=renum[j]).image1 for j in range(4)]

    products1 = zip(disc1, price1, image2, image3)

    con = {
        'products': products,
        'products1': products1
    }
    return render(request,'hand.html',con)


def shoes(request):
    db = shoes1.objects
    renum = []
    for i in range(8):
        h =  random.choice(arr4)
        renum.append(h)
    print(renum)
    disc = [db.get(id=renum[j]).disc for j in range(4)]
    price = [db.get(id=renum[j]).price for j in range(4)]
    image = [db.get(id=renum[j]).image for j in range(4)]
    image1 = [db.get(id=renum[j]).image1 for j in range(4)]

    products = zip(disc, price, image, image1)

    disc1 = [db.get(id=renum[j]).disc for j in range(4)]
    price1 = [db.get(id=renum[j]).price for j in range(4)]
    image2 = [db.get(id=renum[j]).image for j in range(4)]
    image3 = [db.get(id=renum[j]).image1 for j in range(4)]

    products1 = zip(disc1, price1, image2, image3)

    con = {
        'products': products,
        'products1': products1
    }
    return render(request,'shoes.html',con)


def main(request):
    return  render(request,'index.html')



