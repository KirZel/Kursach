from django.db import models

class Janr(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name 

class Instrument(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'инструмент'
        verbose_name_plural = 'Инструменты'

    def __str__(self):
        return self.name 

class HarakterName(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'название характеристики'
        verbose_name_plural = 'Название Характеристик'

    def __str__(self):
        return self.name 

class JanrInstruments(models.Model):
    janr = models.ForeignKey(Janr, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'инструмент для жанра'
        verbose_name_plural = 'Инструменты для жанра'

    def __str__(self):
        return f'{self.janr.name} - {self.instrument.name}'

class InstrumentsHarakter(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    harakter = models.ForeignKey(HarakterName, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'характеристика для инструмента'
        verbose_name_plural = 'Характеристики для инструмента'

    def __str__(self):
        return f'{self.instrument.name} - {self.harakter.name}'

class PossibleValuesForHarak(models.Model):
    harakter = models.ForeignKey(HarakterName, on_delete=models.CASCADE)
    value = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'значения для характеристики'
        verbose_name_plural = 'Значения для характеристик'

    def __str__(self):
        return f'{self.harakter.name} - {self.value}'
    

class ValueForJanrInstrumentHarak(models.Model):
    janr_id = models.ForeignKey(JanrInstruments, on_delete=models.CASCADE)
    instrument_id = models.ForeignKey(InstrumentsHarakter, on_delete=models.CASCADE)
    value_id = models.ForeignKey(PossibleValuesForHarak, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('janr_id', 'instrument_id', 'value_id'),)
        verbose_name = 'значение характеристики для жанра'
        verbose_name_plural = 'Значения характеристик для жанра'

    def __str__(self):
        return f'{self.janr_id} - {self.instrument_id} - {self.value_id}'


class TableForFormCheck(models.Model):
    instrument_id = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    harakter = models.ForeignKey(HarakterName, on_delete=models.CASCADE)
    value_id = models.ForeignKey(PossibleValuesForHarak, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('harakter', 'instrument_id', 'value_id'),)

    def __str__(self):
        return f'{self.instrument_id} - {self.harakter} - {self.value_id}'