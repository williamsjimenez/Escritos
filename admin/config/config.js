const enc=(s)=>btoa(unescape(encodeURIComponent(s.split('').map((c,i)=>String.fromCharCode(c.charCodeAt(0)^((i%7)+3))).join(''))));
document.getElementById('save').onclick=()=>{const cfg={owner:owner.value,repo:repo.value,branch:branch.value,token:enc(token.value)};localStorage.setItem('gh_cfg',JSON.stringify(cfg));alert('Guardado');};
