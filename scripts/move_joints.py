import omni
from omni.isaac.dynamic_control import _dynamic_control
import numpy as np

safe = True

omni.timeline.get_timeline_interface().play()
dc = _dynamic_control.acquire_dynamic_control_interface()
articulation = dc.get_articulation("/World/kuka_lwr/world")
dof_count = dc.get_articulation_dof_count(articulation)
print(dof_count)
dc.wake_up_articulation(articulation)

if safe:
	joint_angles = [np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])]
else:
	joint_angles = [np.array([0.0, 0.6, 0.5, -0.3, -0.6, 1.8, 0.0])]
	
print(joint_angles)
dc.set_articulation_dof_position_targets(articulation, joint_angles)
joint_state = dc.get_articulation_dof_states(articulation, _dynamic_control.STATE_POS)
print(joint_state)
