from django.db import models

# Create your models here.
YEAR = (
        ('2023', '2023'),
        ('2022', '2022'),
    )
BRANCH = (
        ('ECE', 'ECE'),
        ('CSE(select-for-similar-brances-like-csm-Ai-IT)', 'CSE(select-for-similar-brances-like-csm-Ai-IT)'),
        ('MECH','MECH'),
        ('CIVIL','CIVIL'),
        ('CHEM','CHEM'),
        ('EEE','EEE'),
    )
PACKAGE = (
    ('2.5-4.5','2.5-4.5'),
    ('4.5-6','4.5-6'),
    ('6-9','6-9'),
    ('9-12','9-12'),
    ('12-18','12-18'),
    ('18-24','18-24'),
    ('more','more')
)
PLACEDON={
    ('core','core'),
    ('IT(software)','IT(software)')
}
class Details(models.Model):
    year = models.CharField(max_length=50, choices=YEAR )
    branch = models.CharField(max_length=50, choices=BRANCH)
    placed = models.BooleanField(default=False)
    placed_on = models.CharField(max_length=50,choices=PLACEDON,blank=True)
    package = models.CharField(max_length=50, choices=PACKAGE, blank=True)
    

