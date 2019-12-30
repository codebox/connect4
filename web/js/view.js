const view = (() => {
    "use strict";
    const holes = document.querySelector('#Holes'),
        USER_CIRCLE_CLASS = 'userPiece',
        SERVER_CIRCLE_CLASS = 'serverPiece';

    let onUserMoveHandler = () => {};

    for (let col=0; col<board.columnCount; col++) {
        document.querySelector(`#cell${col+1}6 #Inner`).onclick = () => {
            onUserMoveHandler(col);
        };
    }

    // holes.onclick=(e => {
    //     const target = e.target;
    //     if (target.id='Inner'){
    //         target.setAttribute('fill', 'red')
    //     }
    // });

    return {
        displayBoard(board) {
            for (let row=0; row<board.rowCount; row++) {
                for (let col=0; col<board.columnCount; col++) {
                    const circle = document.querySelector(`#cell${col+1}${row+1} #Inner`),
                        value = board.getValue(col, row);

                    circle.classList.toggle(USER_CIRCLE_CLASS, value === board.userValue);
                    circle.classList.toggle(SERVER_CIRCLE_CLASS, value === board.serverValue);
                }
            }
        },
        onUserMove(handler) {
            onUserMoveHandler = handler;
        }
    }

})();