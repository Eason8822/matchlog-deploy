from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Match
from .forms import MatchForm
from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # 註冊完直接登入
            return redirect("matches:list")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})



# Create your views here.
@login_required
def match_list(request):
    matches = Match.objects.filter(owner=request.user).order_by("-date", "-id")
    return render(request, "matches/list.html", {
        "matches": matches
    })

@login_required
def match_create(request):
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user   # ⭐ 關鍵
            obj.save()
    return redirect("matches:list")


@login_required
def match_edit(request, pk):
    obj = get_object_or_404(Match, pk=pk, owner=request.user)
    ...

@login_required
def match_delete(request, pk):
    obj = get_object_or_404(Match, pk=pk, owner=request.user)
    if request.method == "POST":
        obj.delete()
    return redirect("matches:list")
