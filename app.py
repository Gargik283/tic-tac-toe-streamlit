import streamlit as st
import numpy as np

# ------------------------
# Initialize board state
# ------------------------
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.game_over = False


# ------------------------
# Helper functions
# ------------------------
def print_board(b):
    symbols = {0: " ", 1: "X", -1: "O"}
    return [[symbols[val] for val in row] for row in b]


def check_winner(b):
    # rows & cols
    if 3 in np.sum(b, axis=1) or 3 in np.sum(b, axis=0):
        return "X"
    if -3 in np.sum(b, axis=1) or -3 in np.sum(b, axis=0):
        return "O"

    # diagonals
    if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return "X"
    if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
        return "O"

    # draw
    if not 0 in b:
        return "Draw"

    return None


def reset_game():
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.game_over = False


# ------------------------
# UI
# ------------------------
st.title("🎮 Tic Tac Toe (Streamlit)")

board = st.session_state.board

st.write("### Player Turn:", "X" if st.session_state.current == 1 else "O")


# ------------------------
# Create grid buttons
# ------------------------
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        if cols[j].button(print_board(board)[i][j] or " ", key=f"{i}-{j}"):

            if not st.session_state.game_over and board[i, j] == 0:

                board[i, j] = st.session_state.current

                # check winner
                result = check_winner(board)

                if result is not None:
                    st.session_state.game_over = True
                    st.success(f"🎉 {result} wins!" if result != "Draw" else "🤝 It's a Draw!")

                else:
                    st.session_state.current *= -1


st.divider()

if st.button("🔄 Reset Game"):
    reset_game()