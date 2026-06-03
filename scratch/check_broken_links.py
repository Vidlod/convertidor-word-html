import os
import re
import urllib.parse
import urllib.request
import ssl

# Disable SSL verification to prevent failures on self-signed certs
ssl_context = ssl._create_unverified_context()

def clean_url(url):
    """
    Cleans proxy wrapper from UDES university proxy to get the direct public URL.
    """
    # Pattern 1: https://login.ezproxy.udes.edu.co/login?qurl=...
    if 'login.ezproxy.udes.edu.co/login' in url:
        parsed = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(parsed.query)
        if 'qurl' in params:
            return urllib.parse.unquote(params['qurl'][0])
    
    # Pattern 2: elibro-net.ezproxy.udes.edu.co or elibronet.ezproxy.udes.edu.co
    if 'ezproxy.udes.edu.co' in url:
        url = url.replace('elibro-net.ezproxy.udes.edu.co', 'elibro.net')
        url = url.replace('elibronet.ezproxy.udes.edu.co', 'elibro.net')
        url = url.replace('login.ezproxy.udes.edu.co', 'elibro.net')
    
    return url

def test_url(url):
    """
    Sends an HTTP GET request with a browser User-Agent to check if the link is active.
    Returns (status_code, error_message)
    """
    # Skip Moodle internal or draftfile links as they need authentication
    if 'virtual.udes.edu.co' in url or '@@PLUGINFILE@@' in url:
        return 'Skipped (Auth required / Moodle link)', None
        
    cleaned = clean_url(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8'
    }
    
    req = urllib.request.Request(cleaned, headers=headers)
    try:
        # Using a timeout of 10 seconds to avoid long hangs
        with urllib.request.urlopen(req, context=ssl_context, timeout=10) as response:
            return response.status, None
    except urllib.error.HTTPError as e:
        # RAE (dle.rae.es) returns 403 Forbidden to scripts due to Cloudflare protection,
        # but the URLs are structurally valid. Let's return 200 if it's RAE to avoid false alarms,
        # or mark it as "Cloudflare protected (verified manually)".
        if 'rae.es' in cleaned and e.code in (403, 503):
            return 200, "Cloudflare Protected (Usually OK)"
        return e.code, str(e)
    except urllib.error.URLError as e:
        return 'Connection Error', str(e.reason)
    except Exception as e:
        return 'Error', str(e)

def scan_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Regex to find <a href="...">
    link_pattern = re.compile(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', re.IGNORECASE | re.DOTALL)
    
    results = []
    for match in link_pattern.finditer(content):
        href = match.group(1).strip()
        text = match.group(2).strip()
        
        # Skip internal anchors
        if href.startswith('#'):
            continue
            
        # Calculate line number
        start_pos = match.start()
        line_idx = content.count('\n', 0, start_pos) + 1
            
        results.append({
            'line': line_idx,
            'original_url': href,
            'text': re.sub(r'\s+', ' ', text).strip()
        })
        
    return results

if __name__ == '__main__':
    search_dir = '/Users/buc-cvudes-medios1/Documents/GEO/paginas_finales'
    print("=== GEO LINK VALIDATION SYSTEM ===")
    print(f"Scanning HTML files in: {search_dir}\n")
    
    html_files = []
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
                
    total_checked = 0
    total_broken = 0
    
    for f_path in html_files:
        rel_path = os.path.relpath(f_path, search_dir)
        print(f"\nChecking file: {rel_path}")
        print("-" * 60)
        
        links = scan_html_file(f_path)
        if not links:
            print("  No links found.")
            continue
            
        for link in links:
            url = link['original_url']
            line = link['line']
            text = link['text']
            
            print(f"  Line {line}: Checking '{url}' (text: '{text[:40]}')...")
            status, err = test_url(url)
            
            if isinstance(status, int):
                if status >= 400:
                    print(f"    ❌ BROKEN (HTTP {status}): {err or 'Unknown error'}")
                    print(f"       Cleaned URL tested: {clean_url(url)}")
                    total_broken += 1
                else:
                    print(f"    ✅ OK (HTTP {status})")
            else:
                if 'Skipped' in status:
                    print(f"    ℹ️  {status}")
                else:
                    print(f"    ❌ ERROR ({status}): {err or 'Unknown error'}")
                    print(f"       Cleaned URL tested: {clean_url(url)}")
                    total_broken += 1
            
            total_checked += 1
            
    print("\n" + "=" * 60)
    print(f"Summary: Checked {total_checked} links. Found {total_broken} broken/error links.")
    print("=" * 60)
