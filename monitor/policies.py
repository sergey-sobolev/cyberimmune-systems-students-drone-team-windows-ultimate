import httpx

auth_url = "http://localhost:8003/service"


def check_operation(id, details):
    # print(f"[debug] checking policies for event {id}, details: {details}")
    print(f"[info] checking policies for event {id},"
          f" {details['source']}->{details['deliver_to']}: {details['operation']}")
    details['source'] = get_source(details['source'])
    src = details['source']
    dst = details['deliver_to']
    command = details['command']

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
    # kea - Kafka events analyzer - an extra service for internal monitoring,
    # can only communicate with itself
    if src == 'kea' and dst == 'kea' \
            and (command == 'self_test' or command == 'test_param'):
        return True

    return False


def get_source(jwt: str):
    response = httpx.get(auth_url, {"token": jwt})
    if (response is None):
        print("---------------------")
        print("authentication failed")
        print("---------------------")
    return response.text
