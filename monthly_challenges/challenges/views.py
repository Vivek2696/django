from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    'january': 'Donate something for good of society. Facts of this month: Month of Makar Shankranti. Uttarayan and kite festival.',
    'february': 'Do fast on Maha Shivratri. Facts of this month: Month of festival like Maha Shivratri, Lohri, Vasant Panchmi and more...',
    'march': 'Participate in Holi Dahan. Facts of this month: This is the month of Holi, cheti chand and more...',
    'april': 'New year\'s resolution Ram Navami. Facts of this month: This month is also of chaitra navratri, hanuman jayanti and more...',\
    'may': 'Take step towards your health. Facts of this month: This month has Dev Snan Purnima, summer solstice.',
    'june': 'Follow Rath Yatra (May start this month ending or beginning of next month). Facts of this month: Month of Ashadh (Monsoon), gayatri jayanti as well',
    'july': 'Do somthing for Janmastmi. Facts of this month: This month is has some of Shravan mah where Shiva drank posion that emerged during the churned ocean.',
    'august': 'Follow rituals of Raksha Bandhan. Facts of this month: This month has Varah Jayanti and may have Krishna Janmastami and more...',
    'september': 'Make sweets for Ganesh Chaturthi. Facts of this month: This month has Vishwakarma Puja, and may constain start of Navaratri.',
    'october': 'Participate on Navaratri Garba. Facts of this month: This month also has Maha Navami, Dushehraa, and begining of Diwali.',
    'november': 'Light up some diya for Diwali. Facts of this month: This month has Diwali, Gujarati new year, Kali puja, Dhanteras and many more...',
    'december': 'Help in harvest season. Facts of this month: This month may has Dev Diwali, Margashirsha and more...'
}

# Create your views here.
def monthly_challenges_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported')