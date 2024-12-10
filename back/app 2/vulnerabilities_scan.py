import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

#region SQL Injection
def detect_sql_injection(response_text):
    return 'error in your SQL syntax' in response_text
#endregion

#region Cross-Site Scripting (XSS)
def detect_xss_vulnerability(soup):
    inputs = soup.find_all(['input', 'textarea', 'select'])
    for input_tag in inputs:
        if input_tag.get('type') not in ['submit', 'button', 'reset', 'image']:
            if input_tag.get('value') and re.search(r'<script[^>]*>(.*?)</script>', input_tag.get('value'), re.IGNORECASE):
                return True
            if input_tag.string and re.search(r'<script[^>]*>(.*?)</script>', input_tag.string, re.IGNORECASE):
                return True
    return False
#endregion

#region Files Inclusion (LFI/RFI)
def detect_lfi_rfi_vulnerability(response_text):
    patterns = [r'(\.\./|%2e%2e%2f)', r'(include\s*\(\s*[\'"](?:.*?)[\'"]\s*\))']
    for pattern in patterns:
        if re.search(pattern, response_text):
            return True
    return False
#endregion

#region User Input Validation
def detect_insufficient_input_validation(soup):
    for element in soup.find_all():
        for attr in element.attrs:
            if is_dangerous_attribute(attr, element[attr]):
                return True
    return False

def is_dangerous_attribute(attr_name, attr_value):
    if re.match(r'on\w+', attr_name, re.IGNORECASE) and is_dangerous_event(attr_value):
        return True
    if is_dangerous_url_attribute(attr_name) and is_dangerous_url(attr_value):
        return True
    return False

def is_dangerous_url_attribute(attr_name):
    dangerous_url_attributes = ['src', 'href', 'action', 'data', 'codebase', 'cite', 'formaction', 'manifest', 'poster', 'profile', 'srcdoc', 'ping']
    return attr_name.lower() in dangerous_url_attributes

def is_dangerous_event(value):
    dangerous_expressions = ['javascript:', 'eval(', 'alert(', 'prompt(', 'confirm(']
    return any(expr.lower() in value.lower() for expr in dangerous_expressions)

def is_dangerous_url(url):
    dangerous_sequences = ['javascript:', 'data:', 'vbscript:', 'file:', 'ftp:', 'tel:', 'sms:', 'mailto:']
    return any(sequence in url.lower() for sequence in dangerous_sequences)
#endregion

#region Session Management
def detect_session_management(headers):
    return 'Set-Cookie' not in headers
#endregion

#region Sensitive Information Exposure
def detect_sensitive_information_exposure(response_text):
    return re.search(r'(password|secret|private_key)', response_text, re.IGNORECASE)
#endregion

def scan_vulnerabilities(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        vulnerabilities = []

        # SQL Injection
        sql_injection = detect_sql_injection(response.text)
        vulnerabilities.append("Possible SQL Injection, please patch your application quickly" 
                               if sql_injection else "No SQL Injection detected")

        # Cross-Site Scripting (XSS)
        xss_vulnerability = detect_xss_vulnerability(soup)
        vulnerabilities.append("Possible Cross-Site Scripting (XSS) attack" 
                               if xss_vulnerability else "No XSS vulnerabilities detected")

        # Files Inclusion (LFI/RFI)
        lfi_rfi_vulnerability = detect_lfi_rfi_vulnerability(response.text)
        vulnerabilities.append("Possible Files Inclusion (LFI/RFI) attack" 
                               if lfi_rfi_vulnerability else "No LFI/RFI vulnerabilities detected")

        # User Input Validation
        user_input_validation = detect_insufficient_input_validation(soup)
        vulnerabilities.append("Insufficient User Input Validation, potential alert" 
                               if user_input_validation else "Sufficient User Input Validation")

        # Session Management
        session_management = detect_session_management(response.headers)
        vulnerabilities.append("Possible Incorrect Session Management" 
                               if session_management else "Correct Session Management")

        # Sensitive Information Exposure
        sensitive_information_exposure = detect_sensitive_information_exposure(response.text)
        vulnerabilities.append("Possible Exposure of Sensitive Information" 
                               if sensitive_information_exposure else "No exposure of sensitive information detected")

        return vulnerabilities

    except requests.RequestException as e:
        return [f"Error during request to {url}: {str(e)}"]

    except Exception as e:
        return [f"Error while parsing URL {url}: {str(e)}"]

@app.route('/scan', methods=['POST'])
def scan():
    if request.method == 'POST':
        url = request.json.get('url')
        if url:
            vulnerabilities = scan_vulnerabilities(url)
            return jsonify({'vulnerabilities': vulnerabilities})
        else:
            return jsonify({'error': 'URL missing in request'}), 400
    else:
        # If not POST method
        return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
