#!/bin/sh
if [ ! -f virtualenv/bin/activate ];then
  virtualenv --no-site-packages virtualenv/
fi
source virtualenv/bin/activate
pip -q install -r pip-requirements
pip -q install coverage
coverage erase
coverage run ./manage.py test $@
ret=$?
if [ $ret -eq 0 ];then
    coverage report -m --include=\* --omit=\*/migrations/\*,spiff/settings.py,spiff/local_settings.py,manage.py,*/site-packages/*
fi
exit $ret

