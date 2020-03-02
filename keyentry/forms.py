from django import forms
from .models import FormHourly, FormDaily2, FormMonthly


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