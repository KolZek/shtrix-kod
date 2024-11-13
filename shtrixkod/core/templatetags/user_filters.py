import re
import datetime as dt

from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def checkdate(date, is_issue_date):
    date_now = dt.date.today()

    if is_issue_date:
        return "#0d6efd"
    elif date == date_now:
        return "#ffaa00"
    elif date > date_now:
        return "green"
    else:
        return "red"


@register.filter
def paidstorage(date):
    paid_storage = date + dt.timedelta(days=3)
    return paid_storage


@register.filter
def paidstoragesum(date):
    paid_storage_date = paidstorage(date)
    date_now = dt.date.today()

    if date_now >= paid_storage_date:
        return True
    return False


@register.filter
def getpaidstoragesum(volume, date):
    paid_storage = paidstorage(date)
    date_now = dt.date.today()

    date_difference = date_now - paid_storage
    days_coeff = 1 if date_difference.days == 0 else date_difference.days

    result_sum = int(volume*(350*days_coeff))
    result_sum = re.sub(r"(?<!^)(?=(\d{3})+$)", ".", str(result_sum))

    return result_sum


@register.filter
def checkoption(querydict, option):
    if option in querydict and querydict is not None:
        querydict = querydict.split(",")
        querydict.remove(option)
        querydict = ",".join(querydict)
    return querydict


@register.filter
def startswith(value, prefix):
    return value.startswith(prefix)
