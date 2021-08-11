from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contacts(request):
    """
    Displays a form to make an inquiry. Creates a new Contact object.
    Checks if user has already made an inquiry.
    """
    if request.method == 'POST':
        realtor_email = request.POST['realtor_email']
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry.')
                return redirect('/listings/'+listing_id)

        contact = Contact(
            listing_id=listing_id,
            listing=listing,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
        )
        contact.save()

        # Sends email if inquiry is successful.
        send_mail(
            'Listing Inquiry',
            'Message: ' + listing,
            'noreply@realestateappdjango.com',
            [realtor_email],
            fail_silently=False
        )
        messages.success(request, 'Your message has been submitted!')
        # Directs user to listings page if inquiry is successful.
        return redirect('/listings/'+listing_id)


def delete(request, listing_id):
    """
    View for deleting an existing Contact object.
    Retrieves the Contact object and deletes it.
    """
    user_id = request.user.id
    listing_id = listing_id
    contact = Contact.objects.get(listing_id=listing_id, user_id=user_id)
    contact.delete()
    # Directs user to dashboard if delete is successful.
    return redirect('/accounts/dashboard')
