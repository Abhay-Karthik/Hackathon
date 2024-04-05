import streamlit as st
st.set_page_config(
    page_title="Multipage app",
    page_icon="😆"
)
st.title("Homepage")
st.sidebar.success("select the pages")

import streamlit as st

# Function to display existing notes
def display_notes(notes):
    st.header("Your Notes")
    if not notes:
        st.write("No notes added yet.")
    else:
        for i, note in enumerate(notes, 1):
            st.write(f"{i}. {note}")

# Function to add a new note
def add_note():
    st.header("Add a New Note")
    new_note = st.text_input("Enter your note:")
    if st.button("Add"):
        if new_note:
            notes.append(new_note)
            st.success("Note added successfully!")
        else:
            st.warning("Please enter a note.")

# Main function
def main():
    st.title("Notes App")
    
    # Initialize notes list
    if 'notes' not in st.session_state:
        st.session_state.notes = []

    # Sidebar with options
    st.sidebar.title("Options")
    if st.sidebar.button("View Notes"):
        display_notes(st.session_state.notes)
    if st.sidebar.button("Add Note"):
        add_note()

if __name__ == "__main__":
    main()

import streamlit as st

# Function to display existing notes
def display_notes(notes):
    st.header("Your Notes")
    if not notes:
        st.write("No notes added yet.")
    else:
        for i, note in enumerate(notes, 1):
            st.info(f"{i}. {note}")

# Function to add a new note
def add_note():
    st.header("Add a New Note")
    new_note = st.text_input("Enter your note:")
    if st.button("Add"):
        if new_note:
            notes.append(new_note)
            st.success("Note added successfully!")
        else:
            st.warning("Please enter a note.")

# Main function
def main():
    st.title("Notes App")
    
    # Initialize notes list
    if 'notes' not in st.session_state:
        st.session_state.notes = []

    # Sidebar with options
    st.sidebar.title("Options")
    if st.sidebar.button("View Notes"):
        display_notes(st.session_state.notes)
    if st.sidebar.button("Add Note"):
        add_note()

if __name__ == "__main__":
    main()
