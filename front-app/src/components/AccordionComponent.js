import * as React from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';

export default function AccordionComponent() {
    return (
        <div>
            <Accordion>
                <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel1a-content"
                    id="panel1a-header"
                >
                    <Typography>Co umożliwia aplikacja?</Typography>
                </AccordionSummary>
                <AccordionDetails>
                    <Typography>
                        Aplikacja umożliwia obliczenie prostej stopy zwrotu ROI (ang. Return of investment). Użytkownik może również filtrować dane dostępne w bazie danych. Istnieją trzy dostępne filtry:
                        obrót, wolumen, liczba transakcji
                    </Typography>
                </AccordionDetails>
            </Accordion>
            <Accordion>
                <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel2a-content"
                    id="panel2a-header"
                >
                    <Typography>Jak aplikacja oblicza rentowność danej spółki?</Typography>
                </AccordionSummary>
                <AccordionDetails>
                    <Typography>
                        Aplikacja oblicza rentowność przy użyciu Roi. Roi jest oceną zwrotu nakładów inwestycyjnych w dany instrument giełdowy.
                        W przypadku tej aplikacji instrumentami giełdowymi bedą spółki akcyjne dostępne na Giełdzie Papierów Wartościowych w warszawie. Zwrot z inwestycji jest opisany wzorem: ROI = Zysk Operacyjny opodatkowany/Całkowite nakłady inwestycyjne * 100%
                        <p>Jeśli ROI jest dodatnie oznacza to, że zainwestowany kapitał przyniósł zysk, jeśli jest ujemny oznacza to, że inwestor stracił pieniądze</p>
                    </Typography>
                </AccordionDetails>
            </Accordion>
            <Accordion>
                <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel2a-content"
                    id="panel2a-header"
                >
                    <Typography>Czy mogę zobaczyć notowania z dzisiaj?</Typography>
                </AccordionSummary>
                <AccordionDetails>
                    <Typography>
                       Nie jest to możliwe ze względu na brak przynależności autora aplikacji do domu maklreskiego. Jest to obowiązek aby otrzymać API odpowiedzialne za dostarczenie danych "na żywo".
                    </Typography>
                </AccordionDetails>
            </Accordion>
            <Accordion>
                <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel2a-content"
                    id="panel2a-header"
                >
                    <Typography>Skąd pochodzą dane?</Typography>
                </AccordionSummary>
                <AccordionDetails>
                    <Typography>
                        Baza danych została uzupełniona arkuszami kalkulacyjnymi pochodzącymi z głównej strony internetowej Giełdy Papierów Wartościowych w Warszawie (www.gpw.pl). Dane zawierają historyczne notowania spółek akcyjnych.
                    </Typography>
                </AccordionDetails>
            </Accordion>
            <Accordion>
                <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel2a-content"
                    id="panel2a-header"
                >
                    <Typography>Przy użyciu jakich technologii została stworzona aplikacja?</Typography>
                </AccordionSummary>
                <AccordionDetails>
                    <Typography>
                       Aplikacja została stworzona przy użyciu: Javy, Pythona, Reacta, SQLAlchemy, Flaska
                    </Typography>
                </AccordionDetails>
            </Accordion>
            <Accordion>
                <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel2a-content"
                    id="panel2a-header"
                >
                    <Typography>Czy planujesz rozbudowywać aplikację?</Typography>
                </AccordionSummary>
                <AccordionDetails>
                    <Typography>
                        Tak. Autor przeanalizował już najważniejsze funkcje rozwojowe, które powinnny zostać zaimplementowane.
                    </Typography>
                </AccordionDetails>
            </Accordion>
        </div>
    );
}