from django.shortcuts import render
from user_form.forms import UserForms, WorkExperienceForm, EducationForm, ReferenceForm, CourseForm
from user_form.models import UserForm, District, Experience


def create_user_form(request):
    form = UserForms
    work_experience_form = WorkExperienceForm
    education_form = EducationForm
    reference_form = ReferenceForm
    course_form = CourseForm

    if request.method == "POST":
        work_experience_form = WorkExperienceForm(request.POST)
        education_form = EducationForm(request.POST)
        reference_form = ReferenceForm(request.POST)
        course_form = CourseForm(request.POST)

        if work_experience_form.is_valid:
            a = work_experience_form.save()

        if education_form.is_valid:
            b = education_form.save()

        if reference_form.is_valid:
            c = reference_form.save()

        if course_form.is_valid:
            d = course_form.save()

        form = UserForms(request.POST, request.FILES)
        form.data._mutable = True
        form.data["experience"] = Experience.objects.create(work_experience=a, education=b, reference=c,course=d)
        form.data._mutable = False

        if form.is_valid:
            form.save()

    return render(request, "user_form/user_form.html", {'form': form, "work_experience_form":work_experience_form, "education_form": education_form,
                                              "reference_form": reference_form, "course_form": course_form})


def load_districts(request):
    city_id = request.GET.get('city_id')
    districts = District.objects.filter(city_id=city_id).all()
    return render(request, 'user_form/district_dropdown_list_options.html', {'districts': districts})

