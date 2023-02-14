from .models import Student
from django.forms import ModelForm

class data(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        new_data = {
            "class" : "box"
        }
        self.fields['Name'].widget.attrs.update({'placeholder':"Your Name"})
        self.fields['BoardRollNo'].widget.attrs.update({'placeholder':"Board Roll"})
        self.fields['RegistrationNo'].widget.attrs.update({'placeholder':"Registration No"})
        self.fields['InstituteRoll'].widget.attrs.update({'placeholder':"Institute Roll"})
        self.fields['Technology'].widget.attrs.update({'value':"Computer"})
        self.fields['Shift'].widget.attrs.update({'value':"1st"})
        self.fields['Group'].widget.attrs.update({'value':"B"})
        self.fields['Session'].widget.attrs.update({'value':"21-22"})
        self.fields['FathersName'].widget.attrs.update({'placeholder':"Fathers Name"})
        self.fields['MothersName'].widget.attrs.update({'placeholder':"MothersName"})
        self.fields['Village'].widget.attrs.update({'placeholder':"Village"})
        self.fields['PostOffice'].widget.attrs.update({'placeholder':"Post Office"})
        self.fields['UpaZila'].widget.attrs.update({'placeholder':"UpaZila"})
        self.fields['District'].widget.attrs.update({'placeholder':"District"})
        self.fields['MobileNo'].widget.attrs.update({'placeholder':"Mobile No"})