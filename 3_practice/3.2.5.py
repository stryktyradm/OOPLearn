class RenderList:
    def __init__(self, type_lst):
        if type_lst == 'ol':
            self.type_lst = type_lst
        else:
            self.type_lst = 'ul'

    def __call__(self, lst):
        html = '<' + self.type_lst + '>\n'
        for text in lst:
            html += '<li>' + text + '</li>\n'
        html += '</' + self.type_lst + '>'
        return html


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)
