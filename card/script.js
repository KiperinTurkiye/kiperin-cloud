function triggerDownload(url, filename){
  try{
    const a=document.createElement('a');
    a.href=url;
    a.download=filename||url.split('/').pop()||'card.png';
    a.rel='noopener';
    a.style.display='none';
    document.body.appendChild(a);
    a.click();
    a.remove();
    return true;
  }catch(e){
    console.error('Download failed',e);
    return false;
  }
}

function autoDownload(){
  const img=document.getElementById('cardImage');
  if(!img)return;
  const url=img.getAttribute('src');
  const filename=img.getAttribute('data-download')||url.split('/').pop()||'card.png';
  triggerDownload(url,filename);
}

window.addEventListener('DOMContentLoaded',()=>{
  const btn=document.getElementById('downloadBtn');
  if(btn){
    btn.addEventListener('click',()=>{
      const img=document.getElementById('cardImage');
      if(img){
        const filename=img.getAttribute('data-download')||img.src.split('/').pop()||'card.png';
        triggerDownload(img.src,filename);
      }
    });
  }

  // Try auto download shortly after load. Some browsers block immediate auto-downloads;
  // this makes a best effort without user gesture.
  setTimeout(autoDownload, 350);
});


