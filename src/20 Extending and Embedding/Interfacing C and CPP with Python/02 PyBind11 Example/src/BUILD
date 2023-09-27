rm -rf build
cmake -S . -B build
cmake --build build
ls -l build
rm *.so
mv build/*.so .
python testit.py
