from django.shortcuts import render
from .forms import GetJanr
from .models import TableForFormCheck, ValueForJanrInstrumentHarak, JanrInstruments, Janr, InstrumentsHarakter

def get_janr(request):
    if request.method == 'POST':
        if '_add' in request.POST:
            form = GetJanr(request.POST)
            if form.is_valid():
                form.save()
        if '_delete' in request.POST:
            affected_rows = TableForFormCheck.objects.all().delete()
        if '_find' in request.POST:
            input_data = TableForFormCheck.objects.all()
            types = {}
            for input in input_data:
                InstHarak = InstrumentsHarakter.objects.get(instrument_id=input.instrument_id, harakter_id=input.harakter_id)
                data = ValueForJanrInstrumentHarak.objects.filter(value_id=input.value_id, instrument_id_id=InstHarak.id)
                for el in data:
                    el = JanrInstruments.objects.get(pk=el.janr_id_id)
                    el = Janr.objects.get(pk=el.janr_id)
                    if el in types:
                        types[el] += 1
                    else:
                        types[el] = 1
            return render(request, 'answer.html', {'data': types})

    table = TableForFormCheck.objects.all()

    form = GetJanr()
    return render(request, 'base.html', {'form': form, 'table': table})
