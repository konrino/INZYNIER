package com.inzynier;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.poi.ss.usermodel.*;

import java.io.*;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Main {

    public static void main(String[] args) {
        try {
            Main.readFile();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void readFile() throws IOException {
        for (int j = 1; j < 30; j++) {
            String file = "akcje ("+j+").xls";
            try (InputStream inp = new FileInputStream("akcje/" + file)
            ) {
                Workbook wb = WorkbookFactory.create(inp);
                ObjectMapper mapper = new ObjectMapper();
                Sheet sheet = wb.getSheetAt(0);
                for (int i = 0; i < sheet.getLastRowNum(); i++) {
                    Row row = sheet.getRow(i + 1);
                    KursDTO kursDTO = prepareDTO(row);
                    HttpClient client = HttpClient.newHttpClient();
                    HttpRequest request = HttpRequest.newBuilder()
                            .uri(URI.create("http://localhost:5000/kursy"))
                            .header("Content-Type", "application/json")
                            .POST(HttpRequest.BodyPublishers.ofString(mapper.writeValueAsString(kursDTO)))
                            .build();
                    client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
                            .thenApply(HttpResponse::body)
                            .thenAccept(System.out::println)
                            .join();
                }

            }
            catch (Exception exception){
                exception.printStackTrace();
                continue;
            }
        }
    }

    public static KursDTO prepareDTO(Row row) {
        KursDTO kursDTO = new KursDTO();
        Cell date = row.getCell(0);
        Cell name = row.getCell(1);
        Cell currency = row.getCell(3);
        Cell kursOtw = row.getCell(4);
        Cell kursMax = row.getCell(5);
        Cell kursMin = row.getCell(6);
        Cell kursZam = row.getCell(7);
        Cell wolumen = row.getCell(9);
        Cell transakcje = row.getCell(10);
        Cell obrot = row.getCell(11);


        kursDTO.setData_dodania(date.getStringCellValue());
        kursDTO.setNazwa(name.getStringCellValue());
        kursDTO.setWaluta(currency.getStringCellValue());
        kursDTO.setKurs_otw(kursOtw.getNumericCellValue());
        kursDTO.setKurs_max(kursMax.getNumericCellValue());
        kursDTO.setKurs_min(kursMin.getNumericCellValue());
        kursDTO.setKurs_zamkn(kursZam.getNumericCellValue());
        kursDTO.setWolumen(wolumen.getNumericCellValue());
        kursDTO.setLiczba_trans(transakcje.getNumericCellValue());
        kursDTO.setObrot(obrot.getNumericCellValue());
        return kursDTO;
    }


}

// C:\Users\Admin\INŻYNIER\proxy\dane.xls