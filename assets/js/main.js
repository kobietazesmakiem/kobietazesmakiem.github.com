//document.addEventListener('DOMContentLoaded', () => {
//    const lightbox = document.getElementById('lightbox');
//    const lightboxImg = document.getElementById('lightbox-img');
//    const closeBtn = document.querySelector('.close');
//    const thumbnails = document.querySelectorAll('.thumbnail');
//
//    thumbnails.forEach(thumbnail => {
//        thumbnail.addEventListener('click', () => {
//            lightbox.style.display = 'flex';
//            lightboxImg.src = thumbnail.dataset.full;
//        });
//    });
//
//    closeBtn.addEventListener('click', () => {
//        lightbox.style.display = 'none';
//    });
//
//    lightbox.addEventListener('click', (e) => {
//        if (e.target !== lightboxImg) {
//            lightbox.style.display = 'none';
//        }
//    });
//});

class LightboxGallery {
  constructor(links) {
    this.links = links;
    this.onOpenListener = () => {}
    this.onCloseListener = () => {}
  }

  onOpen(fn){
    this.onOpenListener = fn;
    console.log('onopen', this);
    return this;
  }

  open(link){
    if(!this.dialog){
        this.createEl();
    }
    this.link = link;
    this.update();
    document.body.appendChild(this.dialog);
    this.onOpenListener(this);
  }

  onClose(fn){
    this.onCloseListener = fn;
    console.log('onopen', this);
    return this;
  }

  close(e){
    e?.stopPropagation();
    this.destroyEl(this.img);
    this.destroyEl(this.closeBtn);
    this.destroyEl(this.prevBtn);
    this.destroyEl(this.nextBtn);
    this.destroyEl(this.dialog);
    this.onCloseListener(this);
  }

  hasPrev(){
    return this.links.indexOf(this.link) > 0
  }

  prev(e){
    e?.stopPropagation();
    if(this.hasPrev()){
        this.link = this.links[this.links.indexOf(this.link) - 1];
        this.update();
    }
  }

  hasNext(){
    return this.links.indexOf(this.link) < this.links.length - 1;
  }

  next(e){
    e?.stopPropagation();
    if(this.hasNext()){
        this.link = this.links[this.links.indexOf(this.link) + 1];
        this.update();
    }
  }

  update(){
    this.img.style.opacity = 0;
    this.prevBtn.style.display = this.hasPrev() ? 'unset' : 'none'
    this.nextBtn.style.display = this.hasNext() ? 'unset' : 'none'
    setTimeout(() => {
        this.img.src = this.link;
        setTimeout(() => {
            this.img.style.opacity = 1;
        }, 100);
    }, 200);
  }

  destroyEl(el){
    el.parentNode.removeChild(el);
  }

  createEl(){

    this.img = document.createElement('img');
    this.img.addEventListener('click', e => e.stopPropagation());

    this.closeBtn = document.createElement('i');
    this.closeBtn.className="fa-solid fa-circle-xmark close";
    this.closeBtn.addEventListener('click', this.close.bind(this));

    this.prevBtn = document.createElement('i');
    this.prevBtn.className="fa-solid fa-circle-chevron-left prev";
    this.prevBtn.addEventListener('click', this.prev.bind(this));

    this.nextBtn = document.createElement('i');
    this.nextBtn.className="fa-solid fa-circle-chevron-right next";
    this.nextBtn.addEventListener('click', this.next.bind(this));

    this.dialog = document.createElement('div');
    this.dialog.className = "lightbox";
    this.dialog.appendChild(this.img);
    this.dialog.appendChild(this.closeBtn);
    this.dialog.appendChild(this.prevBtn);
    this.dialog.appendChild(this.nextBtn);
    this.dialog.addEventListener('click', this.close.bind(this));
  }
}

document.addEventListener('DOMContentLoaded', () => {
    const galleries = document.querySelectorAll('.gallery');
    galleries.forEach(gallery => {
        const links = gallery.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click', (event) => {
                event.preventDefault();
                new LightboxGallery([...links].map(e => e.href))
                    .onOpen(g => {window.gallery = g})
                    .onClose(g => {delete window.gallery})
                    .open(link.href);
            });
        })
    });

});