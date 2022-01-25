import * as React from 'react';
import TextField from '@mui/material/TextField';
import {DatePicker, LocalizationProvider} from "@mui/lab";
import AdapterDateFns from '@mui/lab/AdapterDateFns';
import Container from "@mui/material/Container";
import {useCallback, useEffect} from "react";
import Autocomplete from "@mui/material/Autocomplete";
import Button from "@mui/material/Button";

const FromDatePicker = (callback) => {
    const [value, setValue] = React.useState(null);

    return (
        <LocalizationProvider dateAdapter={AdapterDateFns}>
            <DatePicker
                label="Data od"
                value={value}
                onChange={(newValue) => {
                    setValue(newValue);
                    callback.callback(newValue);
                }}
                renderInput={(params) => <TextField {...params} />}
            />
        </LocalizationProvider>
    );
}

const ToDatePicker = (callback) => {
    const [value, setValue] = React.useState(null);
    console.log("CALLBACK", callback);
    return (
        <LocalizationProvider dateAdapter={AdapterDateFns}>
            <DatePicker
                label="Data do"
                value={value}
                onChange={(newValue) => {
                  setValue(newValue);
                  callback.callback(newValue);
                }}
                renderInput={(params) => <TextField {...params} />}
            />
        </LocalizationProvider>
    );
}

export default function RoiComponent() {
    const [fromDate, setFromDate] = React.useState(null);
    const [toDate, setToDate] = React.useState(null);
    const [invest, setInvest] = React.useState('');
    const [companies, setCompanies] = React.useState([]);
    const [selectedCompany, setSelectedCompany] = React.useState();
    const [roi, setRoi] = React.useState();


    useEffect(() => {
        fetch('http://localhost:5000/spolka-get-nazwy')
            .then(response => response.json())
            .then(data => {
                setCompanies(data);
                console.log("COMPANIES", data);
            })
    }, []);

    const setFromDateHandle = useCallback((date) => {
        setFromDate(date);
    }, []);

    const setToDateHandle = useCallback((date) => {
        setToDate(date);
    }, []);

    const handleChange = (e) => {
        const re = /^[0-9\b]+$/;
        if (e.target.value === '' || re.test(e.target.value)) {
            setInvest(e.target.value);
        }
    }

    const roiLogic = useCallback(() => {
        const toDateQuery = toDate.toISOString().split("T")[0];
         const fromDateQuery = fromDate.toISOString().split("T")[0];
        fetch(`http://localhost:5000/spolka-filter/analiza?spolka_nazwa=${selectedCompany.label}&inwestycja=${invest}&data_od=${fromDateQuery}&data_do=${toDateQuery}`)
            .then(response => response.json())
            .then(data => {
                setRoi(data);
                console.log("ROI", data);
            })
    }, [selectedCompany, invest, toDate, fromDate]);

    return (
        <Container style={{display: 'flex', flexDirection: 'column'}}>
            <Container style={{display: 'flex', flexDirection: 'row', padding: '50px'}}>
                <Autocomplete
                    disablePortal
                    id="combo-box-demo"
                    options={companies}
                    sx={{ width: 300 }}
                    onChange={(event, companyData) => {
                        setSelectedCompany(companyData);
                        console.log("SET COMPANY", companyData);
                    }}
                    renderInput={(params) => <TextField {...params} label="Spolka" />}
                />
                <FromDatePicker callback={setFromDateHandle}/>
                <ToDatePicker callback={setToDateHandle}/>
                <TextField placeholder={'kwota w zł'} value={invest} onChange={(newValue) => handleChange(newValue)}/>
                <Button style={{marginLeft:'15px', minWidth:'150px'}} variant="contained" onClick={roiLogic}>Oblicz Roi</Button>
            </Container>
            <h3 style={{textAlign:"left"}}> Współczynnik Roi dla inwestycji wynosi: {roi?.roi}</h3>
            <h3 style={{textAlign:"left"}}> Inwestycja wyniosła {Number(invest) + Number(((invest) * Number(roi?.roi.split('%')[0])/100))} zł</h3>
            <h3 style={{textAlign:"left"}}>Inwestycja wyniosła największą wartość w dniu:  {roi?.data_dodania_max} Kiedy kurs max wyniósł: {roi?.kurs_max}</h3>
        </Container>
    );

}

