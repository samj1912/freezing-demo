#!/usr/bin/env bash
set -e
APP_NAME=$1
cd dist
ditto -rsrc --arch x86_64 "$APP_NAME.app" "$APP_NAME.tmp"
rm -r "$APP_NAME.app"
mv "$APP_NAME.tmp" "$APP_NAME.app"
hdiutil create -volname "$APP_NAME" -srcfolder "$APP_NAME.app" -ov -format UDBZ "$APP_NAME.dmg"
