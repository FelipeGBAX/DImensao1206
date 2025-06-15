$ saude = 60
$ ameaca = 0 
$ carol_taverna = false
define dante = Character("Dante")
define chatzinho = Character("Chat", color = "#ff0000")
define carol = Character("???", color = "#ffffff")
define daniela = Character("???")
define traira = Character("???")
define luck = Character("???")


image bk_white = "images/tela-branca.png"
image chatzinho_normal = "images/chat_normal.png"
image chatzinho_boca_aberta = "images/chat_boca_aberta.png"
image chatzinho_surpreso = "images/"
image chatzinho_feliz = "images/"
image carol_bebada = "images/carol_normal.png"
image bk_nightpark = "images/bk_nightpark.png"

label start:
    
    scene bk_white:
        zoom 2
    with dissolve
    show chatzinho_normal at truecenter:
        zoom 2.5
        yalign 0.5
    chatzinho "Onde eu estou?"
    dante "Chat? É você?"
    chatzinho "Pãe????"

    scene bk_nightpark at truecenter:
        zoom 1.37
    show chatzinho_normal at center:
        zoom 0.9

    dante "Por que que você tá aqui?"
    hide chatzinho_normal
    show chatzinho_boca_aberta at center:
        zoom 0.9
    with dissolve

    chatzinho "Eu estava investigando movimentações suspeitas e vim parar aqui!"
    chatzinho "Você ta bem????"
    hide chatzinho_boca_aberta
    
    show chatzinho_normal
    dante "Essa é a menor das minhas preocupações… Acho que estamos presos aqui…"
    hide chatzinho_normal
    
    show chatzinho_surpreso
    chatzinho "QUE"
    hide chatzinho_surpreso

    show chatzinho_normal
    dante "Uma porta apareceu em um lugar incomum da yggdrasil, quando fui ver acabei caindo aqui.."
    dante "E a chave nao quer funcionar desde então"

    hide chatzinho_normal
    show chatzinho_feliz
    chatzinho "Acho que é hora investigar!"

    hide chatzinho_feliz
    show chatzinho_normal
    dante "Vamos olhar por aí"

    "Vocês observam o local e percebem uma estátua no parque."

    hide chatzinho_normal
    show chatzinho_boca_aberta
    chatzinho "PREDA!"
    
    hide chatzinho_boca_aberta
    show chatzinho_normal
    dante "Ah não…"
    dante "Que estátua esquisita…"

    hide chatzinho_normal
    show chatzinho_boca_aberta
    chatzinho "Ela tem uma legenda estranha, diz ‘Almas egoístas..."

    hide chatzinho_boca_aberta
    show chatzinho_normal
    carol "NINGUÉM ME AMAAAAA"

    hide chatzinho_normal
    show chatzinho_boca_aberta
    chatzinho "Eita, que isso meu deus?"

    hide chatzinho_boca_aberta
    show carol_bebada at truecenter:
        zoom 0.9
    "Vocês se viram em direção ao grito, há uma mulher cambaleando na beira de uma lagoa"
    "Parece que ela vai pular, ou cair a qualquer momento"

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