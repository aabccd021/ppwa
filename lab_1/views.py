from django.shortcuts import render
from datetime import datetime, date
# Enter your name here
mhs_name = 'Muhamad Abdurahman' # TODO Implement this
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date(1998, 2, 21) #TODO Implement this, format (Year, Month, Date)
npm = 1706040095 # TODO Implement this
university = "Indonesia Univesity"
hobby = "to find new Hobby"
descriptions = "partly good person"
# Create your views here.
def index(request):
    response = {'name': mhs_name,
                'age': calculate_age(birth_date.year),
                'npm': npm,
                'university': university,
                'hobby': hobby,
                'descriptions': descriptions}
    return render(request, 'index_lab1.html', response)

def calculate_age(birth_year):
    return curr_year - birth_year if birth_year <= curr_year else 0
