from collections import namedtuple

from django import forms
from .models import FormHourly, FormDaily2, FormMonthly, FormSynoptic2Ra1


ValueFlag = namedtuple('ValueFlag', 'value flag')


class HourlyForm(forms.ModelForm):
    class Meta:
        model = FormHourly
        labels = {
            'id': '',
            'stationid': 'Station:',
            'elementid': 'Element:',
            'yyyy': 'Year:',
            'mm': 'Month:',
            'dd': 'Day:',

            'hh_00': '00',
            'hh_01': '01',
            'hh_02': '02',
            'hh_03': '03',
            'hh_04': '04',
            'hh_05': '05',
            'hh_06': '06',
            'hh_07': '07',
            'hh_08': '08',
            'hh_09': '09',
            'hh_10': '10',
            'hh_11': '11',
            'hh_12': '12',
            'hh_13': '13',
            'hh_14': '14',
            'hh_15': '15',
            'hh_16': '16',
            'hh_17': '17',
            'hh_18': '18',
            'hh_19': '19',
            'hh_20': '20',
            'hh_21': '21',
            'hh_22': '22',
            'hh_23': '23',
            'flag00': '',
            'flag01': '',
            'flag02': '',
            'flag03': '',
            'flag04': '',
            'flag05': '',
            'flag06': '',
            'flag07': '',
            'flag08': '',
            'flag09': '',
            'flag10': '',
            'flag11': '',
            'flag12': '',
            'flag13': '',
            'flag14': '',
            'flag15': '',
            'flag16': '',
            'flag17': '',
            'flag18': '',
            'flag19': '',
            'flag20': '',
            'flag21': '',
            'flag22': '',
            'flag23': '',
            'total': 'Total',
            'signature': '',
            'entrydatetime': '',
        }
        fields = labels.keys()


class Daily2Form(forms.ModelForm):
    class Meta:
        model = FormDaily2
        labels = {
            'id': '',
            'stationid': 'Station:',
            'elementid': 'Element:',
            'yyyy': 'Year:',
            'mm': 'Month:',
            'hh': 'Hour:',
            'day01': '01',
            'day02': '02',
            'day03': '03',
            'day04': '04',
            'day05': '05',
            'day06': '06',
            'day07': '07',
            'day08': '08',
            'day09': '09',
            'day10': '10',
            'day11': '11',
            'day12': '12',
            'day13': '13',
            'day14': '14',
            'day15': '15',
            'day16': '16',
            'day17': '17',
            'day18': '18',
            'day19': '19',
            'day20': '20',
            'day21': '21',
            'day22': '22',
            'day23': '23',
            'day24': '24',
            'day25': '25',
            'day26': '26',
            'day27': '27',
            'day28': '28',
            'day29': '29',
            'day30': '30',
            'day31': '31',
            'flag01': '',
            'flag02': '',
            'flag03': '',
            'flag04': '',
            'flag05': '',
            'flag06': '',
            'flag07': '',
            'flag08': '',
            'flag09': '',
            'flag10': '',
            'flag11': '',
            'flag12': '',
            'flag13': '',
            'flag14': '',
            'flag15': '',
            'flag16': '',
            'flag17': '',
            'flag18': '',
            'flag19': '',
            'flag20': '',
            'flag21': '',
            'flag22': '',
            'flag23': '',
            'flag24': '',
            'flag25': '',
            'flag26': '',
            'flag27': '',
            'flag28': '',
            'flag29': '',
            'flag30': '',
            'flag31': '',
            'period01': '',
            'period02': '',
            'period03': '',
            'period04': '',
            'period05': '',
            'period06': '',
            'period07': '',
            'period08': '',
            'period09': '',
            'period10': '',
            'period11': '',
            'period12': '',
            'period13': '',
            'period14': '',
            'period15': '',
            'period16': '',
            'period17': '',
            'period18': '',
            'period19': '',
            'period20': '',
            'period21': '',
            'period22': '',
            'period23': '',
            'period24': '',
            'period25': '',
            'period26': '',
            'period27': '',
            'period28': '',
            'period29': '',
            'period30': '',
            'period31': '',
            'total': 'Total',
            'signature': '',
            'entrydatetime': '',
            'temperatureunits': 'Temperature:',
            'precipunits': 'Precip:',
            'cloudheightunits': 'Cloud height:',
            'visunits': 'Visibility:',
        }
        fields = labels.keys()


class MonthlyForm(forms.ModelForm):
    class Meta:
        model = FormMonthly
        labels = {
            'id': '',
            'stationid': 'Station:',
            'elementid': 'Element:',
            'yyyy': 'Year:',
            'mm_01': 'January',
            'mm_02': 'February',
            'mm_03': 'March',
            'mm_04': 'April',
            'mm_05': 'May',
            'mm_06': 'June',
            'mm_07': 'July',
            'mm_08': 'August',
            'mm_09': 'September',
            'mm_10': 'October',
            'mm_11': 'November',
            'mm_12': 'December',
            'flag01': '',
            'flag02': '',
            'flag03': '',
            'flag04': '',
            'flag05': '',
            'flag06': '',
            'flag07': '',
            'flag08': '',
            'flag09': '',
            'flag10': '',
            'flag11': '',
            'flag12': '',
            'period01': '',
            'period02': '',
            'period03': '',
            'period04': '',
            'period05': '',
            'period06': '',
            'period07': '',
            'period08': '',
            'period09': '',
            'period10': '',
            'period11': '',
            'period12': '',
            'signature': '',
            'entrydatetime': '',
        }
        fields = labels.keys()


class Synoptic2Ra1Form(forms.ModelForm):
    COLUMNS = (
        ('106', '107', '400', '814', '399', '301', '185', '101', '102', '103', '105', '110', '192', '114', '115', '168', '169', '170', '171',),
        ('119', '116', '117', '118', '123', '120', '121', '122', '127', '124', '125', '126', '131', '128', '129', '130',),
        ('167', '197', '193', '002', '003', '099', '018', '084', '132', '005', '174', '112', '111',),
    )

    class Meta:
        model = FormSynoptic2Ra1
        labels = {
            'id': '',

            'stationid': 'Station:',
            'yyyy': 'Year:',
            'mm': 'Month:',
            'dd': 'Day:',
            'hh': 'Hour:',

            'val_elem106': 'Station Level Pressure-Po',  # Pressure  Station
            'val_elem107': 'Pressure Reduced to MSL-P',  # Pressure  Sea Level
            'val_elem400': '3hr Pessure Change-P3',  # 3 Hr Pressure Change
            'val_elem814': '3hr Pressure Characteristic',  # 3Hr Pressure Characteristic
            'val_elem399': '24hr Pessure Change-P24',  # Press Tendancy  24 Hly
            'val_elem301': 'Standard Pressure Level -a',  # Pressure Level
            'val_elem185': 'Geopotential Height-hhh',  # Pressure  GPM
            'val_elem101': 'DryBulb Temp-TTT',  # Temp  Dry Bulb
            'val_elem102': 'Wetbulb Temp-TwTwTw',  # Temp  Wet Bulb
            'val_elem103': 'DewPoint Temp-TdTdTd',  # Temp  Dew Point
            'val_elem105': 'Relative Humidity-U',  # Relative Humidty 06Z
            'val_elem110': 'Horizontal Visibility-VV',  # Visibility Hor
            'val_elem192': 'Low Cloud Hght-h',  # Cloud Height Lowest Lvl
            'val_elem114': 'Total Cloud Cover- N',  # Cloud Cover  total
            'val_elem115': 'Vertical Significance',  # Cloud Opacty tot
            'val_elem168': 'Low Lvl Clouds Amount-Nh',  # Cloud Amt Type Height Lvl1
            'val_elem169': 'Low Lvl Clouds Type-CL',  # Cloud Amt Type Height Lvl2
            'val_elem170': 'Medium Lvl Clouds Type-CM',  # Cloud Amt Type Height Lvl3
            'val_elem171': 'High Lvl Clouds Type-CH',  # Cloud Amt Type Height Lvl4

            'val_elem119': 'Vertical Significance 1',  # Cloud Opacity  Lvl1
            'val_elem116': 'Cloud Amt Lvl1-N1',  # Cloud Amt  Lvl 1
            'val_elem117': 'Cloud Type Lvl1-C1',  # Cloud Type  Low
            'val_elem118': 'Cloud Ht Lvl1-HsHs1',  # Cloud Height  Lvl 1
            'val_elem123': 'Vertical Significance 2',  # Cloud Opacity  lvl2
            'val_elem120': 'Cloud Amt Lvl2-N2',  # Cloud Amt  Lvl 2
            'val_elem121': 'Cloud Type Lv2-C2',  # Cloud Type  Lvl 2
            'val_elem122': 'Cloud Ht Lvl2-HsHs2',  # Cloud Height  Lvl 2
            'val_elem127': 'Vertical Significant 3',  # Cloud Opacity  Lvl3
            'val_elem124': 'Cloud Amt Lvl3-N3',  # Cloud Amt  Lvl 3
            'val_elem125': 'Cloud Type Lvl3-C3',  # Cloud Type  Lvl 3
            'val_elem126': 'Cloud Ht Lvl3-HsHs3',  # Cloud Height  Lvl 3
            'val_elem131': 'Vertical Significance 4',  # Cloud Opacity  Lvl4
            'val_elem128': 'Cloud Amt Lvl4-N4',  # Cloud Amt  Lvl 4
            'val_elem129': 'Cloud Type Lvl4-C4',  # Cloud Type  Lvl 4
            'val_elem130': 'Cloud Ht Lvl4-Hshs4',  # Cloud Height  Lvl 4

            'val_elem167': 'PresentWx',  # Present Weather
            'val_elem197': 'PastWx1',  # Visibility Max
            'val_elem193': 'PastWx2',  # Cloud  Medium Lvl  Type
            'val_elem002': 'Tmax',  # Temp  Daily Max
            'val_elem003': 'Tmin',  # Temp  Daily Min
            'val_elem099': 'Grass Min Temp',  # Wind Totalizer  06Z
            'val_elem018': 'Evaporation',  # Evap  Pan1 Daily
            'val_elem084': 'SSS-24Hr',  # Sunshine  Daily Tot
            'val_elem132': 'SSS-1Hr',  # Sunshine Hly Tot
            'val_elem005': 'Precip-24Hr',  # Precip  Daily
            'val_elem174': 'Precip-3Hr',  # Precip  Tot 3 Hours
            'val_elem112': 'Wind Direction-dd',  # Wind Direction
            'val_elem111': 'Wind Speed - fff',  # Wind Speed in Knots
            'val_elem046': 'Insolation - Rad',  # Insolation Daily

            'flag106': '',
            'flag107': '',
            'flag400': '',
            'flag814': '',
            'flag399': '',
            'flag301': '',
            'flag185': '',
            'flag101': '',
            'flag102': '',
            'flag103': '',
            'flag105': '',
            'flag192': '',
            'flag110': '',
            'flag114': '',
            'flag112': '',
            'flag111': '',
            'flag167': '',
            'flag197': '',
            'flag193': '',
            'flag115': '',
            'flag168': '',
            'flag169': '',
            'flag170': '',
            'flag171': '',
            'flag119': '',
            'flag116': '',
            'flag117': '',
            'flag118': '',
            'flag123': '',
            'flag120': '',
            'flag121': '',
            'flag122': '',
            'flag127': '',
            'flag124': '',
            'flag125': '',
            'flag126': '',
            'flag131': '',
            'flag128': '',
            'flag129': '',
            'flag130': '',
            'flag002': '',
            'flag003': '',
            'flag099': '',
            'flag018': '',
            'flag084': '',
            'flag132': '',
            'flag005': '',
            'flag174': '',
            'flag046': '',
        }
        fields = labels.keys()

    def columns(self):
        return [
            [ValueFlag(self['val_elem{}'.format(field_num)], self['flag{}'.format(field_num)]) for field_num in column]
            for column in self.COLUMNS
        ]
