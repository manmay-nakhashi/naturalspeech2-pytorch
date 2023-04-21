from setuptools import setup, find_packages

setup(
  name = 'naturalspeech2-pytorch',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'Natural Speech 2 - Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lucidrains/naturalspeech2-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'latent diffusion',
    'speech synthesis'
  ],
  install_requires=[
    'audiolm-pytorch>=0.27.1',
    'einops>=0.4',
    'torch>=1.6',
    'vector-quantize-pytorch>=1.1.6'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
