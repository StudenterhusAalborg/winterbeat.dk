from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from django.views.decorators.clickjacking import xframe_options_exempt

from northern_winter_beat.models import Page, Artist, Post, Concert


def index(request):
    return render(request, "winter-beat/index.html", {
        "artists": Artist.objects.released(),
    })


def show_page(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)

    return render(request, "winter-beat/page.html", {
        "page": page,
    })


@xframe_options_exempt
def show_artist(request, artist_slug):
    artist = get_object_or_404(Artist, slug=artist_slug)

    return render(request, "winter-beat/artist.html", {
        "artist": artist,
    })


def schedule(request):
    return render(request, "winter-beat/static_schedule.html")
    #concerts = Concert.objects.all().order_by("date", "sort_order")
    #return render(request, "winter-beat/schedule.html", {"concerts": concerts})


def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "winter-beat/view_post.html", {"post": post})


def list_posts(request):
    posts = Post.objects.all() if request.user.is_authenticated and request.user.is_superuser \
        else Post.objects.filter(created__lte=now())
    return render(request, "winter-beat/list_posts.html", {"posts": posts})
