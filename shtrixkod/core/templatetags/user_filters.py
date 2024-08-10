import datetime as dt

from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def checkdate(date):
    date_now = dt.date.today()
    conv_dt = dt.datetime.strptime(date, "%d.%m.%Y").date()

    if conv_dt == date_now:
        return "#ffaa00"
    elif conv_dt > date_now:
        return "green"
    else:
        return "red"
    

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
