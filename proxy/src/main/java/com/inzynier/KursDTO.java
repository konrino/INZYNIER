package com.inzynier;

public class KursDTO {

//zdefiniowane obiekty transferowe - przesyla je aplikacja do bazy danych
    private String data_dodania;
    private String nazwa;
    private String waluta;
    private double kurs_otw;
    private double kurs_max;
    private double kurs_zamkn;
    private double kurs_min;
    private double liczba_trans;
    private double obrot;
    private double wolumen;


    public String getData_dodania() {
        return data_dodania;
    }

    public void setData_dodania(String data_dodania) {
        this.data_dodania = data_dodania;
    }

    public String getNazwa() {
        return nazwa;
    }

    public void setNazwa(String nazwa) {
        this.nazwa = nazwa;
    }

    public String getWaluta() {
        return waluta;
    }

    public void setWaluta(String waluta) {
        this.waluta = waluta;
    }

    public double getKurs_otw() {
        return kurs_otw;
    }

    public void setKurs_otw(double kurs_otw) {
        this.kurs_otw = kurs_otw;
    }

    public double getKurs_max() {
        return kurs_max;
    }

    public void setKurs_max(double kurs_max) {
        this.kurs_max = kurs_max;
    }

    public double getKurs_zamkn() {
        return kurs_zamkn;
    }

    public void setKurs_zamkn(double kurs_zamkn) {
        this.kurs_zamkn = kurs_zamkn;
    }

    public double getKurs_min() {
        return kurs_min;
    }

    public void setKurs_min(double kurs_min) {
        this.kurs_min = kurs_min;
    }

    public double getLiczba_trans() {
        return liczba_trans;
    }

    public void setLiczba_trans(double liczba_trans) {
        this.liczba_trans = liczba_trans;
    }

    public double getObrot() {
        return obrot;
    }

    public void setObrot(double obrot) {
        this.obrot = obrot;
    }

    public double getWolumen() {
        return wolumen;
    }

    public void setWolumen(double wolumen) {
        this.wolumen = wolumen;
    }
}
