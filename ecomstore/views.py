from django.contrib.auth import get_user_model
from django.contrib import messages

from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from ecomstore.models import Product, User, Message, Category, Cart
from ecomstore.forms import Productform, Profileform, Loginform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

User = get_user_model()

# Create your views here.


def loginPage(request):
    form = Loginform()

    if request.method == "POST":
        # form = Loginform(request.POST)

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Email or password')

    return render(request, 'ecomstore/login.html', {'form': form})


def logoutPage(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q')
    products = None
    search = True
    if q is not None:
        search = False


        products = Product.objects.filter(
            Q(name__icontains=q) |
            Q(category__name__icontains=q)
        )


    categories = Category.objects.all()

    men_products = Product.objects.filter(category__name__iexact="Men's Wears",)
    women_products = Product.objects.filter(category__name__iexact="Women's Wears",)

    context = {
        'men_products': men_products,
        'women_products': women_products,
        'categories': categories,
        'products': products,
        'search': search,
        'q': q,
    }

    return render(request, 'ecomstore/home.html', context)


def product(request, pk):

    product = Product.objects.get(id=pk)
    products = Product.objects.all()
    comments = product.message_set.all()
    related = None


    def yes():
        global yes
        yes = product.id
        return yes
    yes()


# loop to check for related products using the product category
    for i in products:
        if i.category == product.category and i.id != product.id:
            related = i

    context = {
        'product': product,
        'comments': comments,
        'related': related,
    }
    return render(request, 'ecomstore/product.html', context)


def createProduct(request):
    form = Productform()

    if request.method == 'POST':
        form = Productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'ecomstore/product-form.html', context)


def updateproduct(request, pk):
    product = Product.objects.get(id=pk)

    form = Productform(instance=product)

    if request.method == 'POST':
        form = Productform(request.POST, instance=product)
        if form.is_valid():
            form.save()

        return redirect('profile', pk=request.user.id)
    return render(request, 'ecomstore/update-product.html', {'product': product, 'form': form})


def createProfile(request):
    form = Profileform()

    if request.method == 'POST':
        form = Profileform(request.POST)
        if form.is_valid():
            firstname= request.POST.get('first_name')
            lastname= request.POST.get('last_name')
            email= request.POST.get('email')
            password= request.POST.get('password')

            user = User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                username='Empty',
                password=password,
                email=email)


            return redirect('home')

        else:
            HttpResponse('An error occurred during registration')

    context = {'form': form}
    return render(request, 'ecomstore/profile-form.html', context)


def Profile(request, pk):

    profile = User.objects.get(id=pk)

    products = profile.product_set.all()

    context = {'profile': profile, 'products': products}

    return render(request, 'ecomstore/profile.html', context)


def cartPage(request):
    if request.user.is_authenticated:
        make = None
        products = None
        profile = User.objects.get(id=request.user.id)

        obj = profile.cart_set.all()

        if request.method == 'POST':
            ll = yes
            products = Product.objects.get(id=ll)
            make, created = Cart.objects.get_or_create(
                product=products,
                user=request.user,
            )
            messages.add_message(request, messages.SUCCESS, 'Product Added Successfully')
    else:
        return redirect('login')

    context = {'obj': obj, 'products': products, 'make': make}

    return render(request, 'ecomstore/cart.html', context)


def createReview(request):
    product = Product.objects.get(id=yes)
    if request.method == 'POST':
        review = request.POST.get('review')
        messages = Message.objects.create(
            review=review,
            user=request.user,
            product=product,
        )

    return redirect('product', pk=yes)
