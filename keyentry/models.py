"""
The models below were originally created by Django's `inspectdb`
by inspecting the original Climsoft 4 database.

However, the original tables did not have a single-column primary
key therefore `inspectdb` incorrectly set `stationid` as the primary
key in each case, and represented the rest of the composite key
using `unique_together`.

This would fail when duplicates station id's were entered,
therefore an additional AutoField called `id` as been added to
each.

`primary_key` has been removed from each `stationid` and
`managed` has been changed from False to True.

We've retained separated `yyyy`, `mm` and `dd` fields to manage
required date parts and partial dates in the same way as the desktop
software.

In form_daily2 there are fields for temperature, precipitation,
cloud height and visibility units. We've just retained these for now
and added the valid and default choices to the fields.

Text fields in the original database were permitted to be NULL (in
addition to just empty "" by default) therefore the CharField fields
below currently have `null=True` created by `inspectdb`.

"""
from django.db import models


# Defaults
DEG_C = 'Deg C'
MM = 'mm'
FEET = 'feet'
METRES = 'metres'


# Units choices
TEMP = [(DEG_C, 'Deg C'), ('Deg F', 'Deg F')]
PRECIP = [(MM, 'mm'), ('inches', 'inches')]
CLOUD = [(FEET, 'feet'), ('metres', 'metres')]
VIS = [(METRES, 'metres'),('yards', 'yards')]

# Flags choices:
# M (Missing), the data value is missing;
# T (Trace), the data value has been recorded as zero but a small trace was observed;
# E (Estimated), the data value is an estimated value rather than an observed value.
# G (Generated), the data has been generated from other values.
# D (Dubious), Dubious or suspect value (data).
FLAGS = [('', ''), ('M', 'M'), ('T', 'T'), ('E', 'E'), ('G', 'G'), ('D', 'D')]


class FormHourly(models.Model):
    id = models.AutoField(primary_key=True)
    stationid = models.CharField(db_column='stationId', max_length=50)  # Field name made lowercase.
    elementid = models.IntegerField(db_column='elementId')  # Field name made lowercase.
    yyyy = models.IntegerField()
    mm = models.IntegerField()
    dd = models.IntegerField()

    hh_00 = models.CharField(max_length=50, blank=True, null=True)
    hh_01 = models.CharField(max_length=50, blank=True, null=True)
    hh_02 = models.CharField(max_length=50, blank=True, null=True)
    hh_03 = models.CharField(max_length=50, blank=True, null=True)
    hh_04 = models.CharField(max_length=50, blank=True, null=True)
    hh_05 = models.CharField(max_length=50, blank=True, null=True)
    hh_06 = models.CharField(max_length=50, blank=True, null=True)
    hh_07 = models.CharField(max_length=50, blank=True, null=True)
    hh_08 = models.CharField(max_length=50, blank=True, null=True)
    hh_09 = models.CharField(max_length=50, blank=True, null=True)
    hh_10 = models.CharField(max_length=50, blank=True, null=True)
    hh_11 = models.CharField(max_length=50, blank=True, null=True)
    hh_12 = models.CharField(max_length=50, blank=True, null=True)
    hh_13 = models.CharField(max_length=50, blank=True, null=True)
    hh_14 = models.CharField(max_length=50, blank=True, null=True)
    hh_15 = models.CharField(max_length=50, blank=True, null=True)
    hh_16 = models.CharField(max_length=50, blank=True, null=True)
    hh_17 = models.CharField(max_length=50, blank=True, null=True)
    hh_18 = models.CharField(max_length=50, blank=True, null=True)
    hh_19 = models.CharField(max_length=50, blank=True, null=True)
    hh_20 = models.CharField(max_length=50, blank=True, null=True)
    hh_21 = models.CharField(max_length=50, blank=True, null=True)
    hh_22 = models.CharField(max_length=50, blank=True, null=True)
    hh_23 = models.CharField(max_length=50, blank=True, null=True)
    flag00 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag01 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag02 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag03 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag04 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag05 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag06 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag07 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag08 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag09 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag10 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag11 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag12 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag13 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag14 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag15 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag16 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag17 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag18 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag19 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag20 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag21 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag22 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    flag23 = models.CharField(max_length=50, blank=True, null=True, choices=FLAGS)
    total = models.CharField(max_length=50, blank=True, null=True)
    signature = models.CharField(max_length=50, blank=True, null=True)
    entrydatetime = models.DateTimeField(db_column='entryDatetime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'form_hourly'
        unique_together = (('stationid', 'elementid', 'yyyy', 'mm', 'dd'),)


class FormDaily2(models.Model):
    id = models.AutoField(primary_key=True)
    stationid = models.CharField(db_column='stationId', max_length=50)  # Field name made lowercase.
    elementid = models.IntegerField(db_column='elementId')  # Field name made lowercase.
    yyyy = models.IntegerField()
    mm = models.IntegerField()
    hh = models.IntegerField()
    day01 = models.CharField(max_length=45, blank=True, null=True)
    day02 = models.CharField(max_length=45, blank=True, null=True)
    day03 = models.CharField(max_length=45, blank=True, null=True)
    day04 = models.CharField(max_length=45, blank=True, null=True)
    day05 = models.CharField(max_length=45, blank=True, null=True)
    day06 = models.CharField(max_length=45, blank=True, null=True)
    day07 = models.CharField(max_length=45, blank=True, null=True)
    day08 = models.CharField(max_length=45, blank=True, null=True)
    day09 = models.CharField(max_length=45, blank=True, null=True)
    day10 = models.CharField(max_length=45, blank=True, null=True)
    day11 = models.CharField(max_length=45, blank=True, null=True)
    day12 = models.CharField(max_length=45, blank=True, null=True)
    day13 = models.CharField(max_length=45, blank=True, null=True)
    day14 = models.CharField(max_length=45, blank=True, null=True)
    day15 = models.CharField(max_length=45, blank=True, null=True)
    day16 = models.CharField(max_length=45, blank=True, null=True)
    day17 = models.CharField(max_length=45, blank=True, null=True)
    day18 = models.CharField(max_length=45, blank=True, null=True)
    day19 = models.CharField(max_length=45, blank=True, null=True)
    day20 = models.CharField(max_length=45, blank=True, null=True)
    day21 = models.CharField(max_length=45, blank=True, null=True)
    day22 = models.CharField(max_length=45, blank=True, null=True)
    day23 = models.CharField(max_length=45, blank=True, null=True)
    day24 = models.CharField(max_length=45, blank=True, null=True)
    day25 = models.CharField(max_length=45, blank=True, null=True)
    day26 = models.CharField(max_length=45, blank=True, null=True)
    day27 = models.CharField(max_length=45, blank=True, null=True)
    day28 = models.CharField(max_length=45, blank=True, null=True)
    day29 = models.CharField(max_length=45, blank=True, null=True)
    day30 = models.CharField(max_length=45, blank=True, null=True)
    day31 = models.CharField(max_length=45, blank=True, null=True)
    flag01 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag02 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag03 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag04 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag05 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag06 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag07 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag08 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag09 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag10 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag11 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag12 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag13 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag14 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag15 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag16 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag17 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag18 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag19 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag20 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag21 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag22 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag23 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag24 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag25 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag26 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag27 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag28 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag29 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag30 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    flag31 = models.CharField(max_length=1, blank=True, null=True, choices=FLAGS)
    period01 = models.CharField(max_length=45, blank=True, null=True)
    period02 = models.CharField(max_length=45, blank=True, null=True)
    period03 = models.CharField(max_length=45, blank=True, null=True)
    period04 = models.CharField(max_length=45, blank=True, null=True)
    period05 = models.CharField(max_length=45, blank=True, null=True)
    period06 = models.CharField(max_length=45, blank=True, null=True)
    period07 = models.CharField(max_length=45, blank=True, null=True)
    period08 = models.CharField(max_length=45, blank=True, null=True)
    period09 = models.CharField(max_length=45, blank=True, null=True)
    period10 = models.CharField(max_length=45, blank=True, null=True)
    period11 = models.CharField(max_length=45, blank=True, null=True)
    period12 = models.CharField(max_length=45, blank=True, null=True)
    period13 = models.CharField(max_length=45, blank=True, null=True)
    period14 = models.CharField(max_length=45, blank=True, null=True)
    period15 = models.CharField(max_length=45, blank=True, null=True)
    period16 = models.CharField(max_length=45, blank=True, null=True)
    period17 = models.CharField(max_length=45, blank=True, null=True)
    period18 = models.CharField(max_length=45, blank=True, null=True)
    period19 = models.CharField(max_length=45, blank=True, null=True)
    period20 = models.CharField(max_length=45, blank=True, null=True)
    period21 = models.CharField(max_length=45, blank=True, null=True)
    period22 = models.CharField(max_length=45, blank=True, null=True)
    period23 = models.CharField(max_length=45, blank=True, null=True)
    period24 = models.CharField(max_length=45, blank=True, null=True)
    period25 = models.CharField(max_length=45, blank=True, null=True)
    period26 = models.CharField(max_length=45, blank=True, null=True)
    period27 = models.CharField(max_length=45, blank=True, null=True)
    period28 = models.CharField(max_length=45, blank=True, null=True)
    period29 = models.CharField(max_length=45, blank=True, null=True)
    period30 = models.CharField(max_length=45, blank=True, null=True)
    period31 = models.CharField(max_length=45, blank=True, null=True)
    total = models.CharField(max_length=45, blank=True, null=True)
    signature = models.CharField(max_length=45, blank=True, null=True)
    entrydatetime = models.DateTimeField(db_column='entryDatetime', blank=True, null=True)  # Field name made lowercase.
    temperatureunits = models.CharField(db_column='temperatureUnits', max_length=45, blank=True, null=True,
                                        choices=TEMP, default=DEG_C)  # Field name made lowercase.
    precipunits = models.CharField(db_column='precipUnits', max_length=45, blank=True, null=True,
                                   choices=PRECIP, default=MM)  # Field name made lowercase.
    cloudheightunits = models.CharField(db_column='cloudHeightUnits', max_length=45, blank=True, null=True,
                                        choices=CLOUD, default=FEET)  # Field name made lowercase.
    visunits = models.CharField(db_column='visUnits', max_length=45, blank=True, null=True,
                                choices=VIS, default=METRES)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'form_daily2'
        unique_together = (('stationid', 'elementid', 'yyyy', 'mm', 'hh'),)


class FormMonthly(models.Model):
    id = models.AutoField(primary_key=True)
    stationid = models.CharField(db_column='stationId', max_length=255)  # Field name made lowercase.
    elementid = models.IntegerField(db_column='elementId')  # Field name made lowercase.
    yyyy = models.IntegerField()
    mm_01 = models.CharField(max_length=255, blank=True, null=True)
    mm_02 = models.CharField(max_length=255, blank=True, null=True)
    mm_03 = models.CharField(max_length=255, blank=True, null=True)
    mm_04 = models.CharField(max_length=255)
    mm_05 = models.CharField(max_length=255, blank=True, null=True)
    mm_06 = models.CharField(max_length=255, blank=True, null=True)
    mm_07 = models.CharField(max_length=255, blank=True, null=True)
    mm_08 = models.CharField(max_length=255, blank=True, null=True)
    mm_09 = models.CharField(max_length=255, blank=True, null=True)
    mm_10 = models.CharField(max_length=255, blank=True, null=True)
    mm_11 = models.CharField(max_length=255, blank=True, null=True)
    mm_12 = models.CharField(max_length=255, blank=True, null=True)
    flag01 = models.CharField(max_length=255, blank=True, null=True, choices=FLAGS)
    flag02 = models.CharField(max_length=255, blank=True, null=True, choices=FLAGS)
    flag03 = models.CharField(max_length=255, blank=True, null=True, choices=FLAGS)
    flag04 = models.CharField(max_length=255, blank=True, null=True, choices=FLAGS)
    flag05 = models.CharField(max_length=255, blank=True, null=True, choices=FLAGS)
    flag06 = models.CharField(max_length=255, blank=True, null=True, choices=FLAGS)
    flag07 = models.CharField(max_length=255, blank=True, null=True, choices=FLAGS)
    flag08 = models.CharField(max_length=255, blank=True, null=True, choices=FLAGS)
    flag09 = models.CharField(max_length=255, blank=True, null=True, choices=FLAGS)
    flag10 = models.CharField(max_length=255, blank=True, null=True, choices=FLAGS)
    flag11 = models.CharField(max_length=255, blank=True, null=True, choices=FLAGS)
    flag12 = models.CharField(max_length=255, blank=True, null=True, choices=FLAGS)
    period01 = models.CharField(max_length=255, blank=True, null=True)
    period02 = models.CharField(max_length=255, blank=True, null=True)
    period03 = models.CharField(max_length=255, blank=True, null=True)
    period04 = models.CharField(max_length=255, blank=True, null=True)
    period05 = models.CharField(max_length=255, blank=True, null=True)
    period06 = models.CharField(max_length=255, blank=True, null=True)
    period07 = models.CharField(max_length=255, blank=True, null=True)
    period08 = models.CharField(max_length=255, blank=True, null=True)
    period09 = models.CharField(max_length=255, blank=True, null=True)
    period10 = models.CharField(max_length=255, blank=True, null=True)
    period11 = models.CharField(max_length=255, blank=True, null=True)
    period12 = models.CharField(max_length=255, blank=True, null=True)
    signature = models.CharField(max_length=50, blank=True, null=True)
    entrydatetime = models.DateTimeField(db_column='entryDatetime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'form_monthly'
        unique_together = (('stationid', 'elementid', 'yyyy'),)
