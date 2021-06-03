import datetime
import json

from flask import request, Blueprint


basic_page = Blueprint('simple_page', __name__)


@basic_page.route('/spolka-get', methods=['GET'])
def get_spolka():
    from app.models import Spolka, Kursy
    from app.models import AlchemyEncoder

    nazwa = request.args.get('nazwa')
    return json.dumps(Kursy.query.filter(Kursy.sp_id == Spolka.query.filter_by(nazwa=nazwa).first().id).all(), cls=AlchemyEncoder)


@basic_page.route('/kursy', methods=['POST'])
def add_kurs():
    from app.models import AlchemyEncoder
    from app.models import save_entity
    from app.models import Spolka, Kursy

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
        nowy_kurs = Kursy(data_dodania,kurs_otw,kurs_max,kurs_min,kurs_zamkn,liczba_trans,wolumen,obrot, spolka.id)
        save_entity(nowy_kurs)

        return json.dumps(nowy_kurs, cls=AlchemyEncoder)

    nowa_spolka = Spolka(nazwa, waluta)
    save_entity(nowa_spolka)
    nowy_kurs = Kursy(data_dodania,kurs_otw,kurs_max,kurs_min,kurs_zamkn,
                      liczba_trans,wolumen,obrot, Spolka.query.filter_by(nazwa=nazwa).first().id)
    save_entity(nowy_kurs)

    return json.dumps(nowy_kurs, cls=AlchemyEncoder)


@basic_page.route('/kursy-get', methods=['GET'])
def get_kursy():
    from app.models import Kursy
    from app.models import AlchemyEncoder
    return json.dumps(Kursy.query.all(), cls=AlchemyEncoder)


@basic_page.route('/oblicz', methods=['POST'])
def wyszukiwanie_data():
    spolka_a = request.json['spolka_a']
    spolka_b = request.json['spolka_b']
    from_date = request.json['od_data']


    from app.models import Spolka, Kursy
    from app.models import AlchemyEncoder
    return json.dumps(Kursy.query.filter(Kursy.sp_id == Spolka.query.filter_by(nazwa=spolka_a).first().id).filter(Kursy.data_dodania >= datetime.date.fromisoformat(from_date)).all(), cls=AlchemyEncoder)


@basic_page.route('/oblicz2', methods=['POST'])
def wyszukiwanie_obrot():
    spolka_a = request.json['spolka_a']
    spolka_b = request.json['spolka_b']
    from_obrot = request.json['od_obrotu']


    from app.models import Spolka, Kursy
    from app.models import AlchemyEncoder
    return json.dumps(Kursy.query.filter(Kursy.sp_id == Spolka.query.filter_by(nazwa=spolka_a).first().id).filter(Kursy.obrot >= float(from_obrot)).all(), cls=AlchemyEncoder)

@basic_page.route('/oblicz3', methods=['POST'])
def wyszukiwanie_wolumen():
    spolka_a = request.json['spolka_a']
    spolka_b = request.json['spolka_b']
    from_wolumen = request.json['od_wolumen']


    from app.models import Spolka, Kursy
    from app.models import AlchemyEncoder
    return json.dumps(Kursy.query.filter(Kursy.sp_id == Spolka.query.filter_by(nazwa=spolka_a).first().id).filter(Kursy.wolumen >= float(from_wolumen)).all(), cls=AlchemyEncoder)

@basic_page.route('/oblicz4', methods=['POST'])
def wyszukiwanie_trans():
    spolka_a = request.json['spolka_a']
    spolka_b = request.json['spolka_b']
    from_liczba_trans = request.json['od_trans']


    from app.models import Spolka, Kursy
    from app.models import AlchemyEncoder
    return json.dumps(Kursy.query.filter(Kursy.sp_id == Spolka.query.filter_by(nazwa=spolka_a).first().id).filter(Kursy.liczba_trans >= float(from_liczba_trans)).all(), cls=AlchemyEncoder)

@basic_page.route('/oblicz5', methods=['POST'])
def wyszukiwanie_kurs_otw():
    spolka_a = request.json['spolka_a']
    spolka_b = request.json['spolka_b']
    from_kurs_otw = request.json['od_kurs_otw']


    from app.models import Spolka, Kursy
    from app.models import AlchemyEncoder
    return json.dumps(Kursy.query.filter(Kursy.sp_id == Spolka.query.filter_by(nazwa=spolka_a).first().id).filter(Kursy.liczba_trans >= float(from_kurs_otw)).all(), cls=AlchemyEncoder)