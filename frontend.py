import streamlit as st
from ai_researcher_2 import INITIAL_PROMPT, graph, config
import logging
from langchain_core.messages import AIMessage, BaseMessage

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# App config
st.set_page_config(page_title="Research AI Agent", page_icon="📄", layout="wide")
st.title("📄 Research AI Agent")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    logger.info("Initialized chat history")

if "processing" not in st.session_state:
    st.session_state.processing = False

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
user_input = st.chat_input(
    "What research topic would you like to explore?",
    disabled=st.session_state.processing
)

if user_input:
    # Add user message to history and display
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    logger.info(f"User input: {user_input}")
    st.session_state.processing = True
    
    # Prepare input for the agent
    messages = [{"role": "system", "content": INITIAL_PROMPT}] + st.session_state.chat_history
    chat_input_data = {"messages": messages}
    
    logger.info("Starting agent processing...")
    
    # Stream agent response with streaming display
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        tool_calls_log = []
        
        try:
            for s in graph.stream(chat_input_data, config, stream_mode="values"):
                message = s["messages"][-1]
                
                # Log tool calls
                if hasattr(message, "tool_calls") and message.tool_calls:
                    for tool_call in message.tool_calls:
                        tool_name = tool_call.get("name", "unknown")
                        logger.info(f"Tool call: {tool_name}")
                        tool_calls_log.append(f"🔧 Calling: {tool_name}")
                
                # Extract text content
                if isinstance(message, AIMessage) and message.content:
                    content = message.content
                    
                    # Handle different content types
                    if isinstance(content, str):
                        full_response = content
                    elif isinstance(content, list):
                        # Handle content blocks
                        text_parts = [
                            c.get("text", "") if isinstance(c, dict) else str(c)
                            for c in content
                            if isinstance(c, dict) or isinstance(c, str)
                        ]
                        full_response = "\n".join(text_parts)
                    
                    # Update display with both tool calls and response
                    display_content = ""
                    if tool_calls_log:
                        display_content += "\n".join(tool_calls_log) + "\n\n"
                    display_content += full_response
                    
                    response_placeholder.markdown(display_content)
            
            # Add final response to history
            if full_response:
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": full_response}
                )
                logger.info("Agent response added to history")
        
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            st.error(error_msg)
            logger.error(f"Agent error: {str(e)}", exc_info=True)
    
    st.session_state.processing = False

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.success("Chat history cleared!")
        st.rerun()
    
    st.divider()
    
    st.subheader("📊 Chat Stats")
    st.metric("Messages", len(st.session_state.chat_history))
    
    st.divider()
    
    st.subheader("💡 Tips")
    st.markdown("""
    - Start with a broad topic
    - Ask to refine research directions
    - Request paper reading/analysis
    - Ask the agent to write the final paper
    - Papers are saved as PDFs
    """)
