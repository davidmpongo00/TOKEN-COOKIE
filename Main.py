apt update && apt upgrade -y
pkg install git
pkg install python
rm -rf TOKEN-COOKIE
git clone --depth=1 https://github.com/U7P4L-IN/TOKEN-COOKIE.git
cd TOKEN-COOKIE
python main.py
