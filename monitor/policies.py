import httpx


def check_operation(id, details):
    src = details['source']
    dst = details['deliver_to']
    command = details['command']

    print(f"[info] checking policies for event {id},"
          f" {details['source']}->{details['deliver_to']}: {details['operation']}")

    if src == 'mobile_app' and dst == 'fly_control' and command == 'start':
        return True
    if src == 'mobile_app' and dst == 'fly_control' and command == 'stop':
        return True
    if src == 'fly_control' and dst == 'control_center' and command == 'get_task':
        return True
    if src == 'control_center' and dst == 'fly_control' and command == 'get_task':
        return True
    if src == 'control_center' and dst == 'mobile_app' and command == 'get_task':
        return True
    if src == 'drone_state_control' and dst == 'mobile_app' and command == 'error':
        return True
    if src == 'fly_control' and dst == 'mobile_app' and command == 'error':
        return True
    if src == 'mobile_app' and dst == 'control_center' and command == 'error':
        return True
    if src == 'fly_control' and dst == 'drone_state_control' and command == 'error':
        return True
    if src == 'drone_state_control' and dst == 'fly_control' and command == 'error':
        return True
    if src == 'fly_control' and dst == 'gps' and command == 'get_coordinates':
        return True
    if src == 'gps' and dst == 'fly_control' and command == 'get_coordinates':
        return True
    if src == 'gps' and dst == 'env_control' and command == 'get_coordinates':
        return True
    if src == 'fly_control' and dst == 'mobile_app' and command == 'get_drone_state':
        return True
    if src == 'mobile_app' and dst == 'fly_control' and command == 'get_drone_state':
        return True
    if src == 'fly_control' and dst == 'control_center' and command == 'error':
        return True
    if src == 'fly_control' and dst == 'env_control' and command == 'start':
        return True
    if src == 'env_control' and dst == 'fly_control' and command == 'start':
        return True
    if src == 'fly_control' and dst == 'mobile_app' and command == 'noise':
        return True
    if src == 'mobile_app' and dst == 'fly_control' and command == 'stop':
        return True
    if src == 'fly_control' and dst == 'mobile_app' and command == 'notification':
        return True
    if src == 'fly_control' and dst == 'sprayer' and command == 'start':
        return True
    if src == 'env_control' and dst == 'sprayer' and command == 'stop':
        return True
    if src == 'env_control' and dst == 'fly_control' and command == 'noise':
        return True
    if src == 'fly_control' and dst == 'control_center' and command == 'noise':
        return True
    if src == 'fly_control' and dst == 'control_center' and command == 'report':
        return True

    if src == 'kea' and dst == 'kea' \
            and (command == 'self_test' or command == 'test_param'):
        return True

    print(f"[error] event {id} was denied due to policies")

    return False
