from django import forms 
from django.forms import ValidationError

from datetime import datetime


        
        
class RegisterForm(forms.Form):
    fullName  = forms.CharField(label="Nombre Completo",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Completo'}),  min_length=4, max_length=50)
    since     = forms.CharField(label='Check-in',widget=forms.TextInput(attrs={'class':'form-control appointment_date-check-in','placeholder':'Check-in'}))
    weeks     = forms.ChoiceField(label='Número de Semanas',widget=forms.Select(attrs={'class':'form-control','placeholder':'# Semanas'}),choices=(('0','# Semanas'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15')))
               # validators.Regexp('^\w+$' , message="El nombre de usuario debe contener solo letras, números o guiones bajos")
    adult     = forms.ChoiceField(label='Adultos',widget=forms.Select(attrs={'class':'form-control','placeholder':'# Adultos'}),choices=(('0','# Adultos'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')))
    children  = forms.ChoiceField(label='Niños',widget=forms.Select(attrs={'class':'form-control','placeholder':'# Niños'}),choices=(('#','# Niños'),('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')))
    email     = forms.EmailField(label='Correo electronico',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Correo electrónico'}))
 
 

    def clean_since(self):
        since = self.cleaned_data['since'] 
       

        date_object = datetime.strptime(since, '%d/%m/%Y')

        fecha_str = datetime.strftime(date_object, '%Y/%m/%d')
        print(fecha_str)
        today = datetime.today().strftime("%Y/%m/%d")
        if fecha_str < today:
            raise ValidationError('No puede ser una fecha pasada')       
        return since
        

    def clean_weeks(self):
        weeks = self.cleaned_data['weeks'] 
        if weeks=="0":
            raise ValidationError('Debe seleccinar el número de semanas')       
        return weeks
        

    def clean_adult(self):
        adult = self.cleaned_data['adult'] 
        if adult=="0":
            raise ValidationError('Debe seleccinar el número de adultos')       
        return adult
        

    def clean_children(self):
        children = self.cleaned_data['children'] 
        if children=="#":
            raise ValidationError('Debe seleccinar el número de niños')       
        return children
        