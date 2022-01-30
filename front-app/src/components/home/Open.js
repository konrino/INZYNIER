import React from "react";
import '../home/HomeView.css';
import logo from '../../assets/obrazek (4).jpg';
import contact from '../../assets/obrazek (1).jpg';
import AOS from 'aos';
import 'aos/dist/aos.css';
import CountUp from 'react-countup';
import VisibilitySensor from 'react-visibility-sensor';

AOS.init({
    disable: false,
    startEvent: 'DOMContentLoaded',
    initClassName: 'aos-init',
    animatedClassName: 'aos-animate',
    useClassNames: false,
    disableMutationObserver: false,
    debounceDelay: 50,
    throttleDelay: 99,



    offset: 120,
    delay: 0,
    duration: 400,
    easing: 'ease',
    once: false,
    mirror: false,
    anchorPlacement: 'top-bottom',

});

export default function Open()
{

    return(
        <>
            <section className="open">
                <h1 className="open__text">
                    APLIKACJA WSPOMAGAJĄCA INWESTOWANIE
                </h1>
            </section>
            <section className="aboutAplication">
                <div className="aboutTile">
                    <p className="textTile aplicationText">Główny Urząd Statystyczny oświadczył, że inflacja średnioroczna w Polsce w 2021 roku wyniosła, aż 5.1%.
                        Jest to największy odnotowany wynik w XXI wieku. Można więc śmiało stwierdzić, że wiele ludzi martwi się o swój majątek, który nie jest zainwestowany w żaden sposób.
                        Wśród społeczeństwa panuje przekonanie, iż giełda jest na tyle złożona i zagmatwana, że nie warto się nią interesować.
                        Aplikacja ma na celu wspomóc nowych inwestorów poprzez udostępnienie narzędzia, które umożliwia obliczenie prostej stopy zwrotu "ROI". Ponadto użytkownik może zobaczyć historyczne notowania spółek w zakładce "Filtruj"</p>
                </div>
                <div className="aboutTile">
                    <img className="tileImage firstImage" data-aos="fade-left" src={logo} width={100 + "%"} height={"auto"} alt="Cash"/>
                </div>
            </section>
            <section className="aboutMe_container">
                <div className="aboutMe_kafel">
                    <p className="aboutMe_count">
                        <CountUp end={8} redraw={true}>
                            {({ countUpRef, start }) => (
                                <VisibilitySensor onChange={start} delayedCall>
                                    <span ref={countUpRef} />
                                </VisibilitySensor>
                            )}
                        </CountUp>
                    </p>
                    <p className="aboutMe_desc">
                        Użytych technologii
                    </p>
                </div>
                <div className="aboutMe_kafel">
                    <p className="aboutMe_count">
                        <CountUp end={430} redraw={true}>
                            {({ countUpRef, start }) => (
                                <VisibilitySensor onChange={start} delayedCall>
                                    <span ref={countUpRef} />
                                </VisibilitySensor>
                            )}
                        </CountUp>
                    </p>
                    <p className="aboutMe_desc">
                         Dostępnych spółek
                    </p>
                </div>
                <div className="aboutMe_kafel">
                    <p className="aboutMe_count">
                        <CountUp end={140} redraw={true}>
                            {({ countUpRef, start }) => (
                                <VisibilitySensor onChange={start} delayedCall>
                                    <span ref={countUpRef} />
                                </VisibilitySensor>
                            )}
                        </CountUp>
                    </p>
                    <p className="aboutMe_desc">
                        Zadowolonych użytkowników
                    </p>
                </div>
            </section>
            <section className="aboutAplication contactCorrection">
                <div className="aboutTile contactImage" data-aos="fade-right">
                    <img className="tileImage" src={contact} width={100 + "%"} height={"auto"} alt="Cash"/>
                </div>
                <div className="aboutTile" style={{lineHeight: "3rem"}}>
                    <div className="textTile">
                        <h1>Kontakt</h1>
                        <p>Konrino@gmail.com<br></br>

                            lub pod numerem telefonu:<br></br>

                            +48 533 247 500</p>
                    </div>
                </div>
            </section>
        </>
    );
}
