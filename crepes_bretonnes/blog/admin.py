from django.contrib import admin
from .models import Categorie, Article
from django.utils.text import Truncator
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):

    # Configuration de la liste d'articles
    list_display = ('titre', 'auteur', 'date', 'apercu_contenu')
    list_filter = ('auteur', 'categorie',)
    date_hierarchy = 'date'
    ordering = ('date', )
    search_field = ('titre', 'contenu')

    # Configuration du formulaire d'édition
#    fields = ('titre', 'auteur', 'categorie', 'contenu')
    fieldsets = (
                    # Fieldset 1 : meta-info (titre, auteur...)
                    ('Général', {
                        'classes': ['collapse', ],
                        'fields': ('titre','slug', 'auteur', 'categorie')
                    }),
                    # Fieldset 2 : contenu de l'article
                    ('Contenu de l\'article', {
                        'description': 'Le formulaire accepte les balises HTML.Utilisez - les à bon escient !',
                     'fields': ('contenu',)
                    }),)

    # remplit automatiquement le champ slug avec titre
    prepopulated_fields = {'slug': ('titre',), }

    # Colonnes personnalisées
    def apercu_contenu(self, article):
        """
        Retourne les 40 premiers caractères du contenu de
        l'article,suivi de points de suspension si le texte est plus
        long.
        On pourrait le coder nous même, mais Django fournit
        déjà la fonction qui le fait pour nous !
        """
        return Truncator(article.contenu).chars(40, truncate='...')

    apercu_contenu.short_description = 'Aperçu du contenu'


admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)




