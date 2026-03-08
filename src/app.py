import streamlit as st
from graph import graph

# ---------- Page Config ----------
st.set_page_config(
    page_title="Abhay ❤️ Shreya Wedding Assistant",
    page_icon="data/couple.png",
    layout="centered"
)

# ---------- Title with Couple Icon ----------
col1, col2 = st.columns([1, 5])

with col1:
    st.image("data/couple.png", width=100)  # Small icon for header

with col2:
    st.markdown("## Abhay & Shreya Wedding Assistant")

st.write("Ask anything about the wedding!")

# ---------- Small Button Styling ----------
st.markdown("""
<style>
div.stButton > button {
    padding: 6px 10px;
    font-size: 12px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Chat Memory ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- Display Chat History ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------- Quick Questions ----------
st.markdown("### Quick Questions")

c1, c2, c3, c4 = st.columns(4)

quick_question = None

with c1:
    if st.button("💃 Sangeet"):
        quick_question = "Tell me about the sangeet event"

with c2:
    if st.button("🐎 Barat"):
        quick_question = "Barat kab niklegi?"

with c3:
    if st.button("🤵 Abhay"):
        quick_question = "Abhay ke bare btaye"

with c4:
    if st.button("👰 Ladkiwale-stay"):
        quick_question = "ladkiwalo ke stay/hotel ke bare me jankari"


# ---------- Chat Input ----------
user_input = st.chat_input("Ask about the wedding...")

# Use quick question if clicked
question = user_input or quick_question

# ---------- Run Assistant ----------
if question:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    # ---------- Show typing animation ----------
    with st.chat_message("assistant"):
        message_placeholder = st.empty()  # Empty container
        with st.spinner("Assistant is preparing the answer..."):
            # simulate API call
            result = graph.invoke({
                "question": question
            })
        answer = result["answer"]

        # Display answer in the chat bubble
        message_placeholder.write(answer)

    # Save assistant message in session
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })