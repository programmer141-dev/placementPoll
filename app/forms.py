from django import forms
from .models import Details

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('year', 'branch', 'placed', 'placed_on', 'package')

    def __init__(self, *args, **kwargs):
        super(DetailsForm, self).__init__(*args, **kwargs)
        # Add custom labels for fields
        self.fields['year'].label = 'Year of Passing'
        self.fields['branch'].label = 'Branch of Study'
        self.fields['placed'].label = 'Placed in Campus Recruitment?'
        self.fields['placed_on'].label = 'Name of Company Placed With'
        self.fields['package'].label = 'Placement Package (in Lakhs per Annum)'

        # Add custom help text for fields
        self.fields['placed'].help_text = 'Select "Yes" if you were placed in a campus recruitment drive.'
        self.fields['placed_on'].help_text = 'Enter the name of the company you were placed with, if applicable.'
        self.fields['package'].help_text = 'Enter the package you were offered in lakhs per annum, if applicable.'
