from django.shortcuts import render


def runoob(request):
    # # key - value, use the value
    # context = {}
    # context['hello'] = 'hello world'
    # return render(request, 'runoob.html', context)

    # views_name = 'me'
    # return render(request, 'runoob.html', {'name': views_name})

    # # link
    # view_list = "<a href='https://www.runoob.com/'>点击跳转</a>"
    # return render(request, 'runoob.html', {'name': view_list})

    lst = [1, 2, 3, 4, 5, 6]
    return render(request, 'runoob.html', {'name':lst})