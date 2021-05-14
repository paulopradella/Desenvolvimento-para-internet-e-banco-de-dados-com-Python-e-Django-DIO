from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello World!!! Como vai {}, de {} anos?</h1>'.format(nome, idade))

def soma(request, numero_a, numero_b):
    total = numero_a + numero_b
    return HttpResponse('<h1>A soma é: {}</h1>'.fomart(total))

def subtracao(request, numero_a, numero_b):
    total = numero_a - numero_b
    return HttpResponse('<h1>A subtração é: {}</h1>'.fomart(total))

def multiplicacao(request, numero_a, numero_b):
    total = numero_a * numero_b
    return HttpResponse('<h1>A multiplicação é: {}</h1>'.fomart(total))

def divisao(request, numero_a, numero_b):
    total = numero_a / numero_b
    return HttpResponse('<h1>A divisão é: {}</h1>'.fomart(total))