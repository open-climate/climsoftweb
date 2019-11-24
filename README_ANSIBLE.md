# climsoftweb-setup

During development, you may want to use ansible to set up the environment,
but then use a local copy of the code. Currently ansible pulls the latest
version of climsoftweb from GitHub.

Therefore, after deploying, we set up a symbolic link to the local copy:

```
# remove the symbolic link if it exists
rm /webapps/climsoftweb
cd /tmp/climsoftwebinstall/climsoftweb-setup/
ansible-playbook --ssh-extra-args=-A -i development webservers.yml -K -vvvv                                          

cd /webapps/climsoftweb
mv climsoftweb climsoftweb_github  # or just delete it 
ln -s /media/sf_data/work/projects/climsoftweb/git/climsoft

```

# climsoftweb

Run the development server with something like:
```
cd /webapps/climsoftweb/
. bin/activate
cd climsoftweb
./manage.py runserver 192.168.1.161:8080

```
