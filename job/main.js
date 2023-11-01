import fs from "fs";
import request from "request";
import PDFParser from "pdf2json";

const pdfUrl = "https://www.porterco.org/DocumentCenter/View/15171/3-2022-General-Election-OFFICIAL-Summary";
const pdfParser = new PDFParser();

const pdfPipe = request({url: pdfUrl, encoding:null}).pipe(pdfParser.createParserStream());

pdfPipe.on("pdfParser_dataError", err => console.error(err) );
pdfPipe.on("pdfParser_dataReady", pdf => {
    let usedFieldsInTheDocument = pdfParser.getAllFieldsTypes();
    console.log(usedFieldsInTheDocument)
});
