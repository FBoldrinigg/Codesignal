#link https://app.codesignal.com/arcade/intro/level-6/t97bpjfrMDZH8GJhi

def chessBoardCellColor(cell1, cell2):
    black, nB = "ACEG", "1357"
    white, nW = "BDFH", "2468"
    return (cell1[0] in black and cell1[1] in nB or cell1[0] in white and cell1[1] in nW)  ==  (cell2[0] in white and cell2[1] in nW or cell2[0] in black and cell2[1] in nB)
        