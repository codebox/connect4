const view = (() => {
    "use strict";
    const holes = document.querySelector('#Holes');
    holes.onclick=(e => {
        const target = e.target;
        if (target.id='Inner'){
            target.setAttribute('fill', 'red')
        }
    })


})();