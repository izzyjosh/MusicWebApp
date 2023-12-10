from django import forms
from .models import Music


class AddMusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ["title","musician","image","music_file"]
        widgets = {
                'title': forms.TextInput(attrs={
                    "name":"title",
                    "placeholder":"Title",
                    "type":"text",
                    "class":"form-control my-2",
                    }),

                'musician': forms.TextInput(attrs={
                    "name":"musician",
                    "placeholder":"Musician",
                    "type":"text",
                    "class":"form-control my-2",
                    }),
                }


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields["image"].widget = forms.FileInput(attrs={
            "name":"image",
            "type":"file",
            "class":"form-control my-2"
            })

        self.fields["music_file"].widget = forms.FileInput(attrs={
            "name":"musicfile",
            "type":"file",
            "class":"form-control my-2"
            })
