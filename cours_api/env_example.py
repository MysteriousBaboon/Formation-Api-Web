import os 

from dotenv import load_dotenv 

load_dotenv()

mdp = os.getenv('mdp_bancaire')
print(mdp)