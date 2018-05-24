#!/usr/bin/env python

import rospy
import smach, smach_ros
from std_msgs.msg import *

# Power_Flag: 0: Always ON; 1: Normal; 2: standby
power_flag = 0


def switchToNormal(msg):
    global power_flag
    power_flag = 1
    pass

def switchToAlwaysOn(msg):
    global power_flag
    if msg.data == True:
        power_flag = 0
    pass


def switchToNormal(msg):
    global power_flag
    if msg.data == True:
        power_flag = 1
    pass


# define state AlwaysOn
class power_AlwaysOn(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['to_Normal'])

    def execute(self, userdata):
        global power_flag
        rospy.loginfo('power mode >>> AlwaysOn.')
        if power_flag == 1:
            rospy.loginfo('>>>>>>> Switch to Normal Power Mode.')
            return 'to_Normal'


# define power state : normal
class power_Normal(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['to_AlwaysOn', 'to_Standby'])

    def execute(self, userdata):
        global power_flag
        rospy.loginfo('power mode >>> Normal.')
        if power_flag == 0:
            rospy.loginfo('>>>>>>> Switch to AlwaysOn Mode.')
            return 'to_AlwaysOn'
        elif power_flag == 2:
            rospy.loginfo('>>>>>>> Switch to Standby Mode.')
            return 'to_Standby'


# define power state : normal
class power_Standby(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['to_AlwaysOn', 'to_Normal'])

    def execute(self, userdata):
        global power_flagor
        rospy.loginfo('power mode >>> Standby.')
        if power_flag == 0:
            rospy.loginfo('>>>>>>> Switch to AlwaysOn Mode.')
            return 'to_AlwaysOn'
        elif power_flag == 1:
            rospy.loginfo('>>>>>>> Switch to Normal Mode.')
            return 'to_Normal'

# define state Bas
class AMR_On(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['power_Normal'])

    def execute(self, userdata):
        rospy.sleep(3.0)
        rospy.loginfo('Start Power Management.')
        return 'power_Normal'

def main():
    rospy.init_node('smach_example_state_machine')
    rospy.Subscriber('/switchToAlwaysOn', Bool, switchToAlwaysOn)
    rospy.Subscriber('/switchToNormal', Bool, switchToNormal)
    # Create the top level SMACH state machine
    sm_top = smach.StateMachine(outcomes=['outcome6'])

    # Open the container
    with sm_top:
        smach.StateMachine.add('BAS', Bas(),
                               transitions={'outcome3': 'CON'})

        # Create the sub SMACH state machine
        # Once the outcome meet the outcome_map, sm_con publish 'outcome5' and leave the con state machine.
        sm_con = smach.Concurrence(outcomes=['outcome4', 'outcome5'],
                                   default_outcome='outcome4',
                                   outcome_map={'outcome5':
                                                    {'FOO': 'outcome2',
                                                     'BAR': 'outcome1'}})

        # Open the container
        with sm_con:
            # Add states to the container
            smach.Concurrence.add('FOO', Foo())
            smach.Concurrence.add('BAR', Bar())

        smach.StateMachine.add('CON', sm_con,
                               transitions={'outcome4': 'CON',
                                            'outcome5': 'outcome6'})
    # Create and start the introspection server
    sis = smach_ros.IntrospectionServer('server_name', sm_top, '/SM_ROOT')
    sis.start()
    # Execute SMACH plan
    outcome = sm_top.execute()
    sis.stop()


if __name__ == '__main__':
    rospy.init_node('NaviCenter')
    main()


