# 🔬 AI Research Paper Generator

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-green.svg)](https://github.com/langchain-ai/langgraph)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Generate complete, publication-ready research papers in minutes using AI agents powered by Google Gemini and LangGraph**

An advanced agentic AI application that autonomously conducts literature review, reads research papers from arXiv, analyzes findings, and generates complete research papers in PDF format - all in under 2 minutes.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Tools Explained](#-tools-explained)
- [Troubleshooting](#-troubleshooting)
- [Advanced Usage](#-advanced-usage)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

This project implements an **AI Research Assistant** that mimics the workflow of human researchers:

1. **Literature Review**: Searches and filters recent papers from arXiv
2. **Paper Analysis**: Reads and extracts information from PDF research papers
3. **Research Writing**: Generates new research ideas and writes complete papers
4. **PDF Export**: Converts LaTeX documents to publication-ready PDFs

### What Makes This Special?

- ✅ **Fully Autonomous**: Minimal human intervention required
- ✅ **Production-Grade**: Built with best practices and error handling
- ✅ **Real-time Web Scraping**: Fetches latest research from arXiv
- ✅ **Multi-Model Support**: Uses Google Gemini 2.0/2.5 Pro
- ✅ **Interactive UI**: Beautiful Streamlit interface
- ✅ **Custom Tools**: Hand-crafted tools for research workflows

---

## ✨ Features

### Core Capabilities

| Feature | Description |
|---------|-------------|
| 🔍 **Intelligent Search** | Searches arXiv with topic-based filtering and relevance ranking |
| 📄 **PDF Processing** | Extracts and parses text from research papers automatically |
| 🤖 **AI Agents** | Two implementations: Simple (create_react_agent) and Advanced (StateGraph) |
| 📝 **LaTeX Support** | Generates properly formatted LaTeX documents with equations |
| 🎨 **PDF Rendering** | Converts LaTeX to PDF using Tectonic compiler |
| 💬 **Chat Interface** | Interactive Streamlit UI with conversation history |
| 🧠 **Memory System** | Maintains context across multiple interactions |
| 🛠️ **Custom Tools** | Three specialized tools for research workflows |

### Technical Highlights

- **Framework**: LangGraph for advanced agentic workflows
- **LLM**: Google Gemini 2.0 Flash / 2.5 Pro
- **Package Manager**: UV for lightning-fast dependency management
- **Frontend**: Streamlit for rapid prototyping
- **Error Handling**: Comprehensive try-except blocks and logging
- **API Integration**: arXiv API for real-time paper retrieval

---

## 🎬 Demo

### Sample Interaction

```
User: I want to research prompt engineering

Agent: Searching arXiv for recent papers...
       Found 5 relevant papers from 2025!

       1. "Cut-to-the-Net: Generating Next-Shot via In-Context Tuning"
       2. "Robust Normality Detection Leveraging LLMs Against Data Manipulation"
       ...

User: Tell me about the first paper

Agent: Reading the PDF... Analyzing content...

       This paper introduces a novel approach to context tuning...
       [Detailed analysis follows]

User: Based on these papers, write a new research paper on hybrid prompting strategies

Agent: Analyzing recent research... Identifying gaps...
       Generating new research paper...

       ✅ Generated: research_paper_2025_11_07_21_30_45.pdf
```

---

## 🏗️ Architecture

### System Overview

```
┌─────────────────┐
│   User Input    │
│  (Streamlit UI) │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│    AI Research Agent        │
│  (Gemini 2.0/2.5 Pro)       │
│  Built with LangGraph       │
└─────────┬───────────────────┘
          │
          │ Uses Three Tools:
          ├──────────────────────┐
          │                      │
          ▼                      ▼
┌──────────────────┐   ┌──────────────────┐
│  arXiv Search    │   │   Read PDF       │
│  Tool            │   │   Tool           │
│                  │   │                  │
│ • Web scraping   │   │ • PDF parsing    │
│ • XML parsing    │   │ • Text extract   │
│ • Filtering      │   │ • Content clean  │
└──────────────────┘   └──────────────────┘
          │
          ▼
┌──────────────────┐
│  Write PDF Tool  │
│                  │
│ • LaTeX gen      │
│ • Tectonic comp  │
│ • PDF export     │
└──────────────────┘
          │
          ▼
┌─────────────────┐
│  Research Paper │
│  (PDF Output)   │
└─────────────────┘
```

### Technology Stack

| Layer | Technology |
|-------|-----------|
| **LLM** | Google Gemini 2.0 Flash, Gemini 2.5 Pro |
| **Agent Framework** | LangGraph, LangChain |
| **Package Manager** | UV (10-100x faster than pip) |
| **Frontend** | Streamlit |
| **Data Source** | arXiv API |
| **PDF Processing** | PyPDF2 |
| **LaTeX Compiler** | Tectonic |
| **Python Version** | 3.10+ |

---

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- Git
- Internet connection
- API keys (Google Gemini)

### Option 1: Quick Install with UV (Recommended)

UV is a blazing-fast Python package manager written in Rust. It's 10-100x faster than pip!

#### Step 1: Install UV

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Step 2: Clone Repository

```bash
git clone https://github.com/yourusername/ai-researcher.git
cd ai-researcher
```

#### Step 3: Setup Environment with UV

```bash
# Initialize virtual environment
uv init

# Activate virtual environment
# Linux/macOS:
source .venv/bin/activate

# Windows:
.venv\Scripts\activate

# Install all dependencies (lightning fast!)
uv add langchain langchain-core langchain-google-genai langgraph
uv add streamlit
uv add requests pypdf2 python-dotenv
```

#### Step 4: Install Tectonic (LaTeX Compiler)

**Linux/macOS:**
```bash
# Ubuntu/Debian
sudo apt-get install tectonic

# macOS with Homebrew
brew install tectonic
```

**Windows:**
Download installer from: https://github.com/tectonic-typesetting/tectonic/releases

### Option 2: Traditional pip Install

```bash
# Clone repository
git clone https://github.com/yourusername/ai-researcher.git
cd ai-researcher

# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Install Tectonic (see above)
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# Copy example file
cp .env.example .env
```

Edit `.env` and add your API key:

```env
# Google Gemini API Key
# Get it from: https://aistudio.google.com/
GOOGLE_API_KEY=your_google_api_key_here
```

### Getting API Keys

#### Google Gemini API (Free)

1. Visit https://aistudio.google.com/
2. Click "Get API Key"
3. Create a new API key
4. Copy and paste into `.env` file

**Free Tier Limits:**
- 60 requests per minute
- 1,500 requests per day
- Perfect for development and testing

---

## 📖 Usage

### Running the Application

#### Command Line Interface

**Simple Agent (create_react_agent):**
```bash
uv run ai_researcher.py
```

**Advanced Agent (StateGraph):**
```bash
uv run ai_researcher_2.py
```

#### Web Interface (Recommended)

```bash
streamlit run frontend.py
```

Then open your browser to: `http://localhost:8501`

### Example Workflows

#### Workflow 1: Basic Research

```bash
$ uv run ai_researcher.py

User: I want to research transformer architectures
Agent: Searching arXiv for recent papers...
Agent: Found 10 papers. Here are the top 5:
       1. "Attention Is All You Need" (2025)
       2. ...

User: Tell me about paper 1
Agent: Reading PDF... [Analysis follows]

User: Write a paper on efficient transformers
Agent: Generating research paper...
Agent: ✅ Paper saved: output/research_paper_2025_11_07.pdf
```

#### Workflow 2: Interactive Web UI

1. **Start Streamlit**: `streamlit run frontend.py`
2. **Enter topic**: "quantum computing"
3. **Review papers**: Agent shows recent arXiv papers
4. **Select paper**: Choose one to read in detail
5. **Generate paper**: Ask agent to write new research

---

## 📁 Project Structure

```
ai-researcher/
│
├── ai_researcher.py          # Simple agent (create_react_agent)
├── ai_researcher_2.py        # Advanced agent (StateGraph + memory)
├── frontend.py               # Streamlit web interface
│
├── Tools/
│   ├── arxiv_tool.py         # arXiv search & web scraping
│   ├── read_pdf.py           # PDF reading & text extraction
│   └── write_pdf.py          # LaTeX generation & PDF export
│
├── output/                   # Generated PDFs and LaTeX files
│   ├── paper_*.tex          # LaTeX source files
│   └── paper_*.pdf          # Rendered PDF papers
│
├── .env                      # Environment variables (API keys)
├── .env.example              # Template for environment variables
├── requirements.txt          # Python dependencies
├── pyproject.toml            # UV project configuration
├── uv.lock                   # UV lock file
│
└── README.md                 # This file
```

---

## 🔧 How It Works

### Two Agent Implementations

#### 1. Simple Agent (`ai_researcher.py`)

Uses LangGraph's `create_react_agent()` - a high-level API:

```python
from langgraph.prebuilt import create_react_agent

# One-line agent creation!
graph = create_react_agent(model, tools=tools)
```

**Pros:** ✅ Simple, clean code, fast setup
**Cons:** ❌ Less control, limited customization

#### 2. Advanced Agent (`ai_researcher_2.py`)

Uses LangGraph's `StateGraph` for maximum control with:
- Custom state management
- Conditional edges
- Memory checkpointing
- Full workflow control

**Pros:** ✅ Production-grade, full control, memory persistence
**Cons:** ❌ More complex, requires deeper understanding

---

## 🛠️ Tools Explained

### Tool 1: arXiv Search (`arxiv_tool.py`)

**Purpose**: Search for research papers on arXiv

**Features:**
- Query sanitization (removes invalid characters)
- XML parsing with ElementTree
- Sorted by submission date
- Configurable result limit

**Returns:**
```json
{
  "entries": [
    {
      "title": "Paper Title",
      "summary": "Abstract...",
      "authors": ["Author 1", "Author 2"],
      "categories": ["cs.AI", "cs.LG"],
      "pdf": "https://arxiv.org/pdf/..."
    }
  ]
}
```

### Tool 2: Read PDF (`read_pdf.py`)

**Purpose**: Extract text from research papers

**Features:**
- Downloads PDFs from URLs
- Page-by-page extraction
- Error handling for network issues
- Text cleaning and formatting

**Example:**
```python
text = read_pdf("https://arxiv.org/pdf/2501.00123.pdf")
# Returns full text content
```

### Tool 3: Write PDF (`write_pdf.py`)

**Purpose**: Generate LaTeX and export to PDF

**Features:**
- Automatic LaTeX compilation
- Unique timestamped filenames
- LaTeX syntax error checking
- Subprocess management for Tectonic

**Example:**
```python
latex_content = """
\documentclass{article}
\begin{document}
Research Paper Content
\end{document}
"""
pdf_path = render_latex_pdf(latex_content)
```

---

## 🐛 Troubleshooting

### Common Issues

**1. API Key Error**
```
Solution: Verify .env file exists and GOOGLE_API_KEY is set correctly
```

**2. Tectonic Not Found**
```bash
# Install Tectonic
sudo apt-get install tectonic  # Linux
brew install tectonic          # macOS
```

**3. UV Installation Failed**
```bash
# Reload shell
source ~/.bashrc

# Or add to PATH
export PATH="$HOME/.cargo/bin:$PATH"
```

**4. arXiv Rate Limit**
```
Solution: Wait 60 seconds between requests, reduce max_results
```

**5. PDF Extraction Error**
```
Solution: Verify PDF URL is accessible, check internet connection
```

**6. LaTeX Compilation Error**
```
Solution: Check .tex file for syntax errors, verify document structure
```

---

## 🚀 Advanced Usage

### Custom Tools

```python
from langchain_core.tools import tool

@tool
def custom_search(query: str) -> dict:
    """Your custom search tool"""
    # Implementation
    return results
```

### Different Models

```python
# Gemini 2.5 Pro (more capable)
model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

# Gemini 2.0 Flash (faster)
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
```

### Memory Management

```python
from langgraph.checkpoint.memory import MemorySaver

config = {"configurable": {"thread_id": "user_123"}}
graph.stream({"messages": messages}, config)
```

---

## 💡 Tips & Best Practices

### Good Prompts ✅
- "Research recent papers on transformer attention mechanisms"
- "Find papers about reinforcement learning published in 2025"

### Bad Prompts ❌
- "Find stuff" (too vague)
- "!@#$%^&*" (invalid characters)

### Performance
- Use Gemini 2.0 Flash for speed
- Limit max_results to 5-10 papers
- Use streaming for real-time feedback

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch: `git checkout -b feature/name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature/name`
5. Open Pull Request

### Areas for Contribution
- Additional research tools (Google Scholar, PubMed)
- UI/UX improvements
- Analytics and visualization
- Multi-language support
- Better LaTeX templates

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 🙏 Acknowledgments

- **LangChain/LangGraph** - Agent framework
- **Google Gemini** - LLM capabilities
- **arXiv** - Research paper access
- **Tectonic** - LaTeX compilation
- **Streamlit** - UI development
- **UV** - Package management

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/ai-researcher/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/ai-researcher/discussions)

---

## 🎓 Learn More

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Google Gemini API](https://ai.google.dev/docs)
- [arXiv API Guide](https://arxiv.org/help/api)

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

Made with ❤️ for the AI Research Community

[Report Bug](https://github.com/yourusername/ai-researcher/issues) · [Request Feature](https://github.com/yourusername/ai-researcher/issues)

</div>