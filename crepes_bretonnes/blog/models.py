from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=False)
    #null=true
    #CASCADE/SET_NULL/PROTECT

    class Meta:
        verbose_name = "article"
        ordering = ['date']

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.titre


class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Moteur(models.Model):
    nom = models.CharField(max_length=25)

    def __str__(self):
        return self.nom

class Voiture(models.Model):
    nom = models.CharField(max_length=25)
    moteur = models.OneToOneField(Moteur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Vendeur(models.Model):
    nom = models.CharField(max_length=30)
    produits = models.ManyToManyField(Produit, through='Offre',
                                          related_name='+')
    produits_sans_prix = models.ManyToManyField(Produit,
                                                    related_name="vendeurs")
    def __str__(self):
        return self.nom

class Offre(models.Model):
    prix = models.IntegerField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    vendeur = models.ForeignKey(Vendeur, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} vendu par {1}".format(self.produit, self.vendeur)


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="photos/")

    def __str__(self):
        return self.nom

def renommage(instance, nom_fichier):
    return "{}-{}".format(instance.id, nom_fichier)

class Document(models.Model):
    nom = models.CharField(max_length=100)
    doc = models.FileField(upload_to=renommage, verbose_name="Document")

class Profil(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING)  # La liaison OneToOne vers le modèle User
    site_web = models.URLField(blank=True)
    avatar = models.ImageField(null=True, blank=True,upload_to="avatars/")
    signature = models.TextField(blank=True)
    inscrit_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return "Profil de {0}".format(self.user.username)

# Create your models here.

## verbose_name (classe meta pour préciser ce que c'est / ex CommentArticle ==> "commentaire d'articles"
## ordering : ordre par défaut de la sélection des données

#NE PAS OUBLIER
# python manage.py makemigrations (noter les changements)
# python manage.py migrate (faire les changements sur la bdd)
# python manage.py shell (jouer avec la bdd)
# from models import Classes ...

#>>> article = Article(titre="Bonjour", auteur="Maxime") (initialiser un objet)
#>>> article.contenu = "Les crêpes sont trop bonnes !"   (changer un attribut)
# article.save() (==pour save le dossier. Modifications pas enregistrées en temps réel)
# article.delete() (==supprimer un objet)
# moteur = Moteur.objects.create(nom="Vroum") (save direct l'objet)


#Article.objects.all() (afficher tout)
# for article in Article.objects.all(): (on peut le parcourir)

#Article(auteur="Mathieu", titre="Les crêpes", contenu="Les crêpes c'est cool").save()

#for article in Article.objects.filter(auteur="Maxime"): FILTER
#for article in Article.objects.exclude(auteur="Maxime"):

## exemple de filter:
#Article.objects.filter(titre__contains="crêpe") ==> __ = méthode du filtre (contains, lt (<), gt)

# différentes fonctions -> Queryset: all, filter, order_by('date'), order_by (-'date')
# fonctions -> object : get, get_or_create
# elles sont cumulables

# cat.article_set.all()

#Article.objects.filter(categorie__nom__contains="crêpes") (2 __ pour clés étrangères)



