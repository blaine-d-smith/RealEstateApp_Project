from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices

def index(request):
    """
    View for the Home page/index.
    Displays a list of Listing objects.
    """
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    """
    View for the About page.
    Displays a list of Realtor objects.
    """
    realtors = Realtor.objects.order_by('-start_date')
    context = {
        'realtors': realtors
    }

    return render(request, 'pages/about.html', context)
