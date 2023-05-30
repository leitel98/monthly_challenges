from django.shortcuts import render
from django.http import  Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# month dictionary
monthly_challenges = {
    "january": "Eat no meat for one month",
    "february": "Walk for 20 mins every day",
    "march": "march challenge",
    "april": "april challenge",
    "may": "may challenges",
    "june": "june challenge",
    "july": "july challenge",
    "august": "august challenge",
    "september": "september challenge",
    "october": "october challenge",
    "november": "november challenge",
    "december": None,
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge(request, month):  # here month is a str
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()


def monthly_challenge_by_number(request, month):  # here month is a num
    # turns monthly challenges to a list
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month: out of index")

    # indexes the list with the month number and gets it
    redirect_month = months[month - 1]
    # goes to the url with the name month challenge
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
