  window.addEventListener('scroll',
  function(){
    let sc = this.document.documentElement.scrollTop;
if (sc >= 2344) {
    let i = 1;
    function k1() {
        if (i == 1) {
            let img = document.getElementById('img1');
            img.src = 'bag2.png';
            let p = document.getElementById('sh1');
            p.innerText = 'SHOP GIFTS FOR HER >';
            let img2 = document.getElementById('img2');
            img2.src = 'watch.png';
            let p2 = document.getElementById('sh2');
            p2.innerText = 'SHOP WATCHES >';

            i = 0
            
        }
        else{
            let img1 = document.getElementById('img1');
            img1.src = 'bag3.png';
            let p1 = document.getElementById('sh1');
            p1.innerText = 'SHOP GIFTS FOR HIM >';
            let img2 = document.getElementById('img2');
            img2.src = 'sl.png';
            let p2 =document.getElementById('sh2');
            p2.innerText = 'SHOP LITTLE LUXURIES >';

            i = 1
        }
        
    }
    let sen = this.setInterval(k1,4000)
    }
  }
  
  
  
  )                             