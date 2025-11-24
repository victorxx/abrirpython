1. Navegação

page.goto(url) → Navega para uma URL.

page.reload() → Recarrega a página.

page.goBack() → Volta à página anterior.

page.goForward() → Avança para a próxima página.

2. Interação com elementos (cliques e inputs)

Clique em elementos

page.click(selector)
page.dblclick(selector) // clique duplo
page.tap(selector)      // em dispositivos móveis


Digitação

page.fill(selector, text) // substitui o conteúdo
page.type(selector, text, { delay: 100 }) // digita simulando teclado


Seleção

page.selectOption(selector, 'value') // selecionar valor em <select>
page.selectOption(selector, ['value1','value2']) // múltiplos


Arrastar e soltar

page.dragAndDrop(sourceSelector, targetSelector)


Hover (passar o mouse)

page.hover(selector)


Foco

page.focus(selector)


Checkbox / Radio

page.check(selector)   // marca
page.uncheck(selector) // desmarca
page.isChecked(selector) // verifica estado

3. Eventos do teclado
page.keyboard.press('Enter')
page.keyboard.type('Hello World')
page.keyboard.down('Shift')
page.keyboard.up('Shift')

4. Eventos do mouse
page.mouse.move(x, y)
page.mouse.click(x, y)
page.mouse.down()
page.mouse.up()
page.mouse.wheel({ deltaX, deltaY })

5. Interação com frames e iframes
const frame = page.frame({ name: 'frameName' })
frame.click(selector)
frame.fill(selector, 'text')

6. Scrolling
page.evaluate(() => window.scrollBy(0, 1000))
page.evaluate(() => document.querySelector('selector').scrollIntoView())

7. Manipulação de arquivos
page.setInputFiles(selector, 'path/to/file') // upload

8. Captura de tela e PDF
page.screenshot({ path: 'screenshot.png' })
page.pdf({ path: 'page.pdf' })

9. Esperas e sincronização
page.waitForSelector(selector)       // espera elemento aparecer
page.waitForTimeout(2000)            // espera fixa (ms)
page.waitForNavigation()             // espera carregamento de página
page.waitForResponse(urlOrPredicate) // espera resposta de rede

10. Outras interações úteis

Alertas e diálogos

page.on('dialog', dialog => dialog.accept())


Cookies

page.context().cookies()
page.context().addCookies([{ name, value, url }])


Local Storage

page.evaluate(() => localStorage.setItem('key', 'value'))
