"""Building a webapp
We will use streamlit module with the same backend we built earlier.
"""
import streamlit as st
import functions


def addTask():
    todo = st.session_state["addTask"] + "\n"
    todoList.append(todo)
    functions.set_todo_list(todoList)
    st.session_state["addTask"] = ""


def markDone(task):
    del st.session_state[task]
    taskNumber = todoList.index(task)
    todoList.pop(taskNumber)
    functions.set_todo_list(todoList)


todoList = functions.get_todo_list()

st.title("The Task App")
st.write("Add pending tasks here:")

for index, task in enumerate(todoList):
    todo = st.checkbox(task, key=task)
    if todo:
        markDone(task)
        st.rerun()
    else:
        pass


st.text_input(label="Add a New Task", placeholder="Type here...", key="addTask", on_change=addTask)

st.subheader("Completed Tasks")
