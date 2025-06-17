default saude = 60
default ameaca = 0 
default carol_taverna = False

define dante = Character("Dante", image = "dante")
define chatzinho = Character("Chat", color = "#ff0000")
define carol = Character("???", color = "#ffffff")
define daniela = Character("???")
define traira = Character("???")
define luck = Character("???")


image bk_white = "images/tela-branca.png"
image bk_nightpark = "images/bk_nightpark.png"

image side dante surpreso= im.Scale("images/dante surpreso.png", 594, 1056, xoffset = -15, yoffset = 430)

image chatzinho_normal = im.Scale("images/chat_normal.png", 972, 1728)
image chatzinho_boca_aberta = im.Scale("images/chat_boca_aberta.png", 972, 1728)
image chatzinho_desnorteado = im.Scale("images/chat_desnorteado.png", 972, 1728)
image chatzinho_surpreso = im.Scale("images/chat_surpreso.png", 972, 1728)
image chatzinho_feliz = im.Scale("images/chat_feliz.png", 972, 1728)
image chatzinho_confuso = im.Scale("images/chat_confuso.png", 972, 1728)

image carol_normal = "images/carol_normal.png"
image carol_bebada = im.Scale("images/carol_bebada.png", 972, 1728, yoffset = 250)

label start:
    
    scene bk_white:
        zoom 2
    with dissolve

    show chatzinho_desnorteado at truecenter:
        zoom 2.5
        yalign 0.5
    with dissolve

    chatzinho "..."
    chatzinho "Hm?"
    hide chatzinho_desnorteado 
    show chatzinho_boca_aberta at truecenter:
        zoom 2.5
        yalign 0.5
    with dissolve

    chatzinho "Onde eu estou?"
    dante "Chat? É você?"
    hide chatzinho_boca_aberta
    show chatzinho_surpreso at truecenter:
        zoom 2.5
        yalign 0.5
    with dissolve
    chatzinho "Pãe????"

    scene bk_nightpark at truecenter:
        zoom 1.37
    hide chatzinho_surpreso
    show chatzinho_normal at center
    with fade

    dante surpreso "Por que que você tá aqui?"
    hide chatzinho_normal
    show chatzinho_boca_aberta at center
    with dissolve

    chatzinho "Eu estava investigando movimentações suspeitas e vim parar aqui! Você ta bem????"
    hide chatzinho_boca_aberta
    show chatzinho_normal at center
    with dissolve

    dante "Essa é a menor das minhas preocupações… Acho que estamos presos aqui…"
    hide chatzinho_normal
    
    show chatzinho_surpreso at center:
        ypos 1410
        easein 0.3 ypos 1440
    
    chatzinho "QUE? Como assim?"

    dante "Não sei bem o que aconteceu, mas uma porta apareceu em um lugar estranho da yggdrasil, quando fui ver acabei caindo aqui.."
    dante "...A chave nao quer funcionar desde então..."
    hide chatzinho_surpreso
    show chatzinho_normal
    with dissolve
    dante "Vamos olhar por aí e tentar achar um jeito de sair daqui..."
    hide chatzinho_normal
    show chatzinho_feliz at center
    with dissolve

    chatzinho "Acho que é hora investigar!"

    hide chatzinho_feliz
    show chatzinho_normal at center
    with dissolve
    

    "Vocês observam o local e percebem uma estátua no parque."

    hide chatzinho_normal
    show chatzinho_feliz at center
    with dissolve
    chatzinho "PREDA!"
    
    dante "Ah não…"
    dante "Que estátua esquisita…"

    hide chatzinho_feliz
    show chatzinho_confuso at center
    with dissolve

    chatzinho "Ela tem uma legenda estranha, diz ‘Almas egoístas..."
    chatzinho "O que é--"

    hide chatzinho_confuso
    show chatzinho_surpreso at center:
        ypos 1410
        easein 0.3 ypos 1440
    with hpunch
    carol "NINGUÉM ME AMAAAAA"

    hide chatzinho_surpreso
    show chatzinho_boca_aberta at center
    with dissolve
    chatzinho "Eita, que isso meu deus?"

    hide chatzinho_boca_aberta
    
    "Vocês se viram em direção ao grito..."
    "Há uma mulher cambaleando na beira de uma lagoa"
    show carol_bebada
    with dissolve

    "Parece que ela vai {color=#FF0000} pular {/color}, ou {color=#FF0000}cair{/color} a qualquer momento"

    menu:
        "Correr e pegá-la":
            $ ameaca += 10
            $ saude += 10
            jump Emocional
        "Gritar para ela tomar cuidado":
            $ ameaca += 5
            $ saude += 5
            jump Cauteloso
        "Se aproximar e conversar com ela":
            $ ameaca += 2
            $ saude += 2
            jump Racional
        "Ignorar":
            $ saude -=10
            jump Insensível
return