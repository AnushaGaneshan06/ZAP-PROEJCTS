from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, SignInForm, SearchForm
from . models import *
from django.core.paginator import Paginator
from .forms import BookingForm  # Assuming you have a form for bookings



def home(request):
    return render(request, "Core/index.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            fname = form.cleaned_data["fname"]
            lname = form.cleaned_data["lname"]
            email = form.cleaned_data["email"]
            pass1 = form.cleaned_data["pass1"]

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.Please choose different username")
                return redirect("signup")
            
            if User.objects.filter(email = email).exists():
                messages.error(request, "Email is already exits.")
                return redirect("signup")

            # Create user
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()

            messages.success(request, "Your account has been successfully created.")
            return redirect("signin")
        else:
            messages.error(request, "There was an error with the form.")
    
    else:
        form = SignUpForm() 

    return render(request, "Core/signup.html", {"form": form})

def signin(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            pass1 = form.cleaned_data["pass1"]

            user = authenticate(username=username, password=pass1)

            if user is not None:
                login(request, user)
                fname = user.first_name
                return render(request, "Core/index.html", {"fname": fname})
            else:
                messages.error(request, "Invalid credentials.")
                return redirect("signin")
        else:
            messages.error(request, "There was an error with the form.")
    else:
        form = SignInForm()

    return render(request, "Core/signin.html", {"form": form})

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Successfully Logged Out")
    else:
        messages.info(request, "You are not logged in ")

    return redirect('home')


# --------------------SEARCH------------

def search_districts(request):
    form = SearchForm()
    results = None

    if "query" in request.GET:
        query = request.GET.get("query")
        results = District.objects.filter(name__icontains=query) if query else None  # Case-insensitive search

        district = results.first() if results else None

    return render(request, "Core/search.html", {"form": form, "results": results, "district":district})




# ----------------------------------------MODELS---------------------------------


def temple_list(request):
    search_query = request.GET.get('search', '')
    district = request.GET.get('district', '')
    districts = Temple.objects.values_list('district', flat=True).distinct()

    temples = Temple.objects.all()
    
    if search_query:
        temples = temples.filter(name__icontains=search_query)
    
    if district:
        temples = temples.filter(district=district)

    paginator = Paginator(temples, 6)  # Show 6 temples per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Core/models/temple_list.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'district': district,
        'districts': districts
    })


# -------------------- 



def book_temple(request, temple_id):
    temple = get_object_or_404(Temple, id=temple_id)
    
    if request.method == 'POST':
        # Handling the booking form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        purpose = request.POST.get('purpose')
        
        # Create the booking object
        booking = Booking.objects.create(
            temple=temple,
            name=name,
            email=email,
            phone=phone,
            date=date,
            purpose=purpose
        )
        
        # Redirect to the booking success page
        return redirect('booking_success')  # Ensure this matches the name in URLs
    
    return render(request, 'Core/models/book_temple.html', {'temple': temple})


def booking_success(request):
    return render(request, "Core/models/book_success.html")