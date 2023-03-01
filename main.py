import PyPDF2
import textract
import re
from sympy import sympify, solve, simplify

# Open the PDF file and extract text from all pages
filename = 'pages.pdf'
with open(filename, 'rb') as f:
    pdf = PyPDF2.PdfReader(f)
    text = '\n'.join([page.extract_text() for page in pdf.pages])

print('Text extracted from PDF:')
print(text)

# Define a regular expression to match math problems in the text
problem_regex = r'(\d+[\s]*[+\-*\/][\s]*\d+)'

# Extract all math problems from the text
problems = re.findall(problem_regex, text)

print('Math problems found:')
print(problems)

# Solve each math problem and print the result
for problem in problems:
    try:
        equation = sympify(problem.replace(' ', ''))
        simplified_equation = simplify(equation)
        if equation != simplified_equation:
            result = solve(equation)
            print(f'{problem} = {result}')
        else:
            print(f'{problem} = {equation}')
    except:
        print(f'Error solving problem: {problem}')
