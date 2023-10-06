from django.db.models import Avg, Max, Min
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import karbaran
from .models import Product

# Create your views here.
all_post=[
    {'slug':'python-programming',
     'title':'python',
     'author':'shamsaee',
    'image':'pic_python.jpg',
     'date':'1402/02/10',
     'short_description':'iam 20  old',
     'content':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolore ex illum labore nihil quae quas tempora temporibus. Ipsam, laudantium, minima.'},

    {'slug': 'html',
     'title': 'html',
     'author': 'mohamdi',
    'image':'pic_html.png',
     'date': '1402/03/10',
     'short_description': 'mkitdjflhsldfjlkdfjlkjdfk',
     'content': 'dkjflswepowpoeipowordpres'},

    {'slug': 'css',
     'title': 'css',
     'author': 'hamide',
     'date': '1399/10/5',
    'image':'pic_css.png',
     'short_description': 'asdslf;lkf;lkl',
     'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolore ex illum labore nihil quae quas tempora temporibus. Ipsam, laudantium, minima.'},

    {'slug': 'js',
     'title': 'js',
     'author': '1455/05/2',
     'image':'pic_js.png',
     'date': 'younes',
     'short_description': 'nvlkjposodk',
     'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolore ex illum labore nihil quae quas tempora temporibus. Ipsam, laudantium, minima.'},

    {'slug': 'django',
     'title': 'django',
     'author': 'vahed',
     'date': '1399/05/12',
    'image':'pic_django.png',
     'short_description': 'dkjfjsd;',
     'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolore ex illum labore nihil quae quas tempora temporibus. Ipsam, laudantium, minima.'},

]




def get_data(post):
    return post['date']


def all_posts(request):
    return render(request,'blogs/posts.html', {"leatest_post":all_post})


def single_post(request,slug):
    post= next(post for post in all_post if post['slug']==slug )
    return render(request,'blogs/post_details.html',{'post':post})


def index(request):
  #  d=list(all_post)
   # context={'a':d}
    #return render(request,'blogs/index.html',context)
    sorted_post=sorted(all_post,key=get_data)
    leatests=sorted_post[-2:]
    return render(request,'blogs/index.html',{'leatest_post':leatests})

def karbaran_list(request):
    all_karbaran=karbaran.objects.all()
    return render(request,'blogs/list karbaran.html',{'all_karbaran':all_karbaran})

def product_list(request):

        all_product=Product.objects.all().order_by('-price')
        number_of_Product=all_product.count()
        info= all_product.aggregate(Avg('price'),Max('price'),Min('price'),Max('ratings'))

        return render(request,'blogs/product_list.html',{'all_product':all_product,'number_of_Product':number_of_Product,'info':info})

def product_details(request,slug):
    # try:
    #     product=Product.objects.get(id=product_id)
    # except:
    #     raise Http404()
    product = get_object_or_404(Product, slug=slug)
    return render(request,'blogs/product_details.html',{'product':product})