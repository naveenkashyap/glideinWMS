#!/bin/env python
#
# cat_StartdLog.py
#
# Print out the StartdLog for a glidein output file
#
# Usage: cat_StartdLog.py logname
#

import sys
STARTUP_DIR=sys.path[0]
sys.path.append(os.path.join(STARTUP_DIR,"lib"))
import gWftLogParser

USAGE="Usage: cat_StartdLog.py <logname>"

def main():
    try:
        print gWftLogParser.get_CondorLog(sys.argv[1],"StartdLog")
    except:
        sys.stderr.write("%s\n"%USAGE)
        sys.exit(1)


if __name__ == '__main__':
    main()
 
