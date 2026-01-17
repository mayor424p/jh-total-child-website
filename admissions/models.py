from django.db import models

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')

)
YES_NO_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

CLASS_CHOICES = (
    ('Nursery', 'Nursery'),
    ('Kindergarten', 'Kindergarten'),
    ('Primary 1', 'Primary 1'),
    ('Primary 2', 'Primary 2'),
    ('Primary 3', 'Primary 3'),
    ('Primary 4', 'Primary 4'),
    ('Primary 5', 'Primary 5'),
    ('Primary 6', 'Primary 6'),
    ('JSS 1', 'JSS 1'),
    ('JSS 2', 'JSS 2'),
    ('JSS 3', 'JSS 3'),
)

STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )


class AdmissionApplication(models.Model):
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    surname = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50)
    preferred_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    religion = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    state_of_origin = models.CharField(max_length=50, blank=True, null=True)
    local_government_area = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField()
    home_phone_number = models.CharField(max_length=15, blank=True, null=True)
    first_language = models.CharField(max_length=50, blank=True, null=True)
    proposed_year_of_entry = models.IntegerField()
    current_school_name = models.TextField(max_length=100, blank=True, null=True)
    current_class = models.CharField(max_length=50,blank=True, null=True, choices=CLASS_CHOICES)

    father_name = models.CharField(max_length=100)
    father_title = models.CharField(max_length=10, blank=True)
    father_profession = models.CharField(max_length=100, blank=True)
    father_employer = models.TextField(blank=True)
    father_phone = models.CharField(max_length=20)
    father_email = models.EmailField(blank=True)
    father_local_govt = models.CharField(max_length=100, blank=True)

    mother_name = models.CharField(max_length=100)
    mother_title = models.CharField(max_length=10, blank=True)
    mother_profession = models.CharField(max_length=100, blank=True)
    mother_employer = models.TextField(blank=True)
    mother_phone = models.CharField(max_length=20)
    mother_email = models.EmailField(blank=True)
    mother_local_govt = models.CharField(max_length=100, blank=True)
    parents_address = models.TextField(blank=True)


    life_threatening_condition = models.CharField(max_length=3, choices=YES_NO_CHOICES, blank=True)
    condition_details = models.TextField(blank=True)
    medication_needed = models.CharField(max_length=3, choices=YES_NO_CHOICES, blank=True)
    medication_details = models.TextField(blank=True)
    other_medical_issues = models.TextField(blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.surname} {self.other_names} "

