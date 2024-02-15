

#!/bin/bash

# Evaluate the status from a command
date

if [ $? -eq 0 ]    #if the status code = 0 then success else failure
then
  echo "Success"
  exit 0
else
  echo "Failure" >&2
  exit 1
fi
