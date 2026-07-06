import markdown
import io

out_str = io.BytesIO()


markdown.markdownFromFile(input='symbols.md',
                          output=out_str,
                          extensions=['fenced_code'])

out_str = out_str.getvalue().decode('utf-8')


print(out_str)
