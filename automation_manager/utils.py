import os

def get_instance_name(instance):
    if instance.tags:
        for t in instance.tags:
            if t.get("Key") == "Name":
                return t.get("Value")
    return None


def print_current_resources(ec2, s3):
    print("=== Current EC2 instances ===")
    for instance in ec2.instances.all():
        print("EC2:", instance.id, instance.state["Name"], get_instance_name(instance))

    print("\n=== Current S3 buckets ===")
    for bucket in s3.buckets.all():
        print("S3:", bucket.name)

    print("-" * 40)
