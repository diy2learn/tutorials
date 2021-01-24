When we start `jupyter notebook`, we have the following error:

```shell script
ImportError: dlopen(/usr/local/Caskroom/miniconda/base/envs/wifo_env/lib/python3.6/site-packages/zmq/backend/cython/constants.cpython-36m-darwin.so, 2): Symbol not found: ____chkstk_darwin
  Referenced from: /usr/local/Caskroom/miniconda/base/envs/wifo_env/lib/python3.6/site-packages/zmq/backend/cython/../../.dylibs/libsodium.23.dylib
  Expected in: /usr/lib/libSystem.B.dylib
 in /usr/local/Caskroom/miniconda/base/envs/wifo_env/lib/python3.6/site-packages/zmq/backend/cython/../../.dylibs/libsodium.23.dylib
```

## Conda config:
```shell script
conda info
     active environment : wifo_env
    active env location : /usr/local/Caskroom/miniconda/base/envs/wifo_env
            shell level : 2
       user config file : /Users/Binh/.condarc
 populated config files :
          conda version : 4.7.12
    conda-build version : not installed
         python version : 3.7.4.final.0
       virtual packages :
       base environment : /usr/local/Caskroom/miniconda/base  (writable)
           channel URLs : https://repo.anaconda.com/pkgs/main/osx-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/osx-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /usr/local/Caskroom/miniconda/base/pkgs
                          /Users/Binh/.conda/pkgs
       envs directories : /usr/local/Caskroom/miniconda/base/envs
                          /Users/Binh/.conda/envs
               platform : osx-64
             user-agent : conda/4.7.12 requests/2.22.0 CPython/3.7.4 Darwin/16.7.0 OSX/10.12.6
                UID:GID : 502:20
             netrc file : None
           offline mode : False
```

## Jupyter info

```shell script
(wifo_env) $conda list | grep jupyter
jupyter                   1.0.0                    pypi_0    pypi
jupyter-client            6.1.11                   pypi_0    pypi
jupyter-console           6.2.0                    pypi_0    pypi
jupyter-contrib-core      0.3.3                    pypi_0    pypi
jupyter-contrib-nbextensions 0.5.1                    pypi_0    pypi
jupyter-core              4.7.0                    pypi_0    pypi
jupyter-highlight-selected-word 0.2.0                    pypi_0    pypi
jupyter-latex-envs        1.4.6                    pypi_0    pypi
jupyter-nbextensions-configurator 0.4.1                    pypi_0    pypi
jupyterlab-pygments       0.1.2                    pypi_0    pypi
jupyterlab-widgets        1.0.0                    pypi_0    pypi
```

## Fix
## Work
* reinstall `jupyter`: `conda install -c conda-forge notebook`

## Not work
* update `conda`: `conda update -n base -c defaults conda`
* uninstall and re-install `zeromq`: `conda remove zeromq; conda install zeromq -y`
* restart the PC

refs: 
https://jupyter.org/install
