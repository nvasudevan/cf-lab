from troposphere import Ref, Template, Parameter, Output, GetAtt, Base64, Join
import troposphere.ec2 as ec2


class MyEc2Template:
    def __init__(self, ec2_name):
        self.ec2_name = ec2_name
        self.tmpl = Template()
        self.ami_id_param = Parameter(
            "AmiId",
            Description="Ami Id",
            Type="String",
            Default="ami-01720b5f421cf0179"
        )
        self.inst_type_param = Parameter(
            "InstanceType",
            Description="Instance Type",
            Type="String",
            Default="t2.micro"
        )

        # add it to template
        self.tmpl.add_parameter(self.ami_id_param)
        self.tmpl.add_parameter(self.inst_type_param)

    def ec2_template(self):
        print(f'=> generating ec2 template, ec2: {self.ec2_name}')
        inst = ec2.Instance(self.ec2_name,
                            ImageId=Ref(self.ami_id_param),
                            InstanceType=Ref(self.inst_type_param),
                            UserData=Base64(
                                Join(
                                    "",
                                    [
                                        "#!/bin/bash -xe\n",
                                        "yum update -y && yum install httpd\n",
                                        "httpd -v"
                                    ]
                                )))

        self.tmpl.add_resource(inst)
        self.tmpl.add_output([
            Output(
                "InstanceId",
                Description="Instance Id of the instance created",
                Value=Ref(inst)
            ),
            Output(
                "PublicIp",
                Description="Public IP of the instance created",
                Value=GetAtt(inst, "PublicIp")
            ),
            Output(
                "PrivateIp",
                Description="Private IP of the instance created",
                Value=GetAtt(inst, "PrivateIp")
            )
        ])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_ec2 = MyEc2Template("cflab")
    my_ec2.ec2_template()
    print(f"ec2 json:\n{my_ec2.tmpl.to_json()}")
    jsonp = "/home/krish/kv/tf-cloud/cf/cf_lab.json"
    with open(jsonp, "w+") as cf_lab_json:
        cf_lab_json.write(my_ec2.tmpl.to_json())
