from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from health.models import AppointmentDetails, Department,DoctorDetail, Queries
from django.http import JsonResponse
# Create your views here.

def _process_appointment_form(request):
    if request.method != "POST":
        return None

    doctor_name = request.POST.get('d_doctor_name')
    patient_name = request.POST.get('name')
    patient_email = request.POST.get('email')
    patient_mobile_number = request.POST.get('phone')
    appointment_date = request.POST.get('date')
    appointment_time = request.POST.get('time')
    prescription = request.FILES.get('file')
    message = request.POST.get('message')

    try:
        doctor = DoctorDetail.objects.get(id=doctor_name)
        appointment = AppointmentDetails(
            doctor_name=doctor.doctor_full_name,
            patient_name=patient_name,
            patient_email=patient_email,
            patient_mobile_number=patient_mobile_number,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            prescription=prescription,
            message=message
        )
        appointment.save()
        request.session['appointment_id'] = appointment.id

        patient_subject = 'Appointment Confirmed - Novena Hospital'
        patient_message = (
            f'Dear {patient_name},\n\n'
            f'Your appointment with {doctor.doctor_full_name} has been successfully scheduled for {appointment_date} at {appointment_time}.\n\n'
            'Thank you for choosing Novena Hospital.\n\n'
            'Stay Healthy!\nTeam Novena'
        )
        try:
            send_mail(patient_subject, patient_message, settings.EMAIL_HOST_USER, [patient_email])
        except Exception as e:
            print(f"Email failed: {e}")
            messages.warning(request, "Appointment saved, but we couldn't send the confirmation email.")

        doctor_subject = f'New Appointment Booked - {patient_name}'
        doctor_message = (
            f'Hello {doctor.doctor_full_name},\n\n'
            f'A new patient, {patient_name}, has booked an appointment in your schedule.\n'
            f'Date: {appointment_date}\n'
            f'Time: {appointment_time}\n'
            f'Message from patient: {message}\n\n'
            'Please check your schedule and prepare accordingly.\n\n'
            'Best regards,\nTeam Novena'
        )
        try:
            send_mail(doctor_subject, doctor_message, settings.EMAIL_HOST_USER, [doctor.email])
        except Exception as e:
            print(f"Email failed: {e}")
            messages.warning(request, "Appointment saved, but we couldn't send the confirmation email.")

        return redirect('confirmation')
    except Exception as e:
        messages.error(request, f'Error booking appointment: {e}')
        return None

def index(request):
    departments = Department.objects.all()
    response = _process_appointment_form(request)
    if response:
        return response

    return render(request, 'index.html', {'departments': departments})

def about(request):
    doctor_details=DoctorDetail.objects.all()
    return render(request, 'about.html', {'doctor_details':doctor_details})


def contact(request):
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            # Save the query to the database
            query = Queries(
                name=name,
                email=email,
                subject=subject,
                phone=phone,
                message=message
            )
            query.save()
            print(query)
            # Redirect to a confirmation page or display a success message
            return JsonResponse({'success': 'Your query has been submitted successfully.'})
        return render(request, 'contact.html')
    except Exception as e:
        messages.error(request, f'Error submitting query: {e}')
    return render(request, 'contact.html')


def service(request):
    department_details=Department.objects.all()
    # print(department_details.values())
    return render(request, 'service.html',{'department_details':department_details})

def all_doctors(request,id):
    doctors = DoctorDetail.objects.filter(department_name=id)
    # print(doctors.values())
    return render(request, 'all_doctors.html',{'doctors': doctors})

def single_doctor_details(request,id):
    doctor_single=DoctorDetail.objects.get(id=id)
    # print(doctor_single)
    return render(request, 'doctor_single_details.html',{'doctor_single':doctor_single})

def appointment_book(request, id=None):
    departments = Department.objects.all()
    response = _process_appointment_form(request)
    if response:
        return response
    if id:
        doctor_details = DoctorDetail.objects.get(id=id)
        return render(request, 'appointment.html', {'doctor_details': doctor_details, 'departments': departments})
    else:
        return render(request, 'appointment.html', {'departments': departments})
    

def get_doctors(request):
    if request.method == "POST":
        subject_id = request.POST['subject_id']
        # print(subject_id)
        try:
                doctors = DoctorDetail.objects.filter(
                     department_name=subject_id
                 ).values('id', 'doctor_full_name')
                # print(doctors)
        except Exception:
                data={}
                data['error_message'] = 'error'
                # print(data)
                return JsonResponse(data)

        return JsonResponse(list(doctors.values('id', 'department_name','doctor_full_name')), safe = False) 

def confirmation(request):
    appointment_details = None
    appointment_id = request.session.pop('appointment_id', None)
    if appointment_id:
        try:
            appointment_details = AppointmentDetails.objects.get(id=appointment_id)
        except AppointmentDetails.DoesNotExist:
            appointment_details = None

    return render(request, 'confirmation.html', {'appointment_details': appointment_details})


def subscribe_newsletter(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        subject = 'You have subscribed for HealthCare updates'
        message = 'Thank you for subscribing to our newsletter! We will keep you updated with the latest news and offers from HealthCare.'
        if address:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                messages.success(request, 'Thank you for subscribing! You will receive updates soon.')
            except Exception as e:
                messages.error(request, f'Error sending email: {e}')
        else:
            messages.error(request, 'Email address is required')
        # Redirect back to the referring page
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    return redirect('home')
