from django import forms

class MailForm(forms.Form):
    COURSE_CHOICES = [
        ("CloudDevops", "Cloud Devops"),
        ("CyberSecurity", "Cyber Security"),
        ("DataAnalysis", "Data Analysis"),
        ("SoftwareEngineering", "Software Engineering" )
    ]

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={ 'placeholder': 'Type your message here'}))
    course = forms.ChoiceField(choices=COURSE_CHOICES)
