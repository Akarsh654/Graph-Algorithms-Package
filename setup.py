from setuptools import _install_setup_requires, setup

with open("README.md", "r") as f:
    long_description=f.read()


setup(name='graph_algo_vis',
      classifiers = [
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
      ],
      version='0.2',
      extras_require = {
          "dev": ["networkx", "matplotlib",],
      },
      install_requires=[           
          'networkx',
          'matplotlib',
      ],
      keywords = ['Graph', 'Algorithms', 'BFS', 'DFS', 'Topological Sort'],
      description='Visualize Graph Algorithms',
      packages=['graph_algo_vis'],
      author="Akrash Sharma",
      author_email="akarshsharma654@gmail.com",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="http://akrashsharma.netlify.app/",
      project_urls={
        "Graph Algorithms Visualization": "https://github.com/Akarsh654/Graph-Algorithms-Package",
      },
      python_requires=">=3.6",
      zip_safe=False)