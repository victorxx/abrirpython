Método	O que faz	Quando usar	Tipo de elemento
get_by_text("texto")	Busca elementos pelo texto visível	Qualquer elemento com texto	div, span, button, etc.
get_by_role("role", name="texto")	Busca pelo role (papel/semântica) e nome acessível	Botões, links, inputs, checkboxes, radios	Elementos semânticos com role definido
get_by_label("texto")	Busca inputs, selects, textareas pelo label ou aria-label	Formularios e campos acessíveis	input, select, textarea
:has-text("texto") (CSS)	Filtra elementos que contêm o texto dentro de um seletor CSS	Filtrar por classe, id ou tag específica	Qualquer elemento
locator(..., has_text="texto")	Localiza elementos com texto parcial, permite .first, .last, .nth(n)	Listas ou múltiplos elementos	Qualquer elemento
XPath //tag[text()="texto"] ou contains()	Busca pelo texto no DOM usando XPath	DOMs complexos ou profundos	Qualquer
