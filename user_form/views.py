from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from user_form.forms import UserForms, WorkExperienceForm, EducationForm, ReferenceForm, CourseForm, ExampleForm
from user_form.models import UserForm, District, Experience, Language, LanguageLevel


def index(request):
    return render(request, 'user_form/home.html')

def about(request):
    return render(request, 'user_form/about.html')

def design_page(request):
    return render(request, 'user_form/design_page.html')

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
            instance = form.save()
            return redirect('user_pdf_view',instance.id)

    return render(request, "user_form/user_form.html", {'form': form, "work_experience_form":work_experience_form, "education_form": education_form,
                                              "reference_form": reference_form, "course_form": course_form})



def users_render_pdf_view(request, id):
    # pk = kwargs.get('pk')
    user = get_object_or_404(UserForm, pk=id)

    template_path = 'user_form/generate_pdf.html'
    context = {'user': user}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf;charset=utf-8')

    # to directly download the pdf we need attachment
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # to view on browser we can remove attachment
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    print(html)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def load_districts(request):
    city_id = request.GET.get('city_id')
    districts = District.objects.filter(city_id=city_id) # todo: cache
    return render(request, 'user_form/district_dropdown_list_options.html', {'districts': districts})

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def load_lang_levels(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == "POST":
        lang_id = request.POST.get('lang_id')
        lang_levels = Language.objects.get(id = lang_id).levels.all()
        return render(request, 'user_form/lang_levels_dropdown_list_options.html', {'lang_levels': lang_levels})
    return ""


def load_ability_levels(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == "POST":
        ability_id = request.POST.get('ability_id')
        ability_levels = Language.objects.get(id = ability_id).levels.all()
        return render(request, 'user_form/ability_levels_dropdown_list_options.html', {'ability_levels': ability_levels})
    return ""




def example(request):
    context = dict()
    form = ExampleForm

    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            print("valid e girdi")

        print(form.errors)

    context['form'] = form
    return render(request, 'example.html', context= context)