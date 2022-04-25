# install the latest version of kaggle_environments
from kaggle_environments import make
env = make("kore_fleets", debug=True)
print(env.name, env.version)