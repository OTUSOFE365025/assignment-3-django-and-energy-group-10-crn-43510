from django import forms

class ScanForm(forms.Form):
    upc = forms.CharField(
        label="Enter or Scan UPC",
        max_length=32,
        widget=forms.TextInput(attrs={
            "placeholder": "e.g., 123456789012",
            "style": "padding:8px; width:250px;"
        })
    )
