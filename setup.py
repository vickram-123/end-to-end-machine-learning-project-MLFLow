# import setuptools
# with open("README.md","r",encoding= "utf-8") as f:
#     long_description = f.read()

# __version__= "0.0.0"
# REPO_NAME= "end-to-end-machine-learning-project-MLFLow" 
# AUTHOR_USER_NAME="vickram-123"
# SRC_REPO= "MlProject"
# AUTHOR_EMAIL= "vicky786.290@rediffmail.com" 


# setuptools.setup(
#     name= SRC_REPO,
#     version = __version__,
#     author= AUTHOR_USER_NAME,
#     author_email= AUTHOR_EMAIL,
#     description= 'A small python package for ml app',
#     long_description= long_description,
#     long_description_content= "text/markdown",
#     url= f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
#     project_urls= {
#         "Bug Tracker" f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
#         },
#     package_dir= {"":"src"},
#     packages= setuptools.find_packages(where='src') 

    

# )  

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "end-to-end-machine-learning-project-MLFLow"
AUTHOR_USER_NAME = "vickram-123"
SRC_REPO = "MlProject"
AUTHOR_EMAIL = "vicky786.290@rediffmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for ml app',
    long_description=long_description,  # Corrected parameter name
    long_description_content_type="text/markdown",  # Corrected parameter name
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={  # Corrected dictionary key formatting
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src')
)
