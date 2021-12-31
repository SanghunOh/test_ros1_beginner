import rospy
from turtlebot_pkg.getcharwithoutstop import GetCharwithoutStop

pass
if __name__ == '__main__':
    kb = GetCharwithoutStop()
    print('Get char without Stop : w(forward), x(backward)')
    while True:
        key = kb.getch()
        if key == 'w':
            print('forward')
        elif key == 'x':
            print('backward')
        pass
