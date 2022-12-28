from django import forms
from .models import UserForm, District, WorkExperience, Education, Reference, Course


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = "__all__"
        widgets = {
            'city_we': forms.Select(attrs={'class': 'form-control'}),
            'district_we': forms.Select(attrs={'class': 'form-control'}),
            'job_title_we': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name_we': forms.TextInput(attrs={'class': 'form-control'}),
            'description_we': forms.Textarea(attrs={'class': 'form-control'}),
            'start_date_we': forms.SelectDateWidget(years=range(1970, 2031), attrs={'class': 'form-control'}),
            'end_date_we': forms.SelectDateWidget(years=range(1970, 2031), attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['district_we'].queryset = District.objects.none()

            if 'city' in self.data:
                try:
                    city_id = int(self.data.get('city'))
                    self.fields['district_we'].queryset = District.objects.filter(city_id=city_id).order_by('city_name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['district_we'].queryset = self.instance.city.district_set.order_by('district_name')


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = "__all__"
        widgets = {
            'city_education': forms.Select(attrs={'class': 'form-control'}),
            'district_education': forms.Select(attrs={'class': 'form-control'}),
            'school_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department_name': forms.TextInput(attrs={'class': 'form-control'}),
            'degree_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description_education': forms.Textarea(attrs={'class': 'form-control'}),
            'start_date_education': forms.SelectDateWidget(years=range(1970, 2031), attrs={'class': 'form-control'}),
            'end_date_education': forms.SelectDateWidget(years=range(1970, 2031), attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['district_education'].queryset = District.objects.none()

            if 'city' in self.data:
                try:
                    city_id = int(self.data.get('city'))
                    self.fields['district_education'].queryset = District.objects.filter(city_id=city_id).order_by(
                        'city_name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['district_education'].queryset = self.instance.city.district_set.order_by('district_name')


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = "__all__"
        widgets = {
            'company_name_reference': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name_reference': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name_reference': forms.TextInput(attrs={'class': 'form-control'}),
            'email_reference': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number_reference': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'institution_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description_course': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date_course': forms.SelectDateWidget(years=range(1970, 2024), attrs={'class': 'form-control'}),
            'end_date_course': forms.SelectDateWidget(years=range(1970, 2024), attrs={'class': 'form-control'}),
        }


class UserForms(forms.ModelForm):
    # job_title = forms.CharField(max_length=100)
    # company_name = forms.CharField(max_length=100)
    class Meta:
        model = UserForm
        fields = '__all__'
        widgets = {
            'city_living': forms.Select(attrs={'class': 'form-select'}),
            'district_living': forms.Select(attrs={'class': 'form-select'}),
            'profile_img': forms.FileInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_day': forms.SelectDateWidget(years=range(1970, 2009), attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'marital_status': forms.Select(attrs={'class': 'form-select'}),
            'military_status': forms.Select(attrs={'class': 'form-select'}),
            'driving_license': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'hobby': forms.Textarea(attrs={'class': 'form-control'}),
            'profile': forms.Textarea(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['district_living'].queryset = District.objects.none()

            if 'city' in self.data:
                try:
                    city_id = int(self.data.get('city'))
                    self.fields['district_living'].queryset = District.objects.filter(city_id=city_id).order_by(
                        'city_name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['district_living'].queryset = self.instance.city.district_set.order_by('district_name')

    def save(self, commit=True):
        instance = super(UserForms, self).save(commit=False)

        if commit:
            instance.save()
        return instance


class ExampleForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255, required=True)
    class Meta:
        model = UserForm
        fields = ['first_name', 'phone_number', 'email']

    def clean_email(self):
        print(self.data['email'])


