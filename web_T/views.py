from django.shortcuts import render, get_object_or_404, redirect
from .models import Timetable
from .forms import TimetableForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Timetable
from .forms import TimetableForm

TIME_SLOTS = [
    ('time_08_00_09_00', '08:00 - 09:00'),
    ('time_09_00_10_00', '09:00 - 10:00'),
    ('time_10_00_11_00', '10:00 - 11:00'),
    ('time_11_00_12_00', '11:00 - 12:00'),
    ('time_12_00_13_00', '12:00 - 13:00'),
    ('time_13_00_14_00', '13:00 - 14:00'),
    ('time_14_00_15_00', '14:00 - 15:00'),
    ('time_15_00_16_00', '15:00 - 16:00'),
]

from django.shortcuts import render
from .models import Timetable


def timetable_view(request):
    # Retrieve all timetables from the database
    timetables = Timetable.objects.all()
    
    # Create a dictionary to store timetable data based on days
    timetable_slots = {}
    
    # Loop through each timetable entry and organize by day
    for timetable in timetables:
        if timetable.day_of_week not in timetable_slots:
            timetable_slots[timetable.day_of_week] = {}

        # Assuming 'time_slots' is a dictionary stored in the 'time_slots' field
        timetable_slots[timetable.day_of_week][timetable.start_time] = {
            'pk': timetable.pk,  # Add the primary key to the dictionary
            'end_time': timetable.end_time,
            'course_name': timetable.course_name,
            'instructor': timetable.instructor,
            'room': timetable.room
        }

    # Pass the structured data to the template
    return render(request, 'timetable.html', {'timetable_slots': timetable_slots})
def edit_timetable(request, pk):
    # Get the timetable object by its primary key (pk)
    timetable = get_object_or_404(Timetable, pk=pk)

    # Check if the request is POST, meaning the form is being submitted
    if request.method == 'POST':
        form = TimetableForm(request.POST, instance=timetable)
        
        if form.is_valid():
            # Save the updated timetable object
            form.save()
            return redirect('timetable_view')  # Redirect to the timetable list or other desired page
    else:
        # If the request is GET, create the form and populate it with the existing timetable data
        form = TimetableForm(instance=timetable)
    
    return render(request, 'edit_timetable.html', {'form': form})

def add_timetable(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable_view')
    else:
        form = TimetableForm()

    return render(request, 'add_timetable.html', {'form': form})