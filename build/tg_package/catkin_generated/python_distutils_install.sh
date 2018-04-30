#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/icaro/workspace/TG/src/tg_package"

# snsure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/icaro/workspace/TG/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/icaro/workspace/TG/install/lib/python2.7/dist-packages:/home/icaro/workspace/TG/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/icaro/workspace/TG/build" \
    "/usr/bin/python" \
    "/home/icaro/workspace/TG/src/tg_package/setup.py" \
    build --build-base "/home/icaro/workspace/TG/build/tg_package" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/icaro/workspace/TG/install" --install-scripts="/home/icaro/workspace/TG/install/bin"
