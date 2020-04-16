from django import forms


class MoveForm(forms.ModelForm):
    class Meta:
        model = Move
        fields = [
            'name',
            'description',
            'creator',            
        ]
        widgets = {
            'description': Textarea(attrs={'cols': 20, 'rows': 40})
        }
