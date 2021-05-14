from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import Article, Contact
from .forms import ContactForm, NouveauContactForm, ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def home (request):
    return HttpResponse("""
   <html>
   <body> 
    <h1> Bienvenue sur mon blog </h1>
    <p>Ah que coucou</p>
    </body>
    </html>
    """)

def view_article(request, id_article):
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    if int(id_article) > 100:
        raise Http404
#    return redirect(view_redirection)
#    return redirect('afficher article', id_article=42)
    return HttpResponse('Article de ' + id_article)

#   return HttpResponse(
#   "Vous avez demandé l'article n° {0} !".format(id_article))



def list_articles(request, year, month=1):
    """ Liste des articles d'un mois précis. """
    return HttpResponse('Articles de %s/%s' % (year, month))
# Create your views here.

def view_redirection(request):
    return HttpResponse("vous avez été redirigé")

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date':
datetime.now()})

def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2
    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())

def mapping(request):
    return render(request, 'blog/mapping.html')

def view_photos(request):
    return render(request, 'blog/photos.html')

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id,slug):
    """ Afficher un article complet """
#    try:
#        article = Article.objects.get(id=id)
#    except Article.DoesNotExist:
#        raise Http404
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article': article})

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.

    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

    # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/contact.html', locals())

def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True
    return render(request, 'blog/contact_test.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })



def voir_contacts(request):
    return render(request,'blog/voir_contacts.html', {'contacts': Contact.objects.all()})

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,password=password)  # Nous vérifions si les données sont correctes
            if user is not None:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'blog/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

@login_required
def ma_vue(request):
    return render(request, 'blog/connexion.html', locals())
