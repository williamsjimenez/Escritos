window.CATS=["efemerides","comunicados","discursos","correos","derechos_peticion","tweets","institucional","parrillas","efemerides_academicas","otros"];
window.deadlineInfo=(d)=>{const t=new Date(),f=new Date(d);const diff=Math.ceil((f-t)/86400000);return{diff,vencido:diff<0,proximo:diff>=0&&diff<=7}};
