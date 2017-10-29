from django.db import models
from django.utils import timezone
from django.urls import reverse

from .fields import AudioFileField

# BingoCard is a class containing the title of the card to be displayed
class BingoCard(models.Model):
    
    class Meta:
        verbose_name = 'Bingo Card'
        verbose_name_plural = 'Bingo Cards'

    title = models.CharField(max_length=140, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    pub_date = models.DateField(default=timezone.now)
    header_image = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)
    victory_song = AudioFileField(upload_to='media/audio/%Y/%m/%d', max_upload_size=5242880, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Defeines PK and Slug as URL components
        """
        args = (self.pk, self.slug)
        return reverse(self, args)



# BingoBlock is a class containing a text field for what the bingo block should say
class BingoBlock (models.Model):

    class Meta:
        verbose_name = 'Bingo Block'
        verbose_name_plural = 'Bingo Blocks'

    block_text = models.CharField(max_length=40)
    card = models.ForeignKey(BingoCard,
                             on_delete=models.CASCADE,
                             related_name='blocks')

    def __str__(self):
        return self.block_text

# FreeSpace is displayed at the center of the bingo card
class FreeSpace(models.Model):
    
    class Meta:
        verbose_name = 'Free Space'

    card = models.OneToOneField(BingoCard, 
                                on_delete=models.CASCADE,
                                related_name='free_space')
    freespace_text = models.CharField(max_length=40)

    def __str__(self):
        return self.freespace_text
        