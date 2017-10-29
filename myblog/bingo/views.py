import random

from django.views import generic
from django.utils import timezone

from .models import BingoCard, BingoBlock, FreeSpace

# List of All Bingo Cards
class IndexView(generic.ListView):
    template_name = 'bingo/index.html'
    context_object_name = 'bingo_cards'

    def get_queryset(self):
        """
        return bingo cards ordered by publication date
        """
        bingo_cards = BingoCard.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pubdate')
        return bingo_cards

# Dispaly One Card in Detail
class DetailView(generic.DetailView):
    template_name = 'bingo/detail.html'
    model = BingoCard
    context_object_name = 'card'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        # get the blocks associated with the Card instance
        block_set = self.object.blocks.all()
        # randomizes order of blocks each time the page loads
        context['blocks'] = random.sample(list(block_set), 24)
        # makes the free space always in the center
        context['blocks'].insert(12, self.object.free_space)
        return context
