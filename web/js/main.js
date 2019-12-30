window.onload = (() => {
    "use strict";
    view.displayBoard(board);

    view.onUserMove(col => {
        board.drop(col, board.userValue);
        view.displayBoard(board);
        fetch('http://localhost:8080/connect4', {
            'method' : 'POST',
            'body' : JSON.stringify({
                'board' : board.getState(),
                'iters' : 10000
            }),
            'headers': {
                'Content-Type': 'application/json'
            },
        }).then(response => {
            if (!response.ok) {
                throw new Error('HTTP error, status = ' + response.status);
            }
            response.json().then(move => {
                board.drop(move, board.serverValue);
                view.displayBoard(board);
            })
        })
    });
})();