import os
from openai import OpenAI
from IPython.display import display
import ipywidgets as widgets



# from dotenv import load_dotenv
# load_dotenv()

# import os
# from dotenv import Dotenv
# dotenv = Dotenv(os.path.join(os.path.dirname(__file__), ".env")) # Of course, replace by your correct path
# os.environ.update(dotenv)

# from python-dotenv import load_dotenv

# load_dotenv()

import dotenv
# print(dir(dotenv))

dotenv_path = join(dirname(__file__), '.env')
load(dotenv_path)