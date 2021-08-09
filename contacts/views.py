from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Creates a new Contact object.
def contacts(request):
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

        # Email
        send_mail(
            'Listing Inquiry',
            'Message: ' + listing,
            'noreply@realestateappdjango.com',
            [realtor_email],
            fail_silently=False
        )

        messages.success(request, 'Your message has been submitted!')

        return redirect('/listings/'+listing_id)


# Deletes a Contact object
def delete(request, listing_id):
    user_id = request.user.id
    listing_id = listing_id
    contact = Contact.objects.get(listing_id=listing_id, user_id=user_id)
    contact.delete()
    return redirect('/accounts/dashboard')
