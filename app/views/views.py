import datetime
import itertools
import json
import random

from flask import request, Blueprint
from flask_cors import cross_origin


basic_page = Blueprint('simple_page', __name__)

#deklarowanie endpointow

#zwrocenie wartosci zapisanych w bazie danych po danej nazwie np ORLEN
@basic_page.route('/spolka-get', methods=['GET'])
@cross_origin()
def get_spolka():
    from app.models.models import Spolka, Kursy
    from app.models.models import AlchemyEncoder

    nazwa = request.args.get('nazwa')
    return json.dumps(Kursy.query.filter(Kursy.sp_id == Spolka.query.filter_by(nazwa=nazwa).first().id).all(), cls=AlchemyEncoder)

#zapisanie danych do bazy danych (wykorzystywane w postmanie)

@basic_page.route('/spolka-get-nazwy', methods=['GET'])
@cross_origin()
def get_spolka_all():
    from app.models.models import Spolka, Kursy
    from app.models.models import AlchemyEncoder

    companies = Spolka.query.all()
    companies_to_dump = [{'label': splk.nazwa, 'data': splk} for splk in companies]
    return json.dumps(companies_to_dump, cls=AlchemyEncoder)


@basic_page.route('/spolka-filter', methods=['GET'])
@cross_origin()
def get_spolka_by_filter():
    from app.models.models import Spolka, Kursy
    from app.models.models import AlchemyEncoder

    obrot_max_value = 999999999
    obrot_min_value = 0
    wolumen_max_value = 999999999
    wolumen_min_value = 0
    liczba_trans_max_value = 999999999
    liczba_trans_min_value = 0

    obrot_max = obrot_max_value if request.args.get('obrot_max') is None else request.args.get('obrot_max')
    obrot_min = obrot_min_value if request.args.get('obrot_min') is None else request.args.get('obrot_min')
    wolumen_max = wolumen_max_value if request.args.get('wolumen_max') is None else request.args.get('wolumen_max')
    wolumen_min = wolumen_min_value if request.args.get('wolumen_min') is None else request.args.get('wolumen_min')
    liczba_trans_max = liczba_trans_max_value if request.args.get('liczba_trans_max') is None else request.args.get('liczba_trans_max')
    liczba_trans_min = liczba_trans_min_value if request.args.get('liczba_trans_min') is None else request.args.get('liczba_trans_min')

    key_func = lambda x: x.sp_id
    data_kursy = Kursy.query.filter(obrot_min <= Kursy.obrot, Kursy.obrot <= obrot_max,
                                    Kursy.wolumen <= wolumen_max, wolumen_min <= Kursy.wolumen,
                                    liczba_trans_min <= Kursy.liczba_trans, Kursy.liczba_trans <= liczba_trans_max
                                    ).all()
    data_to_dump = []
    a = 1
    for key, group in itertools.groupby(data_kursy, key_func):
        key_value = Spolka.query.filter_by(id=key).first()
        data_to_dump.append({'id': a, 'nazwa': key_value.nazwa, 'data': list(group)})
        a = a + 1

    print(data_to_dump)
    return json.dumps(data_to_dump, cls=AlchemyEncoder)


@basic_page.route('/spolka-filter/analiza', methods=['GET'])
@cross_origin()
def get_spolka_by_filter_analiza():
    from app.models.models import Spolka, Kursy
    from app.models.models import AlchemyEncoder

    spolka_nazywa = request.args.get('spolka_nazwa')
    inwestycja = request.args.get('inwestycja')
    data_od = request.args.get('data_od')
    data_do = request.args.get('data_do')

    kurs_do = Kursy.query.filter(Kursy.data_dodania == datetime.date.fromisoformat(data_do),
                                 Kursy.sp_id == Spolka.query.filter_by(nazwa=spolka_nazywa).first().id).first().kurs_max
    kurs_od = Kursy.query.filter(Kursy.data_dodania == datetime.date.fromisoformat(data_od),
                                 Kursy.sp_id == Spolka.query.filter_by(nazwa=spolka_nazywa).first().id).first().kurs_max
    kursy_od_do = Kursy.query.filter(Kursy.data_dodania >= datetime.date.fromisoformat(data_od),
                                     Kursy.data_dodania <= datetime.date.fromisoformat(data_do),
                                 Kursy.sp_id == Spolka.query.filter_by(nazwa=spolka_nazywa).first().id).all()

    early_invest = kurs_od * float(inwestycja)
    late_invest = kurs_do * float(inwestycja)
    print(early_invest, late_invest)
    roi = (((late_invest - early_invest) / float(inwestycja)) * 100) / 100

    highest_kurs = [{'kurs': krs.kurs_max, 'data_dodania': krs.data_dodania} for krs in kursy_od_do]

    highest_kurs_value = max(highest_kurs, key=lambda i: i['kurs'])

    return json.dumps({"roi": str(roi)+'%', "spolka": spolka_nazywa, "kurs_max": highest_kurs_value.get('kurs'), 'data_dodania_max': highest_kurs_value.get('data_dodania').strftime('%m/%d/%Y')}, cls=AlchemyEncoder)


@basic_page.route('/kursy', methods=['POST'])
def add_kurs():
    from app.models.models import AlchemyEncoder
    from app.models.models import save_entity
    from app.models.models import Spolka, Kursy

    data_dodania = request.json['data_dodania']
    kurs_otw = request.json['kurs_otw']
    kurs_max = request.json['kurs_max']
    kurs_min = request.json['kurs_min']
    kurs_zamkn = request.json['kurs_zamkn']
    liczba_trans = request.json['liczba_trans']
    obrot = request.json['obrot']
    wolumen = request.json["wolumen"]

    nazwa = request.json['nazwa']
    waluta = request.json['waluta']

    if Spolka.query.filter_by(nazwa=nazwa).first():
        spolka = Spolka.query.filter_by(nazwa=nazwa).first()
        nowy_kurs = Kursy(data_dodania,kurs_otw,kurs_max,kurs_min,kurs_zamkn,liczba_trans,wolumen,obrot,spolka.id)
        save_entity(nowy_kurs)

        return json.dumps(nowy_kurs, cls=AlchemyEncoder)

    nowa_spolka = Spolka(nazwa, waluta)
    save_entity(nowa_spolka)
    nowy_kurs = Kursy(data_dodania,kurs_otw,kurs_max,kurs_min,kurs_zamkn,
                      liczba_trans,wolumen,obrot, Spolka.query.filter_by(nazwa=nazwa).first().id)
    save_entity(nowy_kurs)

    return json.dumps(nowy_kurs, cls=AlchemyEncoder)

#zwrocenie wszystkich kursow

@basic_page.route('/kursy-get', methods=['GET'])
@cross_origin()
def get_kursy():
    from app.models.models import Kursy
    from app.models.models import AlchemyEncoder
    return json.dumps(Kursy.query.all(), cls=AlchemyEncoder)

#Zwrocenie spolek z danego dnia
@basic_page.route('/oblicz', methods=['POST'])
@cross_origin()
def wyszukiwanie_data():
    spolka_a = request.json['spolka_a']
    from_date = request.json['od_data']


    from app.models.models import Spolka, Kursy
    from app.models.models import AlchemyEncoder
    return json.dumps(Kursy.query.filter(Kursy.sp_id == Spolka.query.filter_by(nazwa=spolka_a).first().id).filter(Kursy.data_dodania >= datetime.date.fromisoformat(from_date)).all(), cls=AlchemyEncoder)


# #Wstepna analiza rentownosci - ktora bedzie poszerzona o inne funkjconalnosci
#
# @basic_page.route('/analiza', methods=['POST'])
# @cross_origin()
# def rentownosc():
#     from app.models.models import Spolka, Kursy
#     from app.models.models import AlchemyEncoder
#     from functools import reduce
#     import itertools
#     import operator
#
#
#
#     spolka_a = request.json['spolka_a']
#     from_data = request.json['from_data']
#     to_data = request.json['to_data']
#
#
#     myset = set()
#     myset1 = set()
#
#     while True:
#         try:
#             a = random.randint(1, 31)
#             data = datetime.date(2021, datetime.datetime.fromisoformat(from_data).month, a)
#             if data.weekday() < 5:
#                 myset.add(data)
#             if len(myset) > 4:
#                 break
#         except:
#             print("")
#
#     for d in myset:
#         for i in range(0, 2):
#             data1 = datetime.date(d.year, d.month - i, d.day)
#             myset1.add(data1)
#
#     print(myset1)
#
#     kursy = Kursy.query.filter(Kursy.sp_id == Spolka.query.filter_by(nazwa=spolka_a).first().id) \
#         .filter(Kursy.data_dodania.in_(myset1)).all()
#
#     get_date = operator.attrgetter('data_dodania')
#     kursy_by_date = [list(g) for k, g in itertools.groupby(sorted(kursy,
#                                                                   key=lambda x: x.data_dodania.day), lambda x: x.data_dodania.day)]
#     data = [[{'date': k.data_dodania, 'kurs': k.kurs_min} for k in x] for x in kursy_by_date]
#     calculated_data = []
#     for set_date in data:
#         set_date.sort(key=lambda x: x['date'])
#         calculate = reduce((lambda x, y: x['kurs'] - y['kurs']), set_date)
#         if isinstance(calculate, dict):
#             calculate = 0
#
#         calculated_data.append({'value': calculate, 'data': [{'kurs': x['kurs'], 'data': str(x['date'])} for x in set_date]})
#
#     return json.dumps(calculated_data, cls=AlchemyEncoder)
