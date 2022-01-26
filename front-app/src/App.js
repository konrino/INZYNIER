import { Routes, Route, Link } from "react-router-dom";
import AppBarComponent from "./components/AppBarComponent";
import TableComponent from "./components/TableComponent";
import AccordionComponent from "./components/AccordionComponent";
import Container from "@mui/material/Container";
import RoiComponent from "./components/RoiComponent";
import Open from "./components/home/Open";
import {createTheme, ThemeProvider} from "@mui/material/styles";


const theme = createTheme({
    palette:{
        primary:{
            main: '#52B5A7',
            contrastText: '#ffffff'
        },
        text: {
            primary: '#000000',
        },
    },
})

function Home() {

    return (
        <div>
            <Open/>
        </div>
    );
}

function FAQ() {
    return (
    <>
        <AccordionComponent/>

    </>
    );
}

function Oblicz() {
    return (
        <>
             <RoiComponent/>
        </>
    );
}

function Filtruj() {
    return (
        <>
            <TableComponent/>

        </>
    );
}


function Kontakt() {
    return (
        <>
            <Container style={{maxWidth: '700px', marginTop:'80px'}}>
                <h2 style={{textDecoration: 'underline'}}>Kontakt</h2>
            </Container>
            <Container style={{maxWidth: '600px', marginTop:'50px'}}>
                <p>Kontakt z autorem aplikacji jest możliwy pod podanym adresem email: </p>
                <p>Konrino@gmail.com</p>
                <p>lub pod numerem telefonu:</p>
                <p>+48 533 247 500</p>
            </Container>
        </>
    );
}


function App() {
  return (
      <ThemeProvider theme={theme}>
    <div className="App">
      <AppBarComponent/>
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="FAQ" element={<FAQ />} />
            <Route path="Oblicz" element={<Oblicz />} />
            <Route path="Filtruj" element={<Filtruj />} />
            <Route path="Kontakt" element={<Kontakt />} />
        </Routes>
    </div>
      </ThemeProvider>
  );

}

export default App;
