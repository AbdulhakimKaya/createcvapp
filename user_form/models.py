from django.db import models

# Create your models here.


class City(models.Model):
    city_name = models.CharField(max_length=50, null=True, blank=True)
    plate_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.city_name)


class District(models.Model):
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)
    district_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.district_name)


class Gender(models.Model):
    type_gender = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.type_gender)


class MaritalStatus(models.Model):
    status_marital = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.status_marital)


class MilitaryStatus(models.Model):
    status_military = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.status_military)


class DrivingLicense(models.Model):
    type_driving_license = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.type_driving_license)


class WorkExperience(models.Model):
    city_we = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)
    district_we = models.ForeignKey(District, null=True, blank=True, on_delete=models.SET_NULL)
    job_title_we = models.CharField(max_length=255, null=True, blank=True)
    company_name_we = models.CharField(max_length=255, null=True, blank=True)
    description_we = models.TextField(max_length=255, null=True, blank=True)
    start_date_we = models.DateField(null=True, blank=True)
    end_date_we = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.job_title_we)


class Course(models.Model):
    course_name = models.CharField(max_length=255, null=True, blank=True)
    institution_name = models.CharField(max_length=255, null=True, blank=True)
    description_course = models.TextField(max_length=800, null=True, blank=True)
    start_date_course = models.DateField(null=True, blank=True)
    end_date_course = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.course_name)


class Education(models.Model):
    city_education = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)
    district_education = models.ForeignKey(District, null=True, blank=True, on_delete=models.SET_NULL)
    school_name = models.CharField(max_length=255, null=True, blank=True)
    department_name = models.CharField(max_length=255, null=True, blank=True)
    degree_name = models.CharField(max_length=255, null=True, blank=True)
    description_education = models.TextField(max_length=800, null=True, blank=True)
    start_date_education = models.DateField(null=True, blank=True)
    end_date_education = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.school_name)


class Reference(models.Model):
    company_name_reference = models.CharField(max_length=255, null=True, blank=True)
    first_name_reference = models.CharField(max_length=255, null=True, blank=True)
    last_name_reference = models.CharField(max_length=255, null=True, blank=True)
    email_reference = models.CharField(max_length=255, null=True, blank=True)
    phone_number_reference = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return str(self.company_name_reference)


class Experience(models.Model):
    work_experience = models.ForeignKey(WorkExperience, null=True, blank=True, on_delete=models.SET_NULL)
    education = models.ForeignKey(Education, null=True, blank=True, on_delete=models.SET_NULL)
    reference = models.ForeignKey(Reference, null=True, blank=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Experience " + str(self.id)


class LanguageLevel(models.Model):
    level_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.level_name)


class Language(models.Model):
    language_name = models.CharField(max_length=255, null=True, blank=True)
    levels = models.ManyToManyField(LanguageLevel, blank=True)

    def __str__(self):
        return str(self.language_name)


class AbilityLevel(models.Model):
    level_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.level_name)


class Ability(models.Model):
    ability_name = models.CharField(max_length=255, null=True, blank=True)
    levels = models.ManyToManyField(AbilityLevel)

    def __str__(self):
        return str(self.ability_name)


class UserForm(models.Model):
    experience = models.ForeignKey(Experience, null=True, blank=True, on_delete=models.SET_NULL)
    city_living = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)
    district_living = models.ForeignKey(District, null=True, blank=True, on_delete=models.SET_NULL)
    gender = models.ForeignKey(Gender, null=True, blank=True, on_delete=models.SET_NULL)
    marital_status = models.ForeignKey(MaritalStatus, null=True, blank=True, on_delete=models.SET_NULL)
    military_status = models.ForeignKey(MilitaryStatus, null=True, blank=True, on_delete=models.SET_NULL)
    driving_license = models.ForeignKey(DrivingLicense, null=True, blank=True, on_delete=models.SET_NULL)
    languages = models.ManyToManyField(Language, blank=True)
    abilities = models.ManyToManyField(Ability, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    birth_day = models.DateField(null=True, blank=True)
    profile_img = models.ImageField(null=True, blank=True, upload_to='user_profile_images/')
    email = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)
    profile = models.TextField(max_length=800, null=True, blank=True)
    hobby = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.first_name)
