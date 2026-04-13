import sys
import traceback
from pathlib import Path
LOG = Path(r"D:\05_BLOG\myblog\.codex_tmp\extract_7005_pdf.log")
try:
    USER_SITE = Path(r"C:\Users\SJCNH\AppData\Roaming\Python\Python313\site-packages")
    PDF_PATH = Path(r"D:\15_MAI\7005\ETHICAL SUITE - PRIVACY AND ALGORITHMIC BIAS.pdf")
    sys.path.append(str(USER_SITE))
    from pypdf import PdfReader
    reader = PdfReader(str(PDF_PATH))
    with LOG.open('w', encoding='utf-8') as f:
        f.write(f"PAGES={len(reader.pages)}\n")
        for i, page in enumerate(reader.pages[:8], start=1):
            text = page.extract_text() or ""
            f.write(f"\n--- PAGE {i} ---\n\n")
            f.write(text[:5000])
except Exception:
    LOG.write_text(traceback.format_exc(), encoding='utf-8')
    raise
