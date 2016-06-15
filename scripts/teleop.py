#! /usr/bin/env python3
# Usage: teleop.py [robot name] [controller type]
#           robot name: jackal | husky | simulation
#           controller: gamepad | controller | keyboard | mouse

import rospy
from geometry_msgs.msg import Twist
import sys
import os
import subprocess
#import logging

import curses
from curses import wrapper

#logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', filename='teleop.log', filemode='a', level=logging.INFO)

twist = Twist()
#power = 1

def getinputs():
    #print len(sys.argv)
    control = None
    robot = None
    #power = 1

    for index in range(1,len(sys.argv)):
        arg = sys.argv[index]
        #print arg
        if arg=='jackal' or arg=='Jackal' or arg=='husky' or arg=='Husky' or arg=='sim' or arg=='simulation' or arg=='gazebo':
            robot = arg

        elif arg=='Gamepad' or 'gamepad' or arg=='controller' or arg=='cont' or arg=='contr' or arg=='key' or arg=='keyboard' or 'mouse':
            control = arg

        else:
            #try:
            numb=int(arg)
            print numb
            #power = float(numb)

            #except ValueError:
            #    #power = 0
    if control == None:
        control = 'Gamepad'

    return (robot, control) #power)

def ros_master(robot):
    if len(sys.argv) == 1:
        robot = raw_input('\nWhich robot would you like to control? \n')

        if robot == 'jackal' or robot == 'Jackal':
            loc = 'http://cpr-uaf01:11311'

        elif robot == 'husky' or robot == 'Husky':
            loc = 'http://cpr-uaf02-husky:11311'

        elif robot == 'sim' or robot == 'simulation' or robot == 'gazebo':
            resp = raw_input('\nType the IP address of the simulation server.\n')
            loc = 'http://' + resp + ':11311'

        else:
            print '\nUsage: teleop.py [robot name] [controller type]\n\n\trobot name: jackal | husky | simulation\n\tcontroller: gamepad | controller | keyboard | mouse\n'#\tdrive power: Any whole number (no change when using gamepad control)\n'
            exit()

    else:
        if robot == 'jackal' or robot == 'Jackal':
            loc = 'http://cpr-uaf01:11311'

        elif robot == 'husky' or robot == 'Husky':
            loc = 'http://cpr-uaf02-husky:11311'

        elif robot == 'sim' or robot == 'simulation' or robot == 'gazebo':
            resp = raw_input('\nType the IP address of the simulation server.\n')
            loc = 'http://' + resp + ':11311'

        else:
            robot = raw_input('Which robot would you like to control? \n')

            if robot == 'jackal' or robot == 'Jackal':
                loc = 'http://cpr-uaf01:11311'

            elif robot == 'husky' or robot == 'Husky':
                loc = 'http://cpr-uaf02-husky:11311'

            elif robot == 'sim' or robot == 'simulation' or robot == 'gazebo':
                resp = raw_input('\nType the IP address of the simulation server.\n')
                loc = 'http://' + resp + ':11311'

            else:
                print '\nUsage: teleop.py [robot name] [controller type]\n\n\trobot name: jackal | husky | simulation\n\tcontroller: gamepad | controller | keyboard | mouse\n'#\tdrive power: Any whole number (no change when using gamepad control)\n'
                exit()

    return loc

def keyboard():
    pub = rospy.Publisher('/cmd_vel',Twist, queue_size=1)
    rospy.init_node('teleop_py',anonymous=True)
    rate = rospy.Rate(10)
    stdscr = curses.initscr()
    stdscr.keypad(True)

    while not rospy.is_shutdown():
        twist = wrapper(values)
        pub.publish(twist)
        #rate.sleep()

def gamepad(robot):
    if robot == 'jackal' or robot == 'Jackal':
        string = 'roslaunch jackal_control teleop.launch'
        subprocess.call(string, shell=True)
        #subprocess.call(string, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

    elif robot == 'husky' or robot == 'Husky':
        string = 'roslaunch husky_control teleop.launch'
        subprocess.call(string, shell=True)
        #subprocess.Popen(string, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

    else:
        resp = raw_input('\nWhich robot are you simulating?\n')

        if resp == 'jackal' or resp == 'Jackal':
            string = 'roslaunch jackal_control teleop.launch'
            subprocess.call(string, shell=True)
            #subprocess.Popen(string, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

        elif resp == 'husky' or resp == 'Husky':
            string = 'roslaunch husky_control teleop.launch'
            subprocess.call(string, shell=True)
            #subprocess.Popen(string, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

        else:
            print '\nUsage: teleop.py [robot name] [controller type]\n\n\trobot name: jackal | husky | simulation\n\tcontroller: gamepad | controller | keyboard | mouse\n'#\tdrive power: Any whole number (no change when using gamepad control)\n'
            exit()

def controller(control):
    if control == None:
        gamepad(robot)
    elif control == 'controller' or 'gamepad' or 'Gamepad' or 'contr' or 'cont':
        gamepad(robot)
    elif control == 'key' or control == 'keyboard':
        keyboard()
    elif control == 'mouse':
        exit()
    else:
        print '\nUsage: teleop.py [robot name] [controller type]\n\n\trobot name: jackal | husky | simulation\n\tcontroller: gamepad | controller | keyboard | mouse\n'#\tdrive power: Any whole number (no change when using gamepad control)\n'
        exit()

def values(stdscr):
    stdscr.clear()
    #print '(w for forward, a for left, s for reverse, d for right,k for turning left,l for turning right and . to exit)' + '\n'

    keys=stdscr.getch()
    #s = raw_input(':- ')
    if keys == ord('w') or keys == curses.KEY_UP:
        twist.linear.x = 0.5 #* power
        twist.angular.z = 0.0
        twist.linear.y = 0.0

    elif keys == ord('s') or keys == curses.KEY_DOWN:
        twist.linear.x = -0.5 #* power
        twist.angular.z = 0.0
        twist.linear.y = 0.0

    elif keys == ord('a') or keys == curses.KEY_LEFT:
        twist.angular.z = 1.0 #* power
        twist.linear.x = twist.linear.y = 0.0
    elif keys == ord('d') or keys == curses.KEY_RIGHT:
        twist.angular.z = -1.0 #* power
        twist.linear.x = twist.linear.y = 0.0
    elif keys == ord('.') or keys == ord('x'):
        twist.angular.z = twist.linear.x = twist.linear.y = 0.0
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        sys.exit()

    else:
        twist.linear.x = twist.linear.y = twist.angular.z = 0.0
        print 'Wrong command entered \n'


    stdscr.refresh()
    return twist

if __name__ == '__main__':
    try:
        robot, control=getinputs()
        #print 'robot=%s' %robot
        #print 'control=%s' %control
        #print 'power=%s' % power

        loc = ros_master(robot)
        #print 'Drive Power: %d' %power
        os.environ['ROS_MASTER_URI'] = loc
        print '\nConnecting to %s using %s...' %(robot, control)
        controller(control)
    except rospy.ROSInterruptException:
        pass
