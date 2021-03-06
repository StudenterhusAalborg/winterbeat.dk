from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from django.views.decorators.clickjacking import xframe_options_exempt

from festivals.decorators import festival_required
from festivals.models import Page, Artist, Post


@festival_required
def index(request):
    return render(request, request.festival.theme + "/index.html", {
        "artists": Artist.objects.released().filter(festival=request.festival),
        "festival": request.festival,
    })


@festival_required
def show_page(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug, festival=request.festival)
    return render(request, request.festival.theme + "/page.html", {
        "post": page,
    })


@festival_required
@xframe_options_exempt
def show_artist(request, artist_slug):
    artist = get_object_or_404(Artist, slug=artist_slug, festival=request.festival)

    return render(request, request.festival.theme + "/artist.html", {
        "artist": artist,
    })


@festival_required
def schedule(request):
    context = {
        'artists': Artist.objects.filter(
            stage__festival=request.festival
        ).exclude(
            stage=None, concert_time=None
        )
    }
    return render(request, request.festival.theme + "/schedule.html", context)
    # concerts = Concert.objects.all().order_by("date", "sort_order")
    # return render(request, "winter-beat/schedule.html", {"concerts": concerts})


@festival_required
def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk, festival=request.festival)
    return render(request, request.festival.theme + "view_post.html", {"post": post})


@festival_required
def list_posts(request):
    posts = Post.objects.all() if request.user.is_authenticated and request.user.is_superuser \
        else Post.objects.filter(festival=request.festival, created__lte=now())
    return render(request, request.festival.theme + "/list_posts.html", {"posts": posts})
