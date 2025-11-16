from django.shortcuts import render


def universal_page(request, path=''):
    page_names = {
        '/': 'Главная страница',
        '/about/': 'О компании',
        '/services/': 'Услуги',
        '/contacts/': 'Контакты',
    }
    
    page_name = page_names.get(request.path, f'Страница: {request.path}')
    
    return render(request, 'tree_menu/test_page.html', {
        'page_name': page_name,
    })