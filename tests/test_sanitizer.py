import pytest
from app.utils.sanitizer import sanitize_html

def test_sanitize_html_script_tags():
    input_text = '<script>alert("XSS")</script><p>Test</p>'
    expected = '<p>Test</p>'
    assert sanitize_html(input_text) == expected

def test_sanitize_html_nested_script():
    input_text = '<p><script>alert("XSS")</script>Test</p>'
    expected = '<p>Test</p>'
    assert sanitize_html(input_text) == expected

def test_sanitize_html_event_handlers():
    input_text = '<p onclick="alert(\'XSS\')">Test</p>'
    expected = '<p>Test</p>'
    assert sanitize_html(input_text) == expected

def test_sanitize_html_javascript_urls():
    input_text = '<a href="javascript:alert(\'XSS\')">Test</a>'
    expected = 'Test'
    assert sanitize_html(input_text) == expected

def test_sanitize_html_allows_safe_tags():
    input_text = '<p>Test</p><b>Bold</b><i>Italic</i>'
    expected = '<p>Test</p><b>Bold</b><i>Italic</i>'
    assert sanitize_html(input_text) == expected

def test_sanitize_html_removes_unsafe_tags():
    input_text = '<iframe src="evil.com"></iframe><p>Test</p>'
    expected = '<p>Test</p>'
    assert sanitize_html(input_text) == expected

def test_sanitize_html_handles_empty_input():
    assert sanitize_html(None) is None
    assert sanitize_html('') == ''

def test_sanitize_html_complex_nested():
    input_text = '''
        <div onclick="alert('XSS')">
            <script>alert('Nested XSS')</script>
            <p>Safe content</p>
            <iframe src="evil.com">
                <b>Bold text</b>
            </iframe>
        </div>
    '''
    expected = '<p>Safe content</p><b>Bold text</b>'
    assert sanitize_html(input_text).replace(' ', '') == expected.replace(' ', '')
