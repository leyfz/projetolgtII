from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro

def home(request):
    return render(request, 'livros/home.html')


def cadastrar_livro(request):
    if request.method == 'POST':
        Livro.objects.create(
            titulo=request.POST['titulo'],
            autor=request.POST['autor'],
            editora=request.POST['editora'],
            ano=request.POST['ano'],
            paginas=request.POST['paginas'],
            categoria=request.POST['categoria'],
            isbn=request.POST['isbn'],
            idioma=request.POST['idioma'],
            descricao=request.POST['descricao'],
            cadastrado_por=request.POST['cadastrado_por']
        )
        return redirect('confirmacao')

    return render(request, 'livros/cadastro.html')


def confirmacao(request):
    return render(request, 'livros/confirmacao.html')


def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/lista.html', {'livros': livros})


def detalhes_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    return render(request, 'livros/detalhes.html', {'livro': livro})


def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == 'POST':
        livro.delete()
        return redirect('lista')

    return render(request, 'livros/excluir.html', {'livro': livro})


def consultar_livro(request):
    return render(request, 'livros/consulta.html')


def resultado_consulta(request):
    nome = request.GET.get('nome')
    livros = Livro.objects.filter(titulo__icontains=nome)

    return render(request, 'livros/resultado.html', {'livros': livros})


def sobre(request):
    return render(request, 'livros/sobre.html')


def contato(request):
    return render(request, 'livros/contato.html')