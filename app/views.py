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

    nazwa = request.json['nazwa']
    waluta = request.json['waluta']

    if Spolka.query.filter_by(nazwa=nazwa).first():
        spolka = Spolka.query.filter_by(nazwa=nazwa).first()
        nowy_kurs = Kursy(data_dodania,kurs_otw,kurs_max,kurs_min,kurs_zamkn,liczba_trans,obrot, spolka.id)
        save_entity(nowy_kurs)

        return json.dumps(nowy_kurs, cls=AlchemyEncoder)

    nowa_spolka = Spolka(nazwa, waluta)
    save_entity(nowa_spolka)
    nowy_kurs = Kursy(data_dodania,kurs_otw,kurs_max,kurs_min,kurs_zamkn,
                      liczba_trans,obrot, Spolka.query.filter_by(nazwa=nazwa).first().id)
    save_entity(nowy_kurs)

    return json.dumps(nowy_kurs, cls=AlchemyEncoder)


@basic_page.route('/kursy-get', methods=['GET'])
def get_kursy():
    from app.models import Kursy
    from app.models import AlchemyEncoder
    return json.dumps(Kursy.query.all(), cls=AlchemyEncoder)


@basic_page.route('/oblicz', methods=['POST'])
def oblicz_spolka():
    spolka_a = request.json['spolka_a']
    spolka_b = request.json['spolka_b']
    from_date = request.json['od_data']


    from app.models import Spolka, Kursy
    from app.models import AlchemyEncoder
    return json.dumps(Kursy.query.filter(Kursy.sp_id == Spolka.query.filter_by(nazwa=spolka_a).first().id).filter(Kursy.data_dodania >= datetime.date.fromisoformat(from_date)).all(), cls=AlchemyEncoder)

@basic_page.route('/oblicz2', methods=['POST'])
def wyszukiwanie():
    spolka_a = request.json['spolka_a']
    spolka_b = request.json['spolka_b']
    from_obrot = request.json['od_obrotu']


    from app.models import Spolka, Kursy
    from app.models import AlchemyEncoder
    return json.dumps(Kursy.query.filter(Kursy.sp_id == Spolka.query.filter_by(nazwa=spolka_a).first().id).filter(Kursy.obrot >= float(from_obrot)).all(), cls=AlchemyEncoder)
