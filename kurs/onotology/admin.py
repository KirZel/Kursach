from django.contrib import admin

# Register your models here.
from .models import Janr, Instrument, HarakterName, JanrInstruments, InstrumentsHarakter, PossibleValuesForHarak, ValueForJanrInstrumentHarak, TableForFormCheck

admin.site.register(Janr)
admin.site.register(Instrument)
admin.site.register(HarakterName)
admin.site.register(JanrInstruments)
admin.site.register(InstrumentsHarakter)
admin.site.register(PossibleValuesForHarak)
admin.site.register(ValueForJanrInstrumentHarak)
admin.site.register(TableForFormCheck)