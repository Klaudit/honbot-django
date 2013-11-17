from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import PlayerStats
from django.shortcuts import render_to_response

def browse(request):
    return render_to_response('player_browse.html', {})

class PlayerList(BaseDatatableView):
    # The model we're going to show
    model = PlayerStats

    # define the columns that will be returned
    columns = ['nickname', 'mmr', 'TSR', 'wins', 'losses', 'kills', 'deaths', 'kdr', 'aactionsmin', 'agoldmin', 'axpmin', 'hours', 'ks15', 'updated']

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = columns

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 100

    def get_initial_queryset(self):
        # return queryset used as base for futher sorting/filtering
        # these are simply objects displayed in datatable
        # You should not filter data returned here by any filter values entered by user. This is because
        # we need some base queryset to count total number of records.
        return PlayerStats.objects.all()

    def filter_queryset(self, qs):
        # use request parameters to filter queryset

        # simple example:
        sSearch = self.request.GET.get('sSearch', None)
        if sSearch:
            qs = qs.filter(nickname__istartswith=sSearch)
        return qs

    def prepare_results(self, qs):
        # prepare list with output column data
        # queryset is already paginated here
        json_data = []
        for item in qs:
            json_data.append([
                item.nickname,
                item.mmr,
                item.TSR,
                item.wins,
                item.losses,
                item.kills,
                item.deaths,
                item.kdr,
                item.aactionsmin,
                item.agoldmin,
                item.axpmin,
                item.hours,
                item.ks15,
                item.updated,
            ])
        return json_data