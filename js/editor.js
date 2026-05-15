const HEADER=`Rectoría | Universidad Nacional de Colombia<br>Bogotá D.C.<br>${new Date().toISOString().slice(0,10)}`;
const FOOTER=`Carrera 45 # 26-85 – Edificio Uriel Gutiérrez Piso 5<br>(+57 1) 3165469 – rectoriaun@unal.edu.co<br>Bogotá, D.C., Colombia`;
document.getElementById('headerBlock').innerHTML=HEADER;document.getElementById('footerBlock').innerHTML=FOOTER;
const quill=new Quill('#editor',{theme:'snow'});
const p=new URLSearchParams(location.search),cat=p.get('cat'),file=p.get('file');
fetch(`${cat}/${file}`).then(r=>r.arrayBuffer()).then(buf=>mammoth.convertToHtml({arrayBuffer:buf})).then(r=>quill.clipboard.dangerouslyPasteHTML(r.value)).catch(()=>quill.setText('Documento no legible en demo.'));

document.getElementById('downloadBtn').onclick=()=>{const {Document,Packer,Paragraph,TextRun}=docx;const lines=quill.getText().split('\n').filter(Boolean);const body=lines.map(l=>new Paragraph(l));const d=new Document({sections:[{children:[new Paragraph({children:[new TextRun('Rectoría | Universidad Nacional de Colombia')]}),...body,new Paragraph('Carrera 45 # 26-85 – Edificio Uriel Gutiérrez Piso 5')]}]});Packer.toBlob(d).then(b=>saveAs(b,`editado_${file||'documento'}`))};
document.getElementById('waBtn').onclick=()=>window.open(`https://wa.me/?text=${encodeURIComponent('Documento editado listo para revisión Rectoría UNAL.')}`,'_blank');
