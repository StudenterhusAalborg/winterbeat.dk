from typing import Type, Tuple

from django.db import models
from django.db.models import Field
from django.template.defaultfilters import slugify
# Create your models here.
from django.utils.safestring import mark_safe
from django.utils.text import format_lazy
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy, get_language, ugettext
from solo.models import SingletonModel


def create_field_for_both_languages(field_type: Type[Field], pretty_name: str, **kwargs) -> Tuple[Field, Field]:
    """
    helper for making the same textfield for danish and english.
    :param field_type:
    :param pretty_name:
    :param kwargs:
    :return: a 2-tuple of two fields
    """
    ret: Tuple[Field, Field] = tuple(field_type(
        format_lazy("{pretty_name} [{lang}]", pretty_name=pretty_name, lang=lang),
        **kwargs
    ) for lang in [ugettext_lazy("Danish"), ugettext_lazy("English")])

    return ret


class WinterbeatSettings(SingletonModel):
    top_text_da, top_text_en = create_field_for_both_languages(
        models.TextField,
        ugettext_lazy("Top text"),
        help_text=ugettext_lazy("the paragraph above the list of bands. Is hidden if empty"),
        default=""
    )
    bottom_text_da, bottom_text_en = create_field_for_both_languages(
        models.TextField,
        ugettext_lazy("Bottom text"),
        help_text=ugettext_lazy("The paragraph below the list of bands. It is hidden if empty"),
        default=""
    )

    description = models.TextField(
        ugettext_lazy("Description"),
        help_text=ugettext_lazy("The description that is used when linking to winterbeat from another page"),
        default=""
    )

    show_nav_bar = models.BooleanField(
        ugettext_lazy("Show navigation bar"),
        help_text=ugettext_lazy("Show the bar of pages on top or not."),
        default=False
    )

    def __str__(self):
        return ugettext("Winterbeat Settings")

    @property
    def bottom_text(self):
        return mark_safe(self.bottom_text_da if get_language() == "da" else self.bottom_text_en)

    def top_text(self):
        return mark_safe(self.top_text_da if get_language() == "da" else self.top_text_en)

    class Meta:
        verbose_name = ugettext_lazy("Winterbeat Settings")


class Page(models.Model):
    title_da, title_en = create_field_for_both_languages(
        models.CharField,
        ugettext_lazy("title"),
        max_length=64
    )
    slug = models.CharField(
        ugettext_lazy("slug"),
        max_length=64
    )
    # page including html
    body_da, body_en = create_field_for_both_languages(
        models.TextField,
        ugettext_lazy("body"),
        help_text="Accepts HTML etc. make sure you don't abuse this!"
    )

    @property
    def title(self):
        return self.title_da if get_language() == "da" else self.title_en

    @property
    def body(self):
        return mark_safe(self.body_da if get_language() == "da" else self.body_en)

    def save(self, **kwargs):
        self.slug = slugify(self.title_en)
        super().save(**kwargs)

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = ugettext_lazy("page")
        verbose_name_plural = ugettext_lazy("pages")


class Artist(models.Model):
    name = models.CharField(
        ugettext_lazy("name"),
        max_length=128
    )
    description_da, description_en = create_field_for_both_languages(
        models.TextField,
        ugettext_lazy("description"),
        blank=True,
        default=""
    )
    subtitle = models.CharField(
        ugettext_lazy("subtitle"),
        max_length=128,
        blank=True,
        default="")
    youtube_video_link = models.CharField(
        max_length=128,
        blank=True,
        default="")

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        super().save(**kwargs)

    def __str__(self):
        return self.name

    @property
    def name_len(self):
        return len(self.name)

    @property
    def description(self):
        return self.description_da if get_language() == "da" else self.description_en

    @property
    def body(self):
        return mark_safe((self.description + (f"<br><br> {self.embedded_youtube}" if self.youtube_video_link else "")).
                         replace("\r\n", "<br>").replace("\n", "<br>"))

    @property
    def embedded_youtube(self):
        link = self.youtube_video_link.replace("watch?v=", "embed/")
        return f'<div class="embed-responsive embed-responsive-16by9"><iframe src="{link}" width="100%" class="embed-responsive-item" allowfullscreen></iframe></div>'

    class Meta:
        verbose_name = ugettext_lazy("artist")
        verbose_name_plural = ugettext_lazy("artists")
        ordering = ("pk",)

class Post(models.Model):
    title_da, title_en = create_field_for_both_languages(
        models.CharField,
        ugettext_lazy("title"),
        max_length=128
    )
    body_da, body_en = create_field_for_both_languages(
        models.TextField,
        ugettext_lazy("body"),
        help_text="Can contain HTML, however be careful as this could make fucked up shit"
    )
    created = models.DateTimeField(default=now)

    def title(self):
        return self.title_da if get_language() == "da" else self.title_en

    def __str__(self):
        return f"{self.title} ({self.created})"

    class Meta:
        verbose_name = ugettext_lazy("post")
        verbose_name_plural = ugettext_lazy("posts")
