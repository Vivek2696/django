from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'january': ['Donate something for good of society','Month of Makar Shankranti. Uttarayan and kite festival.'],
    'february': ['Do fast on Maha Shivratri.', 'Month of festival like Maha Shivratri, Lohri, Vasant Panchmi and more...'],
    'march': ['Participate in Holi Dahan.', 'This is the month of Holi, cheti chand and more...'],
    'april': ['New year\'s resolution Ram Navami.', 'This month is also of chaitra navratri, hanuman jayanti and more...'],
    'may': ['Take step towards your health.', 'This month has Dev Snan Purnima, summer solstice.'],
    'june': ['Follow Rath Yatra (May start this month ending or beginning of next month).', 'Month of Ashadh (Monsoon), gayatri jayanti as well'],
    'july': ['Do somthing for Janmastmi.', 'This month is has some of Shravan mah where Shiva drank posion that emerged during the churned ocean.'],
    'august': ['Follow rituals of Raksha Bandhan.', 'This month has Varah Jayanti and may have Krishna Janmastami and more...'],
    'september': ['Make sweets for Ganesh Chaturthi.', 'This month has Vishwakarma Puja, and may constain start of Navaratri.'],
    'october': ['Participate on Navaratri Garba.', 'This month also has Maha Navami, Dushehraa, and begining of Diwali.'],
    'november': ['Light up some diya for Diwali.', 'This month has Diwali, Gujarati new year, Kali puja, Dhanteras and many more...'],
    'december': ['Help in harvest season.', 'This month may has Dev Diwali, Margashirsha and more...']
}

# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys()) # Using the fact that keys will be ordered for Python 3.6 and beyond

    if month > len(months) or month < 1:
        return HttpResponseNotFound('<h2>Invalid numbered month!</h2>')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f'<h2>{challenge_text[0]}</h2><h3>Facts for this month:<h3><h3>{challenge_text[1]}</h3>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h2>This month is not supported!</h2>')