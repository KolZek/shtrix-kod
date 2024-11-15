from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Record
from .forms import RecordForm, RecordFormIssueDate


def index(request):
    """Главна страница сайта."""
    template = "posts/index.html"

    options_data = request.GET

    record_list = Record.objects.exclude(~Q(issue_date=None))
    if "f" in options_data.keys() and options_data["f"] != "":
        record_list = Record.objects.all()
    if "o" in options_data.keys() and options_data["o"] != "":
        options = options_data["o"].split(",")
        options = [x for x in options if x != ""]
        record_list = record_list.order_by(*options).all()

    page_obj = paginator(request, record_list)
    context = {
        "page_obj": page_obj,
        "querydict": options_data
    }

    is_info_msg = request.session.get("is_info_message")
    if is_info_msg:
        context["is_info_message"] = is_info_msg
        request.session.pop("is_info_message", None)

    return render(request, template, context)


def record_create(request):
    """Страница создания новой записи."""
    template = "posts/create_post.html"
    form = RecordForm(files=request.FILES or None)
    context = {"form": form}
    if request.method == "POST":
        form = RecordForm(request.POST or None, files=request.FILES or None)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            request.session["is_info_message"] = "Запись успешно создана"
            return redirect("index:index")
        return render(request, template, context)
    return render(request, template, context)


def record_add_issue_date(request, record_id):
    """Страница добавления даты выдачи."""
    record = get_object_or_404(Record, id=record_id)
    template = "posts/create_post.html"
    form = RecordFormIssueDate(files=request.FILES or None, instance=record)
    context = {
        "form": form,
        "is_add_issue": True
    }
    if request.method == "POST":
        form = RecordFormIssueDate(
            request.POST or None, files=request.FILES or None, instance=record
        )
        if form.is_valid():
            record.save()
            request.session["is_info_message"] = "Дата выдачи успешно добавлена"
            return redirect("index:index")
        return render(request, template, context)
    return render(request, template, context)


def record_edit(request, record_id):
    """Страница редактирования записи."""
    record = get_object_or_404(Record, id=record_id)
    template = "posts/create_post.html"
    form = RecordForm(files=request.FILES or None, instance=record)
    context = {
        "form": form,
        "record_id": record_id,
        "is_edit": True
    }
    if request.method == "POST":
        form = RecordForm(
            request.POST or None, files=request.FILES or None, instance=record
        )
        if form.is_valid():
            form.save()
            request.session["is_info_message"] = "Запись успешно отредактирована"
            return redirect("index:index")
    return render(
        request,
        template,
        context,
    )


def record_delete(request, record_id):
    """Удаление записи."""
    record = get_object_or_404(Record, id=record_id)
    record.delete()
    request.session["is_info_message"] = "Запись успешно удалена"
    return redirect("index:index")


def paginator(request, post_list):
    paginator = Paginator(post_list, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj
