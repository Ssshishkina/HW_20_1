from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    '''Класс стилизации формы'''
    def init(self, *args, **kwargs):
        '''Функция стилизации формы'''
        super().init(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                       'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        '''Функция валидации поля 'name' на недопустимые
        слова из списка forbidden_words.'''
        cleaned_name = self.cleaned_data['name']
        if cleaned_name.lower() in self.forbidden_words:
            raise forms.ValidationError('Ошибка, использовано недопустимое слово в названии!')
        return cleaned_name

    def clean_description(self):
        '''Функция валидации поля 'description'
        на недопустимые слова из списка forbidden_words.'''
        cleaned_data = self.cleaned_data['description']
        if cleaned_data.lower() in self.forbidden_words:
            raise forms.ValidationError('Ошибка, использовано недопустимое слово в описании!')
        return cleaned_data

    #def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'form-control'


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('name', 'number',)
