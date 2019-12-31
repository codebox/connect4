window.onload = (() => {
    "use strict";
    view.displayBoard(board);

    view.setStatePreGame();

    view.onNewGame(() => {
        board.reset();
        view.displayBoard(board);
        startGame();
    });

    view.onResetGame(() => {
        board.reset();
        view.displayBoard(board);
        startGame();
    });

    view.onQuitGame(() => {
        view.setStatePreGame();
    });

    function requestServerMove() {
        view.setStateWaitingForServer();
        fetch('http://localhost:8080/connect4', {
            'method' : 'POST',
            'body' : JSON.stringify({
                'board' : board.getState(),
                'iters' : view.getPrefs().difficulty
            }),
            'headers': {
                'Content-Type': 'application/json'
            },
        }).then(response => {
            if (!response.ok) {
                throw new Error('HTTP error, status = ' + response.status);
            }
            response.json().then(response => {
                if (response.move !== undefined) {
                    const [col, row] = board.drop(response.move, board.serverValue);
                    view.displayBoard(board);
                    view.flashCell(col, row);
                }
                if (response.winner) {
                    view.setStateGameOver(response.winner);
                } else {
                    view.setStateUserMove();
                }
            })
        })
    }

    function startGame() {
        if (view.getPrefs().userStarts) {
            view.setStateUserMove();
        } else {
            requestServerMove();
        }
    }

    view.onUserMove(col => {
        board.drop(col, board.userValue);
        view.displayBoard(board);
        requestServerMove();
    });
})();