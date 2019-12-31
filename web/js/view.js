const view = (() => {
    "use strict";
    const elMsg = document.querySelector('#msg'),
        elNewGame = document.querySelector('#newGame'),
        elResetGame = document.querySelector('#restartGame'),
        elQuitGame = document.querySelector('#quitGame'),
        elPreGameControls = document.querySelector('#preGameControls'),
        elInGameControls = document.querySelector('#inGameControls'),
        elUserStarts = document.querySelector('#userStarts'),
        elUserPlaysRed = document.querySelector('#userRed'),
        elUserPlaysYellow = document.querySelector('#userYellow'),
        elDifficulty = document.querySelector('#difficulty'),
        elDifficultyValue = document.querySelector('#difficultyValue'),
        RED_CIRCLE_CLASS = 'redPiece',
        YELLOW_CIRCLE_CLASS = 'yellowPiece';

    let allowUserMoves = false,
        onUserMoveHandler = () => {},
        onNewGameHandler = () => {},
        onResetGameHandler = () => {},
        onQuitGameHandler = () => {};

    for (let col=0; col<board.columnCount; col++) {
        document.querySelectorAll(`.col${col+1}`).forEach(el => {
            el.onclick = () => {
                if (allowUserMoves) {
                    onUserMoveHandler(col);
                }
            };
        });
    }

    function flashCell(col, row, count=3) {
        const circle = document.querySelector(`#cell${col+1}${row+1} #Outer`);
        circle.classList.toggle('highlight');
        setTimeout(() => {
            if (count){
                flashCell(col, row, count-1)
            } else {
                circle.classList.remove('highlight');
            }
        },500);
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

    function toggleColourSelection() {
        elUserPlaysRed.classList.toggle('selected');
        elUserPlaysYellow.classList.toggle('selected');
    }

    elUserPlaysRed.onclick = toggleColourSelection;
    elUserPlaysYellow.onclick = toggleColourSelection;

    function updateDifficulty(){
        elDifficultyValue.innerHTML = ['', 'Easy', 'Medium', 'Hard', 'Expert'][elDifficulty.value]
    }
    elDifficulty.oninput = () => {
        updateDifficulty();
    };
    updateDifficulty();

    const STATE_PRE_GAME = 'pre-game',
        STATE_USER_TURN = 'user turn',
        STATE_SERVER_TURN = 'server turn';

    function toggle(el, isVisible) {
        el.style.display = isVisible ? 'flex' : 'none';
    }

    function updateUiForState(state, stateData) {
        allowUserMoves = state === STATE_USER_TURN;

        let msg;
        if (state === STATE_PRE_GAME) {
            msg = stateData;
        } else if (state === STATE_USER_TURN) {
            msg = 'Your turn';
        } else if (state === STATE_SERVER_TURN) {
            msg = 'Thinking...';
        } else {
            msg = '';
        }
        elMsg.innerHTML = msg;

        toggle(elPreGameControls, state === STATE_PRE_GAME);
        toggle(elInGameControls, state === STATE_USER_TURN || state === STATE_USER_TURN);
    }

    return {
        displayBoard(board) {
            const userPlaysRed = this.getPrefs().userColour === 'red',
                userPieceClass = userPlaysRed ? RED_CIRCLE_CLASS : YELLOW_CIRCLE_CLASS,
                serverPieceClass = userPlaysRed ? YELLOW_CIRCLE_CLASS : RED_CIRCLE_CLASS;

            for (let row=0; row<board.rowCount; row++) {
                for (let col=0; col<board.columnCount; col++) {
                    const circle = document.querySelector(`#cell${col+1}${row+1} #Inner`),
                        value = board.getValue(col, row);

                    circle.classList.toggle(userPieceClass, value === board.userValue);
                    circle.classList.toggle(serverPieceClass, value === board.serverValue);
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
                userStarts: elUserStarts.checked,
                userColour: elUserPlaysRed.classList.contains('selected') ? 'red' : 'yellow',
                difficulty : Math.pow(10, Number(elDifficulty.value))
            };
        },
        flashCell(col, row) {
            flashCell(col, row, 4)
        },
        setStatePreGame() {
            updateUiForState(STATE_PRE_GAME, 'Click NEW GAME to play');
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
            updateUiForState(STATE_PRE_GAME, resultMsg);
        }
    }

})();