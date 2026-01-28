"""
Simple symbol translation for MakeTables output formats.

Just add symbols to the SYMBOLS dictionary below and they'll be automatically
translated to the appropriate format (LaTeX, HTML, DOCX, etc.).
"""

# Symbol translations: canonical_symbol -> {format: representation}
SYMBOLS = {
    # Statistical symbols
    "R²": {
        "tex": r"R²",         # Unicode superscript
        "typst": "$R^2$",        # Typst math mode
        "html": "R<sup>2</sup>", # HTML superscript
        "docx": "R²",            # Unicode
        "plain": "R²"
    },

    # Interaction symbol
    "×": {
        "tex": r"×",          # Unicode times
        "typst": "$times$",      # Typst math mode
        "html": "&times;",       # HTML entity
        "docx": "×",
        "plain": "x"
    },

    # Mathematical comparison symbols
    "≤": {
        "tex": r"≤",          # Unicode
        "typst": "$≤$",          # Typst math mode
        "html": "&le;",          # HTML entity
        "docx": "≤",
        "plain": "<="
    },

    "≥": {
        "tex": r"≥",          # Unicode
        "typst": "$≥$",          # Typst math mode
        "html": "&ge;",          # HTML entity
        "docx": "≥",
        "plain": ">="
    },

    "<": {
        "tex": r"<",             # LaTeX text mode
        "typst": "$<$",          # Typst math mode
        "html": "&lt;",          # HTML entity
        "docx": "<",
        "plain": "<"
    },

    ">": {
        "tex": r">",             # LaTeX text mode
        "typst": "$>$",          # Typst math mode
        "html": "&gt;",          # HTML entity
        "docx": ">",
        "plain": ">"
    },

    # Greek letters commonly used in statistics
    "α": {
        "tex": r"α",        # Unicode
        "typst": "$alpha$",      # Typst math mode
        "html": "&alpha;",       # HTML entity
        "docx": "α",
        "plain": "alpha"
    },

    "β": {
        "tex": r"β",         # Unicode
        "typst": "$beta$",       # Typst math mode
        "html": "&beta;",        # HTML entity
        "docx": "β",
        "plain": "beta"
    },

    "σ": {
        "tex": r"σ",        # Unicode
        "typst": "$sigma$",      # Typst math mode
        "html": "&sigma;",       # HTML entity
        "docx": "σ",
        "plain": "sigma"
    },

    # Other common symbols
    "±": {
        "tex": r"±",           # Unicode
        "typst": "$plus.minus$", # Typst math mode
        "html": "&plusmn;",      # HTML entity
        "docx": "±",
        "plain": "+/-"
    },

    "°": {
        "tex": r"°",        # Unicode
        "typst": "$degree$",     # Typst math mode
        "html": "&deg;",         # HTML entity
        "docx": "°",
        "plain": "deg"
    }
}


def translate_symbols(text: str, output_format: str) -> str:
    """
    Translate symbols in text to the specified output format.

    Args:
        text: Text containing symbols to translate
        output_format: Target format ('tex', 'typst', 'html', 'docx', 'gt', 'plain')
                      Note: 'gt' is mapped to 'html' since GT uses HTML rendering

    Returns:
        Text with symbols translated to the target format

    Example:
        >>> translate_symbols("Age×Income with R²", "tex")
        "Age\\times Income with R²"
        >>> translate_symbols("α ≤ 0.05", "html")
        "&alpha; &le; 0.05"
    """
    if not isinstance(text, str):
        return text

    # Map 'gt' to 'html' since GT (Great Tables) uses HTML rendering
    format_key = "html" if output_format == "gt" else output_format

    result = text
    for symbol, translations in SYMBOLS.items():
        if symbol in result:
            target_symbol = translations.get(format_key, symbol)
            result = result.replace(symbol, target_symbol)

    return result
