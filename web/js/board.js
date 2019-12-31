const board = (() => {
    "use strict";
    let values = [];

    return {
        columnCount : 7,
        rowCount : 6,
        userValue : '1',
        serverValue : '0',
        emptyValue : '.',

        getValue(col, row) {
            return values[row] && values[row][col];
        },

        getState() {
            const state = [];
            for (let row=this.rowCount-1; row>=0; row--) {
                let rowValue = '';
                for (let col=0; col<this.columnCount; col++) {
                    rowValue += this.getValue(col, row) || this.emptyValue;
                }
                state.push(rowValue);
            }
            return state;
        },

        drop(col, value) {
            if (col < 0 || col >= this.columnCount) {
                throw new Error(`Bad column number: ${col}`);
            }
            if (this.columnIsFull(col)) {
                throw new Error(`Column ${col} is full`);
            }
            if (value !== this.serverValue && value !== this.userValue) {
                throw new Error(`Bad value: ${value}`);
            }

            let highestEmptyRowInColumn = this.rowCount - 1;
            while (highestEmptyRowInColumn > 0) {
                if (this.getValue(col, highestEmptyRowInColumn - 1)) {
                    break;
                }
                highestEmptyRowInColumn--;
            }

            const row = highestEmptyRowInColumn;
            if (!values[row]) {
                values[row] = [];
            }
            values[row][col] = value;

            return [col, row];
        },

        columnIsFull(col) {
            return !! this.getValue(col, this.rowCount-1);
        },

        reset() {
            values = [];
        }
    }
})();