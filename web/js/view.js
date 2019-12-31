const view = (() => {
    "use strict";
    const elMsg = document.querySelector('#msg'),
        elNewGame = document.querySelector('#newGame'),
        elResetGame = document.querySelector('#restartGame'),
        elQuitGame = document.querySelector('#quitGame'),
        elPreGameControls = document.querySelector('#preGameControls'),
        elInGameControls = document.querySelector('#inGameControls'),
        USER_CIRCLE_CLASS = 'userPiece',
        SERVER_CIRCLE_CLASS = 'serverPiece';

    let allowUserMoves = false,
        onUserMoveHandler = () => {},
        onNewGameHandler = () => {},
        onResetGameHandler = () => {},
        onQuitGameHandler = () => {};

    for (let col=0; col<board.columnCount; col++) {
        document.querySelector(`#cell${col+1}6 #Inner`).onclick = () => {
            if (allowUserMoves) {
                onUserMoveHandler(col);
            }
        };
    }

    elNewGame.onclick = () => {
        onNewGameHandler();
    };

    elResetGame.onclick = () => {
        onResetGameHandler();
    };

    elQuitGame.onclick = () => {
        onQuitGameHandler();
    };

    const STATE_PRE_GAME = 'pre-game',
        STATE_USER_TURN = 'user turn',
        STATE_SERVER_TURN = 'server turn',
        STATE_GAME_OVER = 'game over';

    function toggle(el, isVisible) {
        el.style.display = isVisible ? 'block' : 'none';
    }

    function updateUiForState(state, stateData) {
        allowUserMoves = state === STATE_USER_TURN;

        let msg;
        if (state === STATE_PRE_GAME) {
            msg = 'Click NEW GAME when ready to play'
        } else if (state === STATE_USER_TURN) {
            msg = 'Your turn';
        } else if (state === STATE_SERVER_TURN) {
            msg = 'Thinking...';
        } else if (state === STATE_GAME_OVER) {
            msg = stateData;
        } else {
            msg = '';
        }
        elMsg.innerHTML = msg;

        toggle(elPreGameControls, state === STATE_PRE_GAME);
        toggle(elInGameControls, state === STATE_USER_TURN || state === STATE_USER_TURN);
    }

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
        },
        onNewGame(handler) {
            onNewGameHandler = handler;
        },
        onQuitGame(handler) {
            onQuitGameHandler = handler;
        },
        onResetGame(handler) {
            onResetGameHandler = handler;
        },
        getPrefs() {
            return {
                userStarts: true
            };
        },
        setStatePreGame() {
            updateUiForState(STATE_PRE_GAME);
        },
        setStateUserMove() {
            updateUiForState(STATE_USER_TURN);
        },
        setStateWaitingForServer() {
            updateUiForState(STATE_SERVER_TURN);
        },
        setStateGameOver(winner) {
            let resultMsg;
            if (winner === '1') {
                resultMsg = 'You win...this time';
            } else if (winner === '0') {
                resultMsg = 'YOU LOSE !!';
            } else {
                resultMsg = "It's a draw";
            }
            updateUiForState(STATE_GAME_OVER, resultMsg);
        }
    }

})();