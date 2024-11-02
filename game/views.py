from django.shortcuts import render

from game.models import User


def game(request):
    user = ('images/testImage.svg', 19885)
    boss_img = 'images/testImage.svg'
    leaderboard = [(i + 1, leader.ant_count, leader.name) for i, leader in
                   enumerate(get_leaderboard())[:len(get_leaderboard())]]

    ants = [('images/testImage.svg', 12, 128), ('images/testImage.svg', 8, 85), ('images/testImage.svg', 3, 39)]
    total_ants = sum(map(lambda x: x[1], ants))
    items = [('images/testImage.svg', 'Капля мёда', 16), ('images/testImage.svg', 'Капля спермы', 58),
             ('images/testImage.svg', 'Залупа Артёма', 9999)]
    chest = ('images/testImage.svg', 228)

    data = {"user": user, "boss_img": boss_img, "leaderboard": leaderboard, "ants": ants, "total_ants": total_ants,
            "items": items, "chest": chest}
    return render(request, "game.html", context=data)


def get_leaderboard() -> list[User]:
    return User.objects.all().order_by('-ant_count')[:20] if len(User.objects.all()) > 20 else User.objects.all().order_by(
        '-ant_count')
