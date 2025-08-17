
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone
from django.template.exceptions import TemplateDoesNotExist
from .forms import MailForm
from django.contrib.auth.decorators import login_required



# Mapping courses to templates
course_templates = {
    "CloudDevops": "emails/clouddevops.html",
    "CyberSecurity": "emails/cybersecurity.html",
    "DataAnalysis": "emails/dataanalysis.html",
    "SoftwareEngineering": "emails/softwareengineering.html",
}




def unauthorized_view(request):
    email = request.session.pop('unauthorized_email', None)
    return render(request, 'unauthorized.html', {'email': email})



@login_required(login_url='/accounts/login/')
def home(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            course = form.cleaned_data['course']

            context = {
                'name': name,
                'email': email,
                'subject': subject,
                'course': course,
                'message': message,
                'date': timezone.now().strftime("%B %d, %Y"),
            }

            # Get template or fallback
            template_name = course_templates.get(course, "emails/default.html")

            try:
                html_content = render_to_string(template_name, context)
            except TemplateDoesNotExist:
                html_content = render_to_string("emails/default.html", context)

            email_msg = EmailMultiAlternatives(
                subject=subject,
                body=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
            )
            email_msg.attach_alternative(html_content, "text/html")
            email_msg.send()

            return redirect('success')
    else:
        form = MailForm()

    return render(request, 'home.html', {'form': form})




@login_required(login_url='/accounts/login/')
def success(request):
    return render(request, 'success.html')


