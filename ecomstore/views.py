from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from ecomstore.models import Product, User, Message, Category, Cart
from ecomstore.forms import Productform, Profileform, Loginform, UpdateProfileform
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
    search = False
    if q is not None:
        search = True

        products = Product.objects.filter(
            Q(name__icontains=q) |
            Q(category__name__icontains=q)
        )

    categories = Category.objects.all()

    men_products = Product.objects.filter(category__name__iexact="Men's Wears", )[0:4]
    women_products = Product.objects.filter(category__name__iexact="Women's Wears", )[0:4]

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
    related = []

    def yes():
        global yes
        yes = product.id
        return yes

    yes()

    # loop to check for related products using the product category
    for i in products:
        if i.category == product.category and i.id != product.id:
            related.append(i)

    context = {
        'product': product,
        'comments': comments,
        'related': related,
    }
    return render(request, 'ecomstore/product.html', context)


def createProduct(request):
    if request.user.is_authenticated:
        form = Productform()
        categories = Category.objects.all()

        if request.method == 'POST':
            form = Productform(request.POST, request.FILES)
            if form.is_valid():
                category_name = request.POST.get('category')
                category, created = Category.objects.get_or_create(name=category_name)
                Product.objects.create(
                    user=request.user,
                    name=request.POST.get('name'),
                    description=request.POST.get('description'),
                    product_image1=request.POST.get('product_image1'),
                    product_image2=request.POST.get('product_image2'),
                    product_image3=request.POST.get('product_image3'),
                    price=request.POST.get('price'),
                    category=category,
                )
                return redirect('home')
    else:
        return redirect('login')
    context = {'form': form, 'categories': categories}

    return render(request, 'ecomstore/product-form.html', context)


def updateproduct(request, pk):
    product = Product.objects.get(id=pk)
    categories = Category.objects.all()

    form = Productform()

    if request.method == 'POST':
        form = Productform(request.POST, instanc=product)

        if form.is_valid():
            form.save()

        return redirect('profile', pk=request.user.id)

    return render(request, 'ecomstore/update-product.html',
                  {'product': product,
                   'form': form,
                   'categories': categories
                   })


def deleteproduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('profile', pk=request.user.id)

    return render(request, 'ecomstore/delete.html', {'obj': product})


def createProfile(request):
    form = Profileform()

    if request.method == 'POST':
        form = Profileform(request.POST)
        if form.is_valid():
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            email = request.POST.get('email')
            password_1 = request.POST.get('password_1')
            password_2 = request.POST.get('password_2')

            if password_1 != password_2:
                messages.add_message(request, messages.ERROR, 'Passwords does not match')

            else:

                user = User.objects.create_user(
                    first_name=firstname,
                    last_name=lastname,
                    username=email,
                    password=password_1,
                    email=email
                )

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


def updateprofile(request, pk):
    profile = User.objects.get(id=pk)
    form = Profileform
    if request.method == 'POST':
        form = Profileform(request.POST)
        if form.is_valid():
            form.save()

        return redirect('profile', pk=request.user.id)

    return render(request, 'ecomstore/update-profile.html', {'form': form})


def cartPage(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        make = None
        products = None
        total_amount = 0
        for i in cart:
            pm = i.product
            total_amount = pm.price + total_amount

        if request.method == 'POST':
            # Get Product id stored in yes in Product view and store in ll
            ll = yes
            products = Product.objects.get(id=ll)
            make, created = Cart.objects.get_or_create(
                product=products,
                user=request.user,
            )
            messages.add_message(request, messages.SUCCESS, 'Product Added Successfully')
            return redirect('product', pk=ll)

    else:
        return redirect('login')

    context = {'cart': cart, 'products': products, 'make': make, 'total_amount': total_amount, }

    return render(request, 'ecomstore/cart.html', context)


def deleteCart(request, pk):

    cart = Cart.objects.get(id=pk)
    if request.method == 'POST':
        cart.delete()
        return redirect('cart')
    return render(request, 'ecomstore/delete.html', {'obj': cart})

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
