import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()

      while '<' in html and '>' in html:
        start = html.find('<')
        end = html.find('>', start)
        if end != -1:
            html = html[:start] + html[end+1:]
        else:
            break
      html = "\n".join(line for line in html.splitlines() if line.strip())
      return html

result = delete_html_tags("draft (1).html")
print(result)