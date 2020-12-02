import csv  # https://docs.python.org/3/library/csv.html
from unesco.models import States,Region,Site,Iso,Category

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

#0name,1description,2justification,3year,4longitude,5latitude,
#6area_hectares,7category,8states,9region,10iso

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader)

    States.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()
    Iso.objects.all().delete()
    Category.objects.all().delete()
    cnt = 0
    for row in reader:
        print(cnt,row[0])
        cnt += 1
        i,created = Iso.objects.get_or_create(name = row[10])
        c,created = Category.objects.get_or_create(name= row[7])
        r,created = Region.objects.get_or_create(name= row[9])
        st =  States(name= row[8], region = r)
        try:
            st = States.objects.get(name = row[8])
        except:
            st.save()
        try:
            y = int(row[3])
        except:
            y = None
        try:
            lng = float(row[4])
        except:
            lng = None
        try:
            lat = float(row[5])
        except:
            lat = None
        try:
            hect = float(row[6])
        except:
            hect = None
        si = Site(
            name = row[0],
            year = y,
            description = row[1],
            justification = row[2],
            longitude = lng,
            latitude = lat,
            area_hectares = hect,
            category = c,
            state = st,
            iso = i
        )
        si.save()


