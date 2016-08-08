#pyenv初探

##1.install pyenv


    $ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
    $ echo 'export PYENV_ROOT="$HOME/.pyenv"'>> ~/.bashrc
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"'>> ~/.bashrc
    $ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc