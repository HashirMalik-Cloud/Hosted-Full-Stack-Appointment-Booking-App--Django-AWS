from django.shortcuts import render, get_object_or_404, redirect
from .models import AppointmentSlot
from django.contrib import messages  # For flash messages

def home(request):
    slots = AppointmentSlot.objects.all().order_by('date', 'start_time')
    return render(request, 'home.html', {'slots': slots})

def book_slot(request, slot_id):
    if request.method == 'POST':
        slot = get_object_or_404(AppointmentSlot, id=slot_id)
        if not slot.is_booked:
            slot.is_booked = True
            slot.save()
            messages.success(request, f'Successfully booked slot on {slot.date} from {slot.start_time} to {slot.end_time}.')
        else:
            messages.warning(request, 'This slot has already been booked.')
    return redirect('home')
