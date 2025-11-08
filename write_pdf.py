from langchain_core.tools import tool
from datetime import datetime
from pathlib import Path
import subprocess
import logging
import sys

logger = logging.getLogger(__name__)

def render_latex_pdf_impl(latex_content: str) -> str:
    """Internal implementation for LaTeX to PDF rendering"""
    
    try:
        # Step 1: Create output directory
        output_dir = Path("output").absolute()
        output_dir.mkdir(exist_ok=True)
        logger.info(f"Output directory: {output_dir}")
        
        # Step 2: Setup filenames
        tex_file = output_dir / "paper.tex"
        pdf_file = output_dir / "paper.pdf"
        
        # Step 3: Write LaTeX content to file
        tex_file.write_text(latex_content, encoding="utf-8")
        logger.info(f"LaTeX file written: {tex_file}")
        
        # Step 4: Run tectonic with full path
        # On Windows, subprocess needs the executable name or full path
        tectonic_cmd = "tectonic"  # Will use PATH or current directory
        
        cmd = [
            tectonic_cmd,
            str(tex_file),
            "--outdir", str(output_dir)
        ]
        
        logger.info(f"Running: {' '.join(cmd)}")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
            shell=True  # Add this for Windows compatibility
        )
        
        # Step 5: Check for errors
        if result.returncode != 0:
            logger.error(f"tectonic failed with return code {result.returncode}")
            logger.error(f"stdout: {result.stdout}")
            logger.error(f"stderr: {result.stderr}")
            raise RuntimeError(f"tectonic failed: {result.stderr}")
        
        # Step 6: Verify PDF was created
        if not pdf_file.exists():
            logger.error(f"PDF not found at: {pdf_file}")
            files = list(output_dir.glob("*"))
            logger.error(f"Files in output directory: {files}")
            raise FileNotFoundError(f"PDF not generated at {pdf_file}")
        
        logger.info(f"✅ PDF generated: {pdf_file}")
        return str(pdf_file)
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise

# Wrap for LangGraph
render_latex_pdf = tool(render_latex_pdf_impl)
