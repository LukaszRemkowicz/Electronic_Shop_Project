import copy

from ProductApp.models import MainProductDatabase
from Articles.models import LandingPageArticles

def get_url_path(request, product_page=False):
    url_path =request.path
    url_path = url_path.split('/')[1:-1]
    if 'blog' in url_path or 'articles' in url_path:
        url_path.pop(url_path.index('blog'))
        url_path.pop(url_path.index('articles'))
        id = url_path.pop()
        url_path.append(LandingPageArticles.objects.get(id=id).title)
    elif url_path[-1].isdigit() and not product_page:
        url_path.pop()
    elif url_path[-1].isdigit() and product_page:
        id = url_path.pop()
        url_path.append(MainProductDatabase.objects.get(id=id).name)


    url_path = [element.replace('-', ' ') for element in url_path]
    url_path_cp = copy.deepcopy(url_path)
    new_url_path = []

    for num, _ in enumerate(url_path_cp):
        if num +1 < len(url_path):
            new_url_path.append('/'.join(url_path_cp[:-1]))
            url_path_cp.pop()
    new_url_path.reverse()

    last_element = url_path.pop()
    url_path_dict = { name: path for name, path in zip(url_path, new_url_path) }

    return last_element, url_path_dict