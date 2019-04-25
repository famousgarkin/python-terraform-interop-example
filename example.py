import shutil
import os
import json
import subprocess

module_dir = './example'
module_template = {
	'resource': {
		'aws_instance': {
			'example': {
				'instance_type': 't2.micro',
				'ami': 'ami-abc123',
			},
		},
	},
}

shutil.rmtree(module_dir)
os.mkdir(module_dir)

with open(module_dir + '/main.tf.json', 'w') as file:
	json.dump(module_template, file, indent='\t')

for cmd in [
	['terraform', 'init', '--upgrade'],
	['terraform', 'apply'],
]:
	subprocess.check_call(cmd, cwd=module_dir)
