from django.shortcuts import render


def test(request):
    return render(request,'test.html')


def test_choice(request):
    return render(request, 'test_choice.html')


def test_new(request):
    return render(request,'test_new.html')
