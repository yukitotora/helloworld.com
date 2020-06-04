from django import forms
import datetime

class ContactForm(forms.Form):
    CATEGORIES = (
        ('1', 'お仕事の依頼'),
        ('2', 'サイト内容に関するお問い合わせ'),
    )

    name = forms.CharField(
        label='お名前', max_length=50,
        required=False, help_text='※任意'
    )
    email = forms.EmailField(
        label='メールアドレス', required=False, help_text='※任意'
    )
    text = forms.CharField(label='問い合わせ内容', widget=forms.Textarea)
    category = forms.ChoiceField(label='カテゴリ', choices=CATEGORIES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

    # years = [x for x in range(1990, 2031)]
    # months = {
    #     1:'睦月', 2:'如月', 3:'弥生', 4:'卯月',
    #     5:'皐月', 6:'水無月', 7:'文月', 8:'葉月',
    #     9:'長月', 10:'神無月', 11:'霜月', 12:'師走'
    # }
    # created_at = forms.DateField(label='日時', widget=forms.SelectDateWidget(years=years, months=months))

    # HOURS = [(datetime.time(hour=hour),'{}時'.format(hour)) for hour in range(0,24)]
    # created_at = forms.TimeField(label='日時',widget=forms.Select(choices=HOURS))
