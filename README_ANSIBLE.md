cd /tmp/climsoftwebinstall/climsoftweb-setup/
ansible-playbook --ssh-extra-args=-A -i development webservers.yml -K -vvvv                                          
