from tika import parser
from io import StringIO 

def readfile(uploaded_file):
    if uploaded_file is not None:
        filename = str(uploaded_file.name)
        try:
            if filename.endswith('.txt'):
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

                # To read file as string:
                string_data = stringio.read()
                return (string_data)
            else:
                raw = parser.from_file(uploaded_file)
                return (raw['content'])
        except:
            return False