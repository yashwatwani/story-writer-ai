# ui.py
import streamlit as st
from mcp import ModelContextProtocol # Assuming mcp.py is in the same directory or accessible

# Initialize MCP instance - for a web app, state management is key.
# Streamlit's session_state is perfect for this.
if 'mcp' not in st.session_state:
    st.session_state.mcp = ModelContextProtocol()

st.title("Collaborative Story Writing Assistant")

st.header("Your Story So Far:")
# Display the story context in a read-only text area
story_display = st.text_area("Story", value=st.session_state.mcp.get_story_context(), height=300, key="story_display_area", disabled=True)

st.header("Add to Your Story or Get Help:")
user_input = st.text_area("Your next paragraph or idea:", height=100, key="user_story_input")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Add to Story"):
        if user_input:
            st.session_state.mcp.update_story_context(user_input, from_user=True)
            # Rerun to update the display. Streamlit reruns the script on widget interaction.
            st.rerun() # This will refresh the story_display

with col2:
    if st.button("Get Plot Idea"):
        # For now, just show placeholder. Later, this will call the agent.
        suggestion = st.session_state.mcp.delegate_to_agent("plot_weaver", "Suggest a plot twist based on the current story.")
        st.info(f"Plot Weaver says: {suggestion}")
        # In a real app, we might add this suggestion to the user_input box or directly to story

with col3:
    if st.button("Develop Character"):
        suggestion = st.session_state.mcp.delegate_to_agent("character_forge", "Suggest a new character detail or motivation.")
        st.info(f"Character Forge says: {suggestion}")

with col4:
    if st.button("Paint Scene"):
        suggestion = st.session_state.mcp.delegate_to_agent("scene_painter", "Suggest descriptive details for the current scene.")
        st.info(f"Scene Painter says: {suggestion}")


# To run this UI:
# 1. Make sure your virtual environment is activated.
# 2. In your terminal, navigate to the project directory.
# 3. Run: streamlit run ui.py