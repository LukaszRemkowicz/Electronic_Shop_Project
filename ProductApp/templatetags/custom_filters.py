from django import template

register = template.Library()


def search_for_url(url: str, param: str, what_to_lf: str) -> bool:
    if param in url:
        for element in url.split('&'):
            if param in element:
                element = element.split(f'{param}=')
                try:
                    boolean = element[1]
                    if boolean == what_to_lf:
                        return True
                except Exception:
                    return False
        return False
    else:
        return False


@register.filter
def find_producent(url: str) -> str:
    url = url.split('&')
    for urll in url:
        if 'producent=' in urll:
            return urll.split('producent=')[1]

@register.filter
def find_grid (url: str) -> bool:
    return search_for_url(url, 'grid', 'true')


@register.filter
def get_attr(dictionary: dict, name: str) -> str:
    return dictionary.get(name)


@register.filter
def check_curved(url: str) -> bool:
    return search_for_url(url, 'curved', 'Yes')


@register.filter
def check_smart(url: str) -> bool:
    return search_for_url(url, 'smart', 'Yes')
