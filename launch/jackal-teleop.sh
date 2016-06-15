#! /bin/bash
source /opt/ros/indigo/setup.bash
cd ~/Clearpath
python ./teleop.py Jackal

read -n1 -r -p "Press any key to exit..." key

  #if [ "$key" = ' ']; then
  #  python ./teleop.py husky
    # Space pressed, do something
    # echo [$key] is empty when SPACE is pressed # uncomment to trace
  #else
  #  echo 'Exiting...'
  #  exit
    # Anything else pressed, do whatever else.
    # echo [$key] not empty
  #fi

echo 'Exiting...'
