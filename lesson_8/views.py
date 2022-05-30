import csv
import datetime
from posixpath import split

from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q

from lesson_8.models import GameModel, GamerLibraryModel, GamerModel


def upload_data(request):
    with open('vgsales.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            try:
                _, created = GameModel.objects.get_or_create(
                    name=row[1],
                    platform=row[2],
                    year=datetime.date(int(row[3]), 1, 1),
                    genre=row[4],
                    publisher=row[5],
                    na_sales=row[6],
                    eu_sales=row[7],
                    jp_sales=row[8],
                    other_sales=row[9],
                    global_sales=row[10],
                )
            except:
                pass
    return HttpResponse("Done!")


class FilterView(ListView):
    template_name = 'gamemodel_list.html'
    
    # ------------------  filter name game --------------------------------
    # queryset = GameModel.objects.filter(name__contains="Halo")
    # queryset = GameModel.objects.filter(name__exact="Halo 4")
    # queryset = GameModel.objects.filter(name__in=["Halo 4", 'Pac-Man', 'Gears of War 2'])
    
    
    # ------------------ filter integer value -----------------------------
    # queryset = GameModel.objects.filter(na_sales__gt=10.5) # больше чем
    # queryset = GameModel.objects.filter(na_sales__gte=15.85) # больше или равно
    # queryset = GameModel.objects.filter(na_sales__lt=1.85) # меньше чем
    # queryset = GameModel.objects.filter(na_sales__lte=0.01) # меньше или равно

    
    # queryset = GameModel.objects.filter(name__startswith="Red") # наченается но ....
    # queryset = GameModel.objects.filter(name__endswith="4") # кончается на ....
    # queryset = GameModel.objects.filter(na_sales__range=range(2, 4)) # кончается на ....
    # queryset = GameModel.objects.filter(year__year=2016) # по дате год, месяц и день
    # queryset = GameModel.objects.filter(name__isnull=True) # выводит пустое значение
    # queryset = GameModel.objects.filter(name__regex=r'^(Star?|The) +') # фильтрация регулярным выражением


    # queryset = GameModel.objects.filter(
    #     Q(name__startswith="A") & Q(name__endswith="a") & Q(
    #         name__contains="ma"))

    # queryset = GameModel.objects.filter(Q(name__endswith="a"),
    #                                     name__startswith="A")

    # ----------------- Сложные запросы "Q" -----------------------
    
    # queryset = GameModel.objects.filter(
    #     Q(name__startswith="P") & Q(name__endswith="n") &
    #     Q(name__contains="Ma"))
    
    
    # queryset = GameModel.objects.filter(Q(name__endswith="n"),
    #                                     name__startswith="P")


    # queryset = GameModel.objects.filter(
    #     Q(name__startswith="Ab") | Q(name__startswith="Ad") | Q(
    #         name__startswith="Mat"))
    
    
    # queryset = GameModel.objects.filter(
    #     ~Q(name__startswith="Ab") | ~Q(name__startswith="Ad") | ~Q(
    #         name__startswith="Mat"))


def relation_filter_view(request):
    data = GamerLibraryModel.objects.filter(gamer__email__contains="a")
    print(data[0].gamer.email)
    # return HttpResponse(data)
    return HttpResponse(data.order_by("?"))


class ExcludeView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(platform__contains="X360")


class OrderByView(ListView):
    template_name = 'gamemodel_list.html'
    # TODO add reverse
    queryset = GameModel.objects.exclude().order_by('-year')


class AllView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.all()


class UnionView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name="Overwatch").union(
        GameModel.objects.filter(name="Fallout 4").union(
        GameModel.objects.filter(name="Project X Zone")))


class NoneView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.none()


class ValuesView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name="Fallout 4").values("name", "platform", "year")

    def get(self, request, *args, **kwargs):
        print(GameModel.objects.filter(name="Fallout 4").values("name", "platform", "year"))
        print(list(GameModel.objects.filter(name="Fallout 4").values_list("name", 'year')))
        return super().get(request, *args, **kwargs)


def date_view(request):
    data = GameModel.objects.dates(field_name='year', kind='year')
    print(data)
    return HttpResponse(data)


def get_view(request):
    # TODO try error
    data = GameModel.objects.get(id=270)
    print(data)
    return HttpResponse(data)


def create_view(request):
    # myself = GamerModel()
    # myself.email = "admin@admin.com"
    # myself.nickname = "SomeRandomNicknameSave"
    # myself.save()
    

    # myself = GamerModel(email="admin@admin.com", nickname="SomeRandomNicknameSave_2")
    # myself.save()
    
    
    # myself = GamerModel(**{"email": "admin@admin.com", "nickname": "SomeRandomNicknameSave_3"})
    # myself.save()

    # myself = GamerModel.objects.create(**{"email": "admin@admin.com",
    #                                       "nickname": "SomeRandomNicknameCreate_4"})
    # print(myself)
    

    # myself = GamerModel.objects.create(email="admin@admin.com",
    #                                    nickname="SomeRandomNicknameCreate_5")
    
    
    # myself = GamerModel.objects.bulk_create([
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameBulkCreate1_6"),
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameBulkCreate2_6"),
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameBulkCreate3_6"),
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameBulkCreate4_6")
    # ])


    # my_library = GamerLibraryModel(gamer=GamerModel.objects.get(pk=10), size=10)
    # my_library.save()
    # my_library.game.set([GameModel.objects.get(pk=1), GameModel.objects.get(pk=2)])


    # my_library = GamerLibraryModel.objects.create(gamer=GamerModel.objects.get(pk=10),size=10)
    # my_library.game.set([GameModel.objects.get(pk=1),GameModel.objects.get(pk=2)])

    # my_library = GamerLibraryModel.objects.bulk_create(
    #     [GamerLibraryModel(gamer=GamerModel.objects.get(pk=10),
    #                              size=10),
    #      GamerLibraryModel(gamer=GamerModel.objects.get(pk=10),
    #                        size=10)
    #      ])
    
    
    # my_friend = GamerModel.objects.get(pk=10)
    # my_friend.nickname = "My_friend"
    # my_friend.save()
    
    
    my_friend = GamerModel.objects.filter(pk=9)
    my_friend.update(nickname="MySecondNickname")
    
    
    # return HttpResponse(myself)
    # return HttpResponse(my_library)
    return HttpResponse(my_friend)
    
    
