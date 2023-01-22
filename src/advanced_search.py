from advanced_search_pkg.main import *
import os, sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = main()
    main.show()
    sys.exit(app.exec_())