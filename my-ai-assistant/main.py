import streamlit as st
from graph import app

st.set_page_config(page_title="University Help Desk", page_icon="🎓")
st.title("🎓 University Help Desk")
st.caption("Ask me about admissions, fees, courses, exams, hostel, or transport!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask your question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            initial_state = {
                "user_query": prompt,
                "query_type": "",
                "retrieved_context": "",
                "agent_response": "",
                "evaluation_result": "",
                "final_response": "",
                "messages": st.session_state.messages,
                "retry_count": 0
            }
            result = app.invoke(initial_state)
            response = result["final_response"]
            st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})