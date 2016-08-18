Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv
* Django and Gunicorn are installed in the virtualenv

e.g. on Ubuntu (server):

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host Configuration

* see nginx.template.conf
* replace SITENAME with desired sitename, e.g. domainName-staging.com
* used in `/etc/nginx/sites-available` with a symlink to `/etc/nginx/sites-enabled`

## Upstart Job Script

* see gunicorn-upstart.template.conf
* replace SITENAME with desired sitename, e.g. domainName-staging.com
* used in `/etc/init/gunicorn-benjamingrove-staging.ml.conf `

## Folder Structure:
Assume we have a user account at /home/username (~)

/home/username  
└── sites    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── SITENAME  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── database  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── source  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── static  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── virtualenv  
