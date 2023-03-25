from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms

from .models import Variable


class VariableForm(forms.ModelForm):

    class Meta:
        model = Variable
        fields = ('name_var', 'value_var', 'description', 'string_var',
                  'exp_var', 'money', 'save_value_with_result', 'exp_recursive')

        widgets = {
            'exp_var': forms.Textarea(attrs={'cols': 120, 'rows': 12})
        }

        labels = {
            'name_var': 'Variable',
            'value_var': 'Value',
            'description': 'Description',
            'string_var': 'String Variable',
            'money': 'Money ?',
            'save_value_with_result': 'Save exp. ?',
            'exp_recursive': 'Recursive ?',
            'exp_var': 'Expressions'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name_var', css_class='col-md-5 mb-0'),
                Column('value_var', css_class='col-md-3 mb-0'),
                css_class='form-row col-md-10 col-md-offset-10'
            ),
            Row(
                Column('description', css_class='col-md-12 mb-0'),
                css_class='form-row col-md-10 col-md-offset-10'
            ),
            Row(
                Column('string_var', css_class='col-md-12 mb-0'),
                css_class='form-row col-md-10 col-md-offset-10'
            ),
            Row(
                Column('money', css_class='col-md-2 mb-0'),
                Column('save_value_with_result', css_class='col-md-3 mb-0'),
                Column('exp_recursive', css_class='col-md-3 mb-0'),
                css_class='form-row col-md-10 col-md-offset-10'
            ),
            Row(
                Column('exp_var', css_class='form-group col-md-12 mb-0'),
                css_class='form-row col-md-10 col-md-offset-10'
            ),
            Submit("submit", "Save", css_class='col-2')
        )
