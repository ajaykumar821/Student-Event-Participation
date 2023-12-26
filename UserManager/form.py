from django import forms
from django.contrib.auth.forms import UserCreationForm
from UserManager.models import  User, Event_Committee

class EventCommitteeRegForm(UserCreationForm):

    class Meta:
        model = User
        fields = ( 'fname', 'lname', 'clg', 'stream', 'email', 'contect_no' )

    def save(self):
        user = super(EventCommitteeRegForm, self).save(commit=False)
        user.fname = self.cleaned_data['fname']
        user.lname = self.cleaned_data['lname']
        user.email = self.cleaned_data['email']
        user.contect_no = self.cleaned_data['contect_no']
        user.clg = self.cleaned_data['clg']
        user.stream = self.cleaned_data['stream']
        user.is_event_commitee = True
        user.save()

        return user

class EventCommitteeDetailForm(forms.ModelForm):
    class Meta:
        model = Event_Committee
        fields = ('committee_id', 'yearOfStudy', 'in_sponsorship', 'in_publicity', 'in_criative', 'in_technical', 'in_volunteering', 'in_logistics', 'in_graphics', 'in_eventManagement')
        