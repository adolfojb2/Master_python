from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from miapp.forms import FormArticle

# Create your views here.
#MVC = Modelo vista controlador
#MVT = Modelo Template vista  -> MVC para Django

nombre = 'Adolfo Betin'
lenguajes = ['Python','PHP','C','JavaScript','Go','Java','Rust']
year = 2021
hasta = range(year,2051)
def index(request):
    return render(request, 'index.html',{'mi_dato':'Esta información es enviada desde las vistas.',
                                         'title':'Inicio',
                                         'nombre':nombre,
                                         'lenguajes':lenguajes,
                                         'years':hasta
    })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request):
    return render(request, 'pagina.html')

def contacto(requets):
    return render(requets, 'contacto.html')

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public)
    articulo.save()
    return HttpResponse(f"Usuario creado: <strong>{articulo.title}</strong> - {articulo.content}")

def save_article(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']
        articulo = Article(
            title = title,
            content = content,
            public = public)
        articulo.save()
        return HttpResponse(f"Usuario creado: <strong>{articulo.title}</strong> - {articulo.content}")
    else:
        return HttpResponse("<h2>No se a podido crear el articulo.</h2>")

    

def create_article(request):
    return render(request, 'create_article.html')

def create_full_article(request):

    if request.method == 'POST':
        formulario = FormArticle(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']
            articulo = Article(
            title = title,
            content = content,
            public = public)
            articulo.save()
            return redirect('articulos')
            #return HttpResponse(articulo.title + ' - ' + articulo.content + ' - ' + str(articulo.public))
    else:
        formulario = FormArticle()
    return render(request, 'create_full_article.html', {'form': formulario})

def articulo(request):
    try:
        articulo = Article.objects.get(title="Superman", public=False)
        Response = f"Articulo: <br/> {articulo.id}. {articulo.title}"
    except:
        Response = "Articulo no encontrado"    
    return HttpResponse(Response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True
    articulo.save()
    return HttpResponse(f"Articulo {articulo.id} editado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulos(request):
    articulos = Article.objects.all().order_by('-id')
    # articulos = Article.objects.filter(title__contains = "articulo")
    # articulos = Article.objects.filter(title__contains="articulo",).exclude(public = False)

    return render(request, 'articulos.html', {'articulos': articulos})

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos') 
