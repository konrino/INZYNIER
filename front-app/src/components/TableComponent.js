import * as React from 'react';
import {DataGrid} from '@mui/x-data-grid';
import {useCallback, useEffect} from "react";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Container from "@mui/material/Container";
import Box from "@mui/material/Box";

const getDataDodania = (params) => {
    return `${params.row.data[0].data_dodania}`
}

const getWolumen = (params) => {
    return `${params.row.data[0].wolumen}`
}

const getKursOtw = (params) => {
    return `${params.row.data[0].kurs_otw}`
}

const getKursZamk = (params) => {
    return `${params.row.data[0].kurs_zamkn}`
}

const getObroty = (params) => {
    return `${params.row.data[0].obrot}`
}

const getTransakcje = (params) => {
    return `${params.row.data[0].liczba_trans}`
}

const columns = [
    {field: 'nazwa', headerName: 'Nazwa Spółki', width: 130},
    {
        field: 'DataNotowania', headerName: 'Data Notowania',
        valueGetter: getDataDodania,
        width: 130
    },
    {field: 'wolumen', headerName: 'Wolumen', width: 130, valueGetter: getWolumen},
    {field: 'obroty', headerName: 'Obrót', width: 130, valueGetter: getObroty},
    {field: 'transakcje', headerName: 'Liczba Transakcji', width: 200, valueGetter: getTransakcje},
    {field: 'kurs_otwarcia', headerName: 'Kurs Otwarcia', width: 180, valueGetter: getKursOtw},
    {field: 'kurs_zamkniecia', headerName: 'Kurs Zamknięcia', width: 180, valueGetter: getKursZamk},
];


export default function TableComponent() {

    const [kursy, setKursy] = React.useState();
    const [obrot, setObrot] = React.useState(999999999);
    const [obrotMin, setObrotMin] = React.useState(0);
    const [wolumen, setWolumen] = React.useState(999999999);
    const [wolumenMin, setWolumenMin] = React.useState(0);
    const [transakcje, setTransakcje] = React.useState(999999999);
    const [transakcjeMin, setTransakcjeMin] = React.useState(0);


    useEffect(() => {
        fetch(`http://localhost:5000/spolka-filter?wolumen_min=${wolumenMin}&wolumen_max=${wolumen}&obrot_min=${obrotMin}&obrot_max=${obrot}&liczba_trans_min=${transakcjeMin}&liczba_trans_max=${transakcje}`)
            .then(response => response.json())
            .then(data => {
                setKursy(data);
                console.log("COMPANIES", data);
            });
    }, []);

    const handleObrot = (value, maxOrNot) => {
        const correctValue = (value.target.value === '' || !value.target.value);
        if (maxOrNot) {
            setObrot(correctValue ? 999999999 : value.target.value);
        } else {
            setObrotMin(correctValue ? 0 : value.target.value)
        }
    }

    const handleTransakcje = (value, maxOrNot) => {
        const correctValue = (value.target.value === '' || !value.target.value);
        if (maxOrNot) {
            setTransakcje(correctValue ? 999999999 : value.target.value);
        } else {
            setTransakcjeMin(correctValue ? 0 : value.target.value)
        }
    }


    const handleWolumen = (value, maxOrNot) => {
        const correctValue = (value.target.value === '' || !value.target.value);
        if (maxOrNot) {
            setWolumen(correctValue ? 999999999 : value.target.value);
        } else {
            setWolumenMin(correctValue ? 0 : value.target.value)
        }
    }

    const search = useCallback(() => {
        fetch(`http://localhost:5000/spolka-filter?wolumen_min=${wolumenMin}&wolumen_max=${wolumen}&obrot_min=${obrotMin}&obrot_max=${obrot}&liczba_trans_min=${transakcjeMin}&liczba_trans_max=${transakcje}`)
            .then(response => response.json())
            .then(data => {
                setKursy(data);
                console.log("COMPANIES", data);
            });
    }, [wolumen, wolumenMin, obrot, obrotMin, transakcje, transakcjeMin]);

    return (
        <div style={{height: 400, width: '100%', marginTop: 80}}>
            <Box style={{display: 'flex', flexDirection: 'row',alignItems: 'center', justifyContent: 'center'}}>

                <Box style={{
                    display: 'flex',
                    flexDirection: 'column',
                    paddingTop: '15px',
                    paddingBottom: '15px',
                    maxWidth: "200px",
                    marginRight: '15px'
                }}>
                    <TextField placeholder={'Obrót MAX'} onChange={(newValue) => handleObrot(newValue, true)}/>
                    <TextField style={{paddingTop: '10px'}} placeholder={'Obrót MIN '}
                               onChange={(newValue) => handleObrot(newValue, false)}/>
                </Box>

                <Box style={{
                    display: 'flex',
                    flexDirection: 'column',
                    paddingTop: '15px',
                    paddingBottom: '15px',
                    maxWidth: "200px",
                    marginRight: '15px'
                }}>
                    <TextField placeholder={'Wolumen MAX'} onChange={(newValue) => handleWolumen(newValue, true)}/>
                    <TextField style={{paddingTop: '10px'}} placeholder={'Wolumen MIN'}
                               onChange={(newValue) => handleWolumen(newValue, false)}/>
                </Box>

                <Box style={{
                    display: 'flex',
                    flexDirection: 'column',
                    paddingTop: '15px',
                    paddingBottom: '15px',
                    maxWidth: "200px"
                }}>
                    <TextField placeholder={'Liczba Transakcji MAX'}
                               onChange={(newValue) => handleTransakcje(newValue, true)}/>
                    <TextField style={{paddingTop: '10px'}} placeholder={'Liczba Transakcji MIN'}
                               onChange={(newValue) => handleTransakcje(newValue, false)}/>
                </Box>
                <Box style={{
                        display: 'flex',
                        flexDirection: 'column',
                        paddingTop: '15px',
                        paddingBottom: '15px',
                        maxWidth: "200px"
                    }}>
                        <Button style={{marginLeft: '15px', minWidth: '120px', minHeight: '120px'}} variant="contained"
                                onClick={search}>Szukaj</Button>
                </Box>
            </Box>


            <DataGrid
                rows={kursy}
                columns={columns}
                pageSize={20}
                rowsPerPageOptions={[]}
                checkboxSelection
            />
        </div>
    );
}
