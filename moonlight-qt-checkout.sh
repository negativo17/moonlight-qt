#!/bin/sh

PROJECT=moonlight-qt
VERSION=$1

git clone -b v$VERSION https://github.com/moonlight-stream/$PROJECT.git $PROJECT-$VERSION

cd $PROJECT-$VERSION

git submodule update --init --recursive

rm -frv libs .git

cd ..

tar --remove-files -cJf $PROJECT-$VERSION.tar.xz $PROJECT-$VERSION


