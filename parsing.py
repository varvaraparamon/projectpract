import urllib.parse
import re
import urllib.request

def parse_url_and_headers():
    url = input("введите URL англоязычной HTML страницы: ")
    
    parsed_url = urllib.parse.urlparse(url)
    print("разобранный URL:", parsed_url)
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
        h1_pattern = r'.*</h1>'
        h1_tags = re.findall(h1_pattern, html, re.IGNORECASE)
        
        clean_tags = [re.sub(r'<[^>]+>', '', tag).strip() for tag in h1_tags]
        
        print("все заголовки h1:", ' '.join(clean_tags))
    except Exception as e:
        print(f"ошибка при обработке URL: {str(e)}")

parse_url_and_headers()