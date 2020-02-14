# PySide2 - Qt for Python

ref: Qt for Python Tutorials [https://doc.qt.io/qtforpython/tutorials/index.html](https://doc.qt.io/qtforpython/tutorials/index.html)

## install

- qt5, PySide2 and other libraries

  ```sh
  # PySide2
  pip3 install PySide2

  # pyqt5
  pip3 install pyqt5
  #
  # or install by apt-get
  # apt-get install python3-pyqt5

  # pandas
  pip install pandas
  ```

- Designer

  ref:

  - [https://stackoverflow.com/a/58735899](https://stackoverflow.com/a/58735899)
  - [https://pythonbasics.org/qt-designer-python/](https://pythonbasics.org/qt-designer-python/)

  ```sh
  apt install pyqt5-dev-tools pyqt5-dev
  apt install qttools5-dev qttools5-dev-tools qttools5-doc qttools5-examples

  # add /usr/lib/x86_64-linux-gnu/qt5/bin into PATH in ~/.bashrc
  echo "" >> ~/.bashrc
  echo "export PATH=/usr/lib/x86_64-linux-gnu/qt5/bin:$PATH" >> ~/.bashrc
  source ~/.bashrc

  # execute designer
  designer

  # convert designed .ui file(mainwindow.ui) to python file(ui_mainwindow.py)
  pyside2-uic mainwindow.ui > ui_mainwindow.py
  ```

## Tips

- Qt for Python Signals and Slots [https://wiki.qt.io/Qt_for_Python_Signals_and_Slots](https://wiki.qt.io/Qt_for_Python_Signals_and_Slots)
