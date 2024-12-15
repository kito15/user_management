import re
from typing import Optional

def sanitize_html(text: Optional[str]) -> Optional[str]:
    """
    Sanitize HTML content by removing script tags and other potentially harmful elements
    """
    if not text:
        return text

    # Remove script tags and their contents
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
    
    # Remove onclick and other event handlers
    text = re.sub(r' on\w+="[^"]*"', '', text)
    
    # Remove javascript: URLs
    text = re.sub(r'javascript:[^"\']*', '', text)
    
    # Only allow specific safe tags
    allowed_tags = ['p', 'br', 'b', 'i', 'u', 'em', 'strong']
    pattern = r'<[/]?([^> ]+)[^>]*>'
    
    def tag_filter(match):
        tag = match.group(1).lower()
        if tag in allowed_tags:
            return f'<{tag}>'  # Return basic tag without attributes
        return ''  # Remove non-allowed tags
    
    text = re.sub(pattern, tag_filter, text)
    
    return text
