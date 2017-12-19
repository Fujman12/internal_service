from django.db import models


class IdentifierType(models.Model):
    name = models.CharField(u'Domain name', max_length=255)
    description = models.TextField(u'Description')

    class Meta:
        verbose_name = u'Identifier Type'
        verbose_name_plural = u'Identifier Types'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Watchlist(models.Model):
    name = models.CharField(u'Watchlist', max_length=255)

    class Meta:
        verbose_name = u'Watch list'
        verbose_name_plural = u'Watch lists'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Classification(models.Model):
    name = models.CharField(u'Classification', max_length=255)

    class Meta:
        verbose_name = u'Classification'
        verbose_name_plural = u'Classifications'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class WatchlistItem(models.Model):
    identifier_type = models.ForeignKey(IdentifierType, related_name='related_identifier_type', on_delete=models.CASCADE)
    watch_list = models.ForeignKey(Watchlist, related_name='related_watch_list', on_delete=models.CASCADE)
    classification = models.ForeignKey(Classification, related_name='related_classification', on_delete=models.CASCADE)
    silent = models.BooleanField(u'Silent')
    identifier_value = models.CharField(u'Identifier Value', max_length=255)

    class Meta:
        verbose_name = u'Watch list Item'
        verbose_name_plural = u'Watch list Items'
        ordering = ('-id',)

    def __str__(self):
        return self.identifier_type
