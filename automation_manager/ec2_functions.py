import logging
from botocore.exceptions import ClientError
from .utils import get_instance_name


def start_instance(ec2, instance_id: str):
    instance = ec2.Instance(instance_id)
    state = instance.state["Name"]
    
    logging.info(
        f"start_instance called: {instance_id}, state={state}, name={get_instance_name(instance)}"
    )

    print(f"[before] {instance.id} state = {state}, name={get_instance_name(instance)}")
    
    if state == "stopped":
        logging.info(f"(Simulation) Starting instance: {instance_id}")
        print(f"[after ] (Simulation) {instance.id} state = running")
    else:
        print("Instance already running.")


def stop_instance(ec2, instance_id: str):
    instance = ec2.Instance(instance_id)
    state = instance.state["Name"]
    
    logging.info(
        f"stop_instance called: {instance_id}, state={state}, name={get_instance_name(instance)}"
    )

    print(f"[before] {instance.id} state = {state}, name={get_instance_name(instance)}")

    if state == "running":
        logging.info(f"(Simulation) Stopping instance: {instance_id}")
        print(f"[after ] (Simulation) {instance.id} state = stopped")
    else:
        print("Instance already stopped.")
