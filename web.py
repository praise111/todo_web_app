import streamlit as st
from functions import to_read, to_write

todos = to_read()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    to_write(todos)


st.title("My Todo App")
st.subheader("This is my todo")
st.write("this app is tp increase your productivity")

for items in todos:
    checkbox = st.checkbox(items, key=items)
    if checkbox:
        todos.remove(items)
        to_write(todos)
        del st.session_state[items]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')