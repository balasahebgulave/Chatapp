from django import forms
from . models import IssueDetails

class IssueDetailsForm(forms.ModelForm):
	class Meta:
		model = IssueDetails
		fields = "__all__"


		