import random
import time
import datetime
import lorem
import csv


blank_dict = {
    'Year' : '',
    'Month' : '',
    'Day' : '',
    'Time' : '',
    'End Year' : '',
    'End Month' : '',
    'End Day' : '',
    'End Time' : '',
    'Display Date' : '',
    'Headline' : '',
    'Text' : '',
    'Media' : '',
    'Media Credit' : '',
    'Media Caption' : '',
    'Media Thumbnail' : '',
    'Type' : '',
    'Group' : '',
    'Background' : ''
}


def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDay(start, end, prop):
    return strTimeProp(start, end, '%Y|%m|%d', prop)

with open('500_sample.csv', 'w') as f:
    w = csv.DictWriter(f, blank_dict.keys())
    w.writeheader()
    

    for x in range(1,500):

        year,month,day = randomDay("1980|1|1", "2018|12|30", random.random()).split('|')
        year = int(year)
        month = int(month)
        day = int(day)

        line = blank_dict.copy()

        line['Headline'] = lorem.sentence()
        line['Text'] = lorem.paragraph()

        if x < 400:
            size = x + 500
        else:
            size = x
        
        line['Media'] = f'https://picsum.photos/{size}/?random'
        line['Media Caption'] = lorem.sentence()


        # just do some years
        if x < 100:
            line['Year'] = year

            line['Display Date'] = year

        elif x < 450:
            line['Year'] = year
            line['Month'] = month

            line['Display Date'] = f"{datetime.date(year, month, 1).strftime('%B')} {year}"
        else:
            line['Year'] = year
            line['Month'] = month
            line['Day'] = day

            line['Display Date'] = f"{datetime.date(year, month, 1).strftime('%B')} {day} {year}"
           

        w.writerow(line)



with open('500_groups_sample.csv', 'w') as f:
    w = csv.DictWriter(f, blank_dict.keys())
    w.writeheader()
    

    for x in range(1,500):

        year,month,day = randomDay("1980|1|1", "2018|12|30", random.random()).split('|')
        year = int(year)
        month = int(month)
        day = int(day)

        line = blank_dict.copy()

        line['Headline'] = lorem.sentence()
        line['Text'] = lorem.paragraph()

        if x < 400:
            size = x + 500
        else:
            size = x
        
        line['Media'] = f'https://picsum.photos/{size}/?random'
        line['Media Caption'] = lorem.sentence()

        line['Group'] = f"Group {random.randint(1, 5)}"

        # just do some years
        if x < 100:
            line['Year'] = year

            line['Display Date'] = year

        elif x < 450:
            line['Year'] = year
            line['Month'] = month

            line['Display Date'] = f"{datetime.date(year, month, 1).strftime('%B')} {year}"
        else:
            line['Year'] = year
            line['Month'] = month
            line['Day'] = day

            line['Display Date'] = f"{datetime.date(year, month, 1).strftime('%B')} {day} {year}"
           

        w.writerow(line)



with open('1000_sample.csv', 'w') as f:
    w = csv.DictWriter(f, blank_dict.keys())
    w.writeheader()
    

    for x in range(1,1000):

        year,month,day = randomDay("1980|1|1", "2018|12|30", random.random()).split('|')
        year = int(year)
        month = int(month)
        day = int(day)

        line = blank_dict.copy()

        line['Headline'] = lorem.sentence()
        line['Text'] = lorem.paragraph()

        if x < 400:
            size = x + 500
        else:
            size = x
        
        line['Media'] = f'https://picsum.photos/{size}/?random'
        line['Media Caption'] = lorem.sentence()


        # just do some years
        if x < 300:
            line['Year'] = year

            line['Display Date'] = year

        elif x < 600:
            line['Year'] = year
            line['Month'] = month

            line['Display Date'] = f"{datetime.date(year, month, 1).strftime('%B')} {year}"
        else:
            line['Year'] = year
            line['Month'] = month
            line['Day'] = day

            line['Display Date'] = f"{datetime.date(year, month, 1).strftime('%B')} {day} {year}"
           

        w.writerow(line)



