
[app]

# (str) Title of your application
title = MyBuckConverter0.1

# (str) Package name
package.name = mybuckconverter0.1

# (str) Package domain (needed for android/ios packaging)
package.domain = org.luggyasaul

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3==3.10,kivy==2.2.1,kivymd==1.2.0

# (list) Supported orientations
orientation = portrait

# (list) Android permissions
android.permissions = android.permission.INTERNET,android.permission.WRITE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version
android.sdk = 33

# (str) Android NDK version
android.ndk = 25b

# (int) Android NDK API to use
android.ndk_api = 21

# (str) Build tools version (stable)
android.build_tools = 33.0.2

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

# (list) Android architectures
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable full backup feature
android.allow_backup = True



# (int) Log level (0 = errors only, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1