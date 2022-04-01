class HTML:
    def __init__(self):
        self.text = ['']

    def get_code(self):
        return self.text[0]

    def body(self):
        return html._body(self)

    def div(self):
        return html._div(self)

    def p(self, value):
        return html._p(self, value)

    class _body:
        def __init__(self, outer):
            self.text = outer.text

        def __enter__(self):
            self.text[0] += '<body>\n'

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.text[0] += '</body>\n'

    class _div:
        def __init__(self, outer):
            self.text = outer.text

        def __enter__(self):
            self.text[0] += '<div>\n'

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.text[0] += '</div>\n'

    class _p:
        def __init__(self, outer, value):
            outer.text[0] += '<p>' + value + '</p>\n'


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')
print(html.get_code())
