from django.shortcuts import render

def game(request):
    user = ('images/testImage.svg', 19885)
    boss_img = 'images/testImage.svg'
    leaderboard = [(1, 1239123, 'User228'), (2, 123123, 'UserGandon'), (3, 123, 'Niiggaaaa'), (4, 0, 'dmitrywall.ru')]
    ants = [('images/testImage.svg', 12, 128), ('images/testImage.svg', 8, 85), ('images/testImage.svg', 3, 39)]
    total_ants = sum(map(lambda x: x[1], ants))
    items = [('images/testImage.svg', 'Капля мёда', 16), ('images/testImage.svg', 'Капля спермы', 58), ('images/testImage.svg', 'Залупа Артёма', 9999)]
    chest = ('images/testImage.svg', 228)

    data = {"user": user, "boss_img": boss_img, "leaderboard": leaderboard, "ants": ants, "total_ants": total_ants, "items": items, "chest": chest}
    return render(request, "game.html", context=data)