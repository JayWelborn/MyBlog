from django.db.models import FileField
from django.forms import forms
from django.utils.translation import ugettext_lazy as lazy


class AudioFileField(FileField):
    """
    Same as FileField with the following additions:
        * Validates file is of type audio/mpeg3
        * max_upload_size - new KWARG indicating maximum file size.
            2.5MB = 2621440
            5MB   = 5242880
            etc...
    """

    # initiates with properties defining content type and max file size
    def __init__(self, *args, **kwargs):
        self.max_upload_size = kwargs.pop('max_upload_size', 5242880)
        super(AudioFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(AudioFileField, self).clean(*args, **kwargs)
        file = data.file
        if file:
            try:
                file_type = file.content_type
                print (file_type)
                # ensure file is valid type
                if file_type in ['audio/mpeg3',
                                 'audio/mpeg',
                                 'audio/x-mpeg-3',
                                 'audio/mp3',
                                 ]:
                    # ensure file is below maximum size
                    if file._size > self.max_upload_size:
                        raise forms.ValidationError(lazy('File is greater than maximum allowed size'))

                else:
                    raise forms.ValidationError(lazy('File is not an Mp3'))

            except AttributeError:
                pass
        else:
            raise forms.ValidationError(lazy('No File Read'))

        return data
