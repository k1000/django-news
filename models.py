from django.db import models
from datetime import datetime
from django.utils.translation import ugettext as _
# Create your models here.
# define the models
class NewsManager(models.Manager):
    def get_published(self):
        return self.filter(publish=True, pub_date__lte=datetime.now)
    def get_drafts(self):
        return self.filter(publish=False)

class News(models.Model):
    pub_date = models.DateTimeField(_(u"fecha publicacion"), default=datetime.now)
    headline = models.CharField(_("titulo"), max_length=200)
    slug = models.SlugField(_("identificador"), help_text=u'"Identificador" es URL-amigable, unico titulo para la noticia.')
    summary = models.TextField(_("Resumen") )
    body = models.TextField(_("contenido"))
    author = models.CharField(_("author"), max_length=100)
    publish = models.BooleanField( _("Publicar en la web"), default=True,
                                  help_text='Articles will not appear on the site until their "publish date".')
    sections = models.ForeignKey(_('Section'), related_name='section')
    image = models.ImageField(_("imagen principal"), upload_to="upload", )
    enable_comments = models.BooleanField(_("activar acometarios"), default=False)

    # Custom article manager
    objects = NewsManager()

    class Meta:
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
        verbose_name = _('entrada')
        verbose_name_plural = _('entradas')
    
    def __unicode__(self):
        return self.headline

    def get_absolute_url(self):
        args = self.pub_date.strftime("%Y/%b/%d").lower().split("/") + [self.slug]
        return reverse('pr-article-detail', args=args)

class Section(models.Model):
    title = models.CharField("seccion", max_length=80, unique=True)
    slug = models.SlugField()

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pr-section', args=[self.slug])
