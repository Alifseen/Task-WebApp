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


def markDone(key):
    completedTodoList.append(key)
    functions.set_todo_list(completedTodoList, filepath="done.txt")
    del st.session_state[key]
    taskNumber = todoList.index(key)
    todoList.pop(taskNumber)
    functions.set_todo_list(todoList)
    st.rerun()


def editTodo(key):
    newTodo = st.session_state["editTaskInput"] + "\n"
    taskNumber = todoList.index(key)
    todoList[taskNumber] = newTodo
    functions.set_todo_list(todoList)
    st.rerun()


todoList = functions.get_todo_list()
completedTodoList = functions.get_todo_list("done.txt")


st.title("The Task App")
st.divider()
st.write("Pending Tasks:")

for index, task in enumerate(todoList):
    checkBox = st.checkbox(task, key=task)
    if checkBox:
        left, right = st.columns([0.8,0.2])
        editTask = right.button("Edit", help="Change the selected Task",key="editTask", icon=":material/edit:")
        completeTask = left.button("Done", help="Mark the selected task as 'Complete'", key="markDone", icon=":material/check:")
        if completeTask:
            markDone(task)
        if editTask:
            st.session_state["editkey"] = task
            newTask = st.text_input("Edit Task", placeholder="Rewrite the task...", key="editTaskInput", label_visibility="hidden")
        else:
            pass
    else:
        pass

if "editTaskInput" in st.session_state.keys() and st.session_state["editTaskInput"] != "":
    editTodo(st.session_state["editkey"])

st.divider()
st.text_input(label="Add a Task:", placeholder="Type here...", key="addTask", on_change=addTask)
st.divider()

left, right = st.columns([0.8,0.2])
left.subheader("Completed Tasks")
clearList = right.button("Clear", help="Remove all completed tasks from this list",key="clearList", icon=":material/delete_forever:")

for index, task in enumerate(completedTodoList):
    st.write(f"{index+1}. {task}")

if clearList:
    functions.set_todo_list([], filepath="done.txt")
    st.rerun()